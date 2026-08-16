# V0 Validation Rules

## Required field

A field marked `required: true` must contain a non-empty value.

## Unique field

A field marked `unique: true` must not contain duplicate values.

## String field

A field declared with `type: "string"` is expected to contain a string value.

## Identifier format

Identifier fields must not contain spaces.

For V0, validation is deterministic and local.

The validator does not:
- call external services
- use an LLM
- modify customer data
- infer missing values
- perform semantic validation
- verify values against the internet
