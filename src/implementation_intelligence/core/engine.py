from pathlib import Path

from implementation_intelligence.adapters.contract_loader import load_contract
from implementation_intelligence.adapters.csv_loader import load_csv
from implementation_intelligence.core.validator import (
    Finding,
    validate_columns,
    validate_identifier_format,
    validate_required_fields,
    validate_unique_fields,
)


def validate_with_rows(
    contract_path: str | Path,
    input_path: str | Path,
) -> tuple[list[dict[str, str]], list[Finding]]:
    contract = load_contract(contract_path)
    rows = load_csv(input_path)

    findings: list[Finding] = []

    findings.extend(
        validate_required_fields(
            rows,
            contract["fields"],
        )
    )

    findings.extend(
        validate_unique_fields(
            rows,
            contract["fields"],
        )
    )

    findings.extend(
        validate_identifier_format(
            rows,
            contract["fields"],
        )
    )

    findings.extend(
        validate_columns(
            rows,
            contract["fields"],
        )
    )

    return rows, findings


def validate(
    contract_path: str | Path,
    input_path: str | Path,
) -> list[Finding]:
    _, findings = validate_with_rows(
        contract_path,
        input_path,
    )

    return findings
