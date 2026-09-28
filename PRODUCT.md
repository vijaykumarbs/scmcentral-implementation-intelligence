# SCM Central — Product brief

## Problem and evidence

In SCM-oriented ERP programs, customer master data is often delivered as CSV/spreadsheet extracts whose structure and quality vary by source. Analysts compare each extract with a target contract, repair missing/duplicate identifiers, and coordinate clarification with business owners through spreadsheets and email. This can make the same checks hard to repeat and leave file readiness dependent on individual analyst practice.

The repository contains an illustrative item-master sample and deterministic prototype. It does not yet contain participant interviews, customer artifacts, or a completed pilot. Rework and handoff delay are problem hypotheses, not measured outcomes.

## Prioritization

Start with a narrow decision-support slice: explicit target contract, deterministic checks, structured findings with row/field evidence, and an annotated output that analysts can use in their existing resolution process. Prioritize missing/required fields, duplicates, identifier format, and unexpected columns because these can block or complicate load preparation. Avoid broad “readiness scores” that could imply more certainty than the rules support.

## Success criteria / pilot

Run with one data analyst and one data owner on an approved, representative item-master extract with a manually reviewed reference set. Capture:

- elapsed analyst time to identify, classify, and route all blocking findings;
- precision and recall against the agreed reference set;
- number of findings with enough row/field context for the owner to act without a clarification loop;
- false confidence: rows marked clear by the tool that the reference review considers unsafe;
- analyst and data-owner feedback on whether annotated CSV fits the current control process.

Set acceptable thresholds with participants before looking at results. The core safety bar is that the tool must not hide a known blocking issue or label a file “ready” beyond the contract rules. Report sample size, contract scope, and limitations; do not claim general ERP readiness from a single pilot.

## Deferred

- readiness percentages, inferred or semantic rules, and AI recommendations;
- automated remediation or customer-data mutation;
- workflow, ownership routing, audit history, and team collaboration;
- ERP connectors, import automation, databases, and generic plugin frameworks;
- broad master-data coverage before validating the item-master workflow.

## Learning goals

Learn which findings drive most rework, which ones analysts can fix versus must clarify with the customer, whether duplicate rows and conflicting duplicates require distinct treatment, what evidence owners need, and where the contract itself is ambiguous. Use those findings to decide if the next increment should be resolution classification or an improved input/contract workflow.
