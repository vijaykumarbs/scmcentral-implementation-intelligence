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

## Implementation Readiness

Implementation readiness is binary. A file is ready according to the rules known to the validator only when it has zero unresolved validation errors. Any unresolved validation error means the file is not ready. The current implementation workflow has no warnings.

The system identifies blocking data problems and will next distinguish errors the implementation team can resolve from those requiring customer clarification or data. Resolution classification belongs to an individual finding, while its policy may come from the contract and/or evidence available to the validator.

Duplicate records need special treatment: identical duplicate rows and conflicting records may require different resolution paths.

## Deferred Scope

Readiness percentages are explicitly deferred. Automatic correction, AI recommendations, workflow management, import automation, databases, and generic rule or plugin frameworks are also deferred.

The next engineering milestone is a small, testable resolution-classification model based on real item-master cases.
