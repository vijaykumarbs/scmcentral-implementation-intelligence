from pathlib import Path

from implementation_intelligence.adapters.contract_loader import load_contract
from implementation_intelligence.adapters.csv_loader import load_csv
from implementation_intelligence.core.validator import (
    Finding,
    validate_required_fields,
    validate_unique_fields,
    validate_identifier_format,
    validate_columns,
)


def validate(
    contract_path: str | Path,
    input_path: str | Path,
) -> list[Finding]:
    contract = load_contract(contract_path)
    rows = load_csv(input_path)

    findings = []

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

    return findings
