# Implementation Intelligence — System Map

## 1. What are we building?

Implementation Intelligence is a data preparation and validation tool for ERP implementations.

The first use case is customer master data.

The basic problem:

> A customer gives us data in a spreadsheet/CSV. Before that data can be loaded into an ERP or implementation system, we need to identify what is wrong with it.

The current system takes:

1. A target data contract.
2. A customer CSV.

It produces:

1. Structured validation findings.
2. An annotated CSV showing the problem beside the affected row.

## 2. The problem we are solving

ERP implementations frequently require customer master data to be cleaned before loading.

Typical problems include:

- Required values missing.
- Duplicate identifiers.
- Invalid identifier formats.
- Required columns missing.
- Unexpected columns appearing in the input.

Today, much of this work can be performed manually in spreadsheets.

Implementation Intelligence is intended to turn this into a repeatable validation pipeline.

## 3. High-level architecture

```text
                 TARGET CONTRACT
                       |
                       v
CUSTOMER CSV --> CSV LOADER
                       |
                       v
                 Python Rows
                       |
                       v
                VALIDATION ENGINE
                       |
          +------------+------------+
          |            |            |
          v            v            v
       Required      Unique      Identifier
       Validation   Validation   Validation
          |            |            |
          +------------+------------+
                       |
                       v
                Column Validation
                       |
                       v
                    FINDINGS
                       |
                       v
                 CSV WRITER
                       |
                       v
              ANNOTATED CSV
```

The important idea is that each component has a specific responsibility.

## 4. Project structure

```text
src/implementation_intelligence/
|
+-- adapters/
|   |
|   +-- __init__.py
|   +-- contract_loader.py
|   +-- csv_loader.py
|   +-- csv_writer.py
|
+-- core/
|   |
|   +-- __init__.py
|   +-- engine.py
|   +-- validator.py
|
+-- cli/
    |
    +-- __init__.py
    +-- main.py
```

There are also `tests/`, `examples/`, and `docs/` directories.

## 5. Contract

The contract describes what the target system expects.

The current Item Master contract defines fields such as:

- `item_id`
- `item_name`
- `goods_service`
- `item_type`
- `hsn`
- `category`

A field can contain properties such as `required` and `unique`.

For example:

```json
{
  "name": "item_id",
  "required": true,
  "unique": true
}
```

The important architectural idea is that the validator should use the contract to understand what the target system expects rather than hard-code every field specifically for Item Master.

This allows the same validation engine to eventually support other master-data contracts.

## 6. Adapters

### `contract_loader.py`

Reads the contract JSON from disk. It knows how to read the contract, but does not validate data.

### `csv_loader.py`

Reads the customer CSV and converts each row into a Python dictionary.

For example:

```text
item_id,item_name
ITEM-001,Steel Bolt
ITEM-002,Steel Nut
```

becomes approximately:

```python
[
    {"item_id": "ITEM-001", "item_name": "Steel Bolt"},
    {"item_id": "ITEM-002", "item_name": "Steel Nut"},
]
```

### `csv_writer.py`

Creates the validated output CSV. It receives the original rows and findings, groups findings by row, adds `validation_issue`, and writes a new CSV.

It does not decide whether data is valid.

## 7. Validator

`core/validator.py` contains the actual validation rules.

Current rules:

- `required`
- `unique`
- `identifier_format`
- `missing_column`
- `unexpected_column`

### Required-field validation

If a contract says `item_name` is required and a row has an empty value, the validator creates a finding.

### Unique-field validation

If `item_id` is unique and the same value occurs twice, the second occurrence generates a finding.

### Identifier-format validation

The current implementation identifies identifier fields using the `_id` naming convention. An identifier containing spaces produces an error.

### Column validation

The validator compares contract columns with CSV columns and identifies missing required columns, missing optional columns, and unexpected columns.

## 8. Finding

The central internal object is:

```python
@dataclass(frozen=True)
class Finding:
    row: int
    field: str
    rule: str
    severity: str
    message: str
```

A `Finding` represents one detected problem.

Example:

```text
row=5
field=item_id
rule=identifier_format
severity=error
message=Identifier 'ITEM 004' contains spaces
```

This structured representation allows the same finding to support CLI output, CSV output, future Excel output, future APIs, future UI, and future AI-assisted remediation.

## 9. Engine

`core/engine.py` orchestrates validation. It does not contain individual validation rules.

Conceptually:

```text
Load contract
      |
      v
Load CSV
      |
      v
Run required validation
      |
      v
Run unique validation
      |
      v
Run identifier validation
      |
      v
Run column validation
      |
      v
Collect findings
```

`validate()` returns `list[Finding]`.

`validate_with_rows()` returns `rows, findings` because the output writer needs both the original data and validation results.

The existing `validate()` API was kept unchanged so existing callers and tests continue to work.

## 10. Annotated CSV

The writer adds a `validation_issue` column to the original columns.

Example:

```text
item_id,item_name,validation_issue
ITEM-001,Steel Bolt,
ITEM-002,,Required field 'item_name' is empty
ITEM 004,Steel Nut,Identifier 'ITEM 004' contains spaces
```

If one row has multiple problems, the messages are combined in the same cell.

The customer's original file is not modified; a separate validated output is created.

## 11. CLI

`cli/main.py` provides the command-line interface.

Example:

```bash
implementation-intelligence \
  --contract examples/contracts/item-master.contract.json \
  --input examples/input/item-master.csv \
  --output examples/output/item-master.validated.csv
```

The CLI receives arguments, calls the engine, optionally writes the annotated CSV, and prints findings. It should not contain validation rules.

## 12. Complete execution flow

```text
1. CLI receives arguments
          |
          v
2. Engine loads contract
          |
          v
3. Engine loads customer CSV
          |
          v
4. CSV becomes Python dictionaries
          |
          v
5. Required-field rules execute
          |
          v
6. Unique-field rules execute
          |
          v
7. Identifier-format rules execute
          |
          v
8. Column rules execute
          |
          v
9. Findings are collected
          |
          v
10. CSV writer receives rows + findings
          |
          v
11. Findings are attached to affected rows
          |
          v
12. Annotated CSV is written
```

## 13. Tests

The current test suite verifies:

1. Existing Item Master validation behaviour.
2. Missing required column.
3. Missing optional column.
4. CSV output generation.
5. Multiple findings on one row.
6. `validate_with_rows()` returns rows plus findings.

Current checkpoint: **6 tests passing**.

The principle is that meaningful behaviour should eventually have an automated regression test.

## 14. What we have actually built

We have built a small deterministic validation pipeline.

```text
Contract + Customer CSV
          |
          v
Deterministic validation
          |
          v
Structured findings
          |
          v
Annotated CSV
```

This is a foundation, not yet an AI system or complete implementation automation platform.

## 15. What we have NOT built

We do not currently have:

- automatic correction
- suggested corrections
- data transformation
- field mapping
- fuzzy matching
- Excel highlighting
- implementation readiness scoring
- implementation workflow management
- AI-assisted reasoning
- customer-specific learning
- ERP integration
- database persistence
- web UI
- API

These should not be added simply because they sound useful. Each future capability should solve a demonstrated implementation problem.

## 16. Architectural separation

The four major layers are:

```text
ADAPTERS
Read/write external formats

        |
        v

VALIDATORS
Determine whether data violates rules

        |
        v

ENGINE
Orchestrate the validation process

        |
        v

CLI
Interact with the user
```

A useful rule for future development is: put code where its responsibility belongs.

For example, duplicate detection belongs in the validator, not inside the CLI.

## 17. Current limitations

The current implementation is deliberately small.

Known limitations include:

- Identifier fields are currently detected through the `_id` naming convention.
- Column validation operates on the CSV header.
- Missing-column findings have no actual data row to attach to.
- Output is currently CSV rather than formatted Excel.
- The system detects problems but does not fix them.

These are known limitations, not problems to blindly eliminate.

## 18. Why this foundation matters

The deterministic layer provides:

```text
Known input
    +
Known contract
    +
Known rules
    =
Reproducible findings
```

That gives us a reliable foundation for future intelligence.

AI should eventually be introduced where deterministic rules are insufficient.

For example, a customer column such as `Matl Desc` may need to be mapped to a target field such as `item_name`. That is a semantic mapping problem rather than a simple validation problem.

Similarly, customer descriptions may need to be transformed into target-system representations. Those are future problems.

## 19. Product direction

The long-term product should not simply be a CSV validator.

The larger opportunity is:

> An implementation data intelligence layer that reduces the manual effort required to prepare customer data for ERP implementation.

A possible progression is:

```text
Stage 1: Validate
    |
    v
Identify problems

Stage 2: Explain
    |
    v
Explain what is wrong and why

Stage 3: Suggest
    |
    v
Suggest corrections and mappings

Stage 4: Transform
    |
    v
Generate implementation-ready data

Stage 5: Learn
    |
    v
Reuse mappings and decisions across implementations

Stage 6: Automate
    |
    v
Reduce implementation effort significantly
```

The stages should be earned by evidence rather than implemented speculatively.

## 20. 30-second explanation

> I am building a data preparation and validation layer for ERP implementations. A customer provides a CSV and we compare it against a target contract that defines what the implementation system expects. The engine runs deterministic validation rules and produces structured findings. We then generate an annotated CSV where each problematic row contains the issue that needs to be fixed. The current version is deliberately deterministic; AI can be added later where reasoning or mapping is actually valuable.

## 21. Learning checkpoint

Before adding another feature, I should be able to explain:

1. Why the contract exists.
2. Why adapters exist.
3. Why validation logic is separate from the engine.
4. What a `Finding` represents.
5. Why `validate_with_rows()` exists.
6. How a CSV row becomes a Python dictionary.
7. How a finding gets attached to an output row.
8. What the CLI is responsible for.
9. What the current architecture cannot do.
10. Why AI is not yet necessary for the current validation rules.

The goal is not to memorize the code. The goal is to understand the architecture well enough to modify it intentionally.

## 22. Current checkpoint

```text
Validation rules:       Working
Contract loading:       Working
CSV loading:            Working
CLI:                    Working
Annotated CSV writer:    Implemented
Regression tests:       6 passing
```

The immediate next step is:

```text
STOP CODING
      |
      v
UNDERSTAND THE SYSTEM
      |
      v
CRITIQUE THE ARCHITECTURE
      |
      v
IDENTIFY THE REAL NEXT PROBLEM
      |
      v
RESUME IMPLEMENTATION
```

Do not add another feature simply because it is technically easy. The next feature should be selected based on implementation value.
