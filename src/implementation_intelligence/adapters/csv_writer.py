import csv
from pathlib import Path

from implementation_intelligence.core.validator import Finding


def write_validated_csv(
    rows: list[dict[str, str]],
    findings: list[Finding],
    path: str | Path,
) -> None:
    output_path = Path(path)

    issues_by_row: dict[int, list[str]] = {}

    for finding in findings:
        issues_by_row.setdefault(finding.row, []).append(
            finding.message
        )

    fieldnames = list(rows[0].keys()) if rows else []
    fieldnames.append("validation_issue")

    with output_path.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames,
        )

        writer.writeheader()

        for row_number, row in enumerate(rows, start=2):
            output_row = dict(row)
            output_row["validation_issue"] = " | ".join(
                issues_by_row.get(row_number, [])
            )

            writer.writerow(output_row)
