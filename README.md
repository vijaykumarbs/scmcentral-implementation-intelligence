# SCM Central — Implementation Intelligence

ERP data migration work often starts with a contract in one place and customer-owned CSV extracts in another. Business analysts and data leads compare columns, chase missing identifiers, find duplicates, and build spreadsheet formulas to decide whether a file can move toward load. The cost is repeated analyst effort, inconsistent checks between workstreams, and late clarification cycles with the customer.

SCM Central is a provider-agnostic validation utility for making those readiness checks explicit and repeatable. A target data contract and source CSV produce structured findings and an annotated CSV. The current MVP is deterministic: it does not call an LLM, change customer records, or make the final go/no-go decision for a migration.

The first product question is not whether a rules engine can be made more general. It is whether analysts can classify and resolve real data findings faster without hiding uncertainty. See [PRODUCT.md](PRODUCT.md) for problem evidence, prioritization, pilot criteria, deferred scope, and learning goals; see [architecture](docs/architecture.md) for system boundaries.

**Evidence status:** no completed implementation-team pilot or measured time/quality outcome is recorded yet. The sample item-master data is illustrative, not customer data. Treat the proposed value as a hypothesis until the pilot criteria are measured.

## Current workflow

1. Define expected fields and constraints in a JSON contract.
2. Run the CLI against a CSV extract.
3. Review structured findings and an annotated CSV with row-level issues.
4. Resolve findings in the source workstream; this tool does not write into an ERP.

The current checks cover required fields, uniqueness, identifier format, and expected/missing columns. Read [validation rules](docs/validation-rules.md) and [evaluation plan](docs/evaluation.md) for current limits and proposed validation.

## Run locally

Requires Python 3.14. Install the project in editable mode and run the CLI:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
implementation-intelligence --help
```

Use the included example contract and CSV as a smoke-test input. See the [developer runbook](docs/runbook/START-HERE.md) for environment and workflow details.

## Design and safety

The pipeline separates CSV/contract adapters, deterministic validation rules, and output writing. Findings are evidence for analyst review, not proof that a file is complete, semantically correct, compliant, or safe to load. No automatic correction, ERP write-back, or customer-data persistence is implemented.

## Consulting thesis

PM for SCM-focused ERP who builds the data-readiness and extraction tools implementation teams actually need. This repository focuses on data contract validation; companion tools address spreadsheet transformation, document comparison, and drawing-to-BOM extraction.
