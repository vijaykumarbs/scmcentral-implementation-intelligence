# SCM Central — Implementation Intelligence product plan

## What it does

The current tool takes a CSV file and a JSON file that lists the target fields and rules. It checks required fields, duplicate values, spaces in identifiers, and missing or unexpected columns. It returns a list of problems and a copy of the CSV with each problem marked beside its row.

It does not fix the data or load it into an ERP. It checks only the rules written in the JSON file.

## Who it is for

An ERP/SCM data analyst preparing item-master data and a data owner who must correct or explain the source records.

## The problem

Before loading master data, an analyst compares each source file with the fields the ERP expects. Teams often do this with spreadsheet formulas, manual checks, and follow-up messages. Each analyst may check the file differently, and a data owner may receive an issue without enough information to find the row.

This describes the problem the tool aims to solve. The example file is sample data. No customer trial, measured time savings, or error reduction has been reported.

## First version

1. Write the expected fields and rules in a JSON contract.
2. Run the command-line tool with the contract and a CSV file.
3. Review the problems found, including the row and field.
4. Send the marked CSV to the person who owns the source data for correction or clarification.

The current checks are fixed and predictable. They do not use AI, check business meaning, look up values online, or change input records.

## Why this scope

Start with checks that can be stated clearly in the target contract: required fields, duplicate values, simple identifier format, and expected columns. Show each issue beside the affected row so the analyst can pass it to the right person. Do not report a percentage score: passing these checks does not prove that all data is correct.

## Not included

- saying that a file is ready for an ERP load;
- deciding whether an issue is the analyst's or customer's responsibility;
- recommending or applying data corrections;
- checking whether values make business sense;
- ERP connections, import jobs, user accounts, or issue tracking.

## Pilot and measures

**Status: no pilot run yet.** Use an approved item-master file and a list of problems reviewed by an analyst and data owner. Time the normal spreadsheet check and the tool-assisted check on the same task or on similar files.

Record:

- minutes spent finding and sharing problems;
- known problems found and missed;
- incorrect problems reported;
- problems that include enough row and field detail to act on;
- follow-up messages needed before the owner can respond.

Agree what counts as an acceptable result before the trial. Investigate every known problem the tool misses. Passing the tool's checks must never be described as proof that a file is safe to load. Do not publish customer files or claim savings without measured results and permission.

## Questions to answer

- Which checks catch the most real problems?
- Which problems can the analyst fix, and which need the data owner?
- Are duplicate rows and conflicting records handled differently by the team?
- Does the marked CSV fit the team's current review process?
