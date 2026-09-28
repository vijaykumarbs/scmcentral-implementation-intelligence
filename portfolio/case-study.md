# Case study — SCM master-data readiness

## Status

Prototype; pilot not yet run. This page intentionally contains no fabricated client, usage, or impact claims. The example CSV in this repository is illustrative.

## Implementation problem

Before an ERP data load, analysts reconcile customer or item-master extracts against target contracts. Spreadsheet checks are quick to start but often differ between workstreams, and issue lists can lose row-level context as they move between analysts and data owners.

## Product decision

The prototype accepts a target JSON contract and CSV, applies deterministic checks, and emits findings plus an annotated CSV. It deliberately does not calculate a readiness percentage or repair data: those actions could hide the difference between a verified fact and an unresolved assumption.

## Pilot protocol and measures

No pilot has been completed. The next evaluation should use an approved, representative file with a reference set reviewed by an analyst and data owner. Agree the task and thresholds before the run, then report elapsed time, finding precision/recall, actionable evidence, false-clear cases, sample size, and limitations. Do not put customer data in this repository.

## Learning to capture after a pilot

Document participant roles, workflow baseline, contract and record scope, observed results, exceptions, participant feedback, and the product decision that follows. In particular, test whether findings should distinguish customer clarification from implementation-team correction before adding a workflow layer.
