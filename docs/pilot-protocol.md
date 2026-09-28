# Pilot protocol — item-master data readiness

**Status:** ready to run; not yet run. No participant or outcome is implied by this protocol.

## Question

Can the validator help an implementation analyst identify and route item-master data issues faster than their current spreadsheet workflow, while preserving or improving detection of known blockers?

## Participants and materials

- One ERP/SCM data analyst who performs migration preparation.
- One data owner or experienced reviewer to adjudicate the reference findings.
- One approved, representative item-master CSV and its target contract. Prefer two similarly sized/complex extracts if comparing workflows to reduce practice effects.
- A manually reviewed reference list of blocking issues. Keep customer data in the participant’s approved environment; never commit it here.

Agree confidentiality, storage, and provider restrictions before collecting any file. This tool is deterministic and local in the current MVP; do not upload participant data to a public repository.

## Run

1. Record the normal workflow and agree the task boundary: when work starts, what counts as a reviewed issue, and when the output is ready for handoff.
2. Capture a baseline using the current process on one extract: active analyst minutes, blocking findings, clarification loops, and output format.
3. Use the validator on a comparable extract with the same contract and task boundary. Record active analyst minutes and all accepted/rejected findings.
4. Have the data owner compare both outcomes against the manually adjudicated reference. Record false clears (reference blocker not surfaced), false alarms, and findings that lack enough row/field context to act.
5. Ask analyst and data owner what created or removed effort and whether the annotated CSV fits existing review controls.

If there is only one file, randomize or counterbalance which method is used first and call out the learning effect in the result. Do not treat a small, single-participant pilot as statistically generalizable.

## Measures to report

| Measure | Baseline | Tool-assisted | Notes |
| --- | --- | --- | --- |
| Active analyst minutes |  |  |  |
| Reference blockers |  |  | Count |
| True positives |  |  |  |
| False clears |  |  | Safety-critical; investigate every case |
| False alarms |  |  |  |
| Clarification loops |  |  |  |
| Findings actionable without clarification |  |  |  |
| Analyst / owner feedback |  |  | Short verbatim excerpt only with consent |

Agree decision thresholds before the run. At minimum, stop and investigate any false clear of an agreed blocking issue. Faster completion alone is not success if issue detection or traceability degrades.

## Closeout record

Before describing results publicly, record the date, participant roles (not names unless they consent), source/contract scope, row-count band, method order, metrics, exceptions, limitations, and next product decision. Obtain permission for any quotation or identifiable partner reference. Publish aggregate findings only; do not publish source records, customer identifiers, or confidential remediation details.
