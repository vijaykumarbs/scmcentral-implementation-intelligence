# Problem framing

## Implementation context

SCM/ERP data migration teams receive source files from business owners, suppliers, and legacy systems. A data analyst must reconcile actual columns and row contents with a target data contract before the file is ready for conversion, mock load, or cutover.

## Current workaround and cost hypothesis

The usual lightweight workaround is a combination of spreadsheets, one-off formulas, analyst judgment, and clarification messages. It is flexible, but checks can vary by workstream, repeated review consumes analyst capacity, and issue context can be lost as rows move between files. These costs are plausible and practitioner-facing, but have not yet been quantified for this product.

## Scope of the first solution

Make explicit, deterministic contract checks repeatable and put findings beside the affected row and field. Keep resolution with the analyst and data owner. This addresses structural and simple quality blockers; it does not establish semantic correctness or readiness beyond the configured rules.

## Evidence needed

Interview an implementation analyst and a data owner, observe one representative validation task, compare against a manually reviewed reference set, and measure elapsed time, false-clear/missed findings, actionable context, and rework loops. See [PRODUCT.md](../PRODUCT.md) for the pilot and prioritization decisions.
