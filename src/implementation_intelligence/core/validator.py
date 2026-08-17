from dataclasses import dataclass


@dataclass(frozen=True)
class Finding:
    row: int
    field: str
    rule: str
    severity: str
    message: str


def validate_required_fields(
    rows: list[dict[str, str]],
    fields: list[dict],
) -> list[Finding]:
    findings: list[Finding] = []

    required_fields = [
        field["name"]
        for field in fields
        if field.get("required") is True
    ]

    for row_number, row in enumerate(rows, start=2):
        for field_name in required_fields:
            value = row.get(field_name, "")

            if not value or not value.strip():
                findings.append(
                    Finding(
                        row=row_number,
                        field=field_name,
                        rule="required",
                        severity="error",
                        message=f"Required field '{field_name}' is empty",
                    )
                )

    return findings


def validate_unique_fields(
    rows: list[dict[str, str]],
    fields: list[dict],
) -> list[Finding]:
    findings: list[Finding] = []

    unique_fields = [
        field["name"]
        for field in fields
        if field.get("unique") is True
    ]

    for field_name in unique_fields:
        seen: dict[str, int] = {}

        for row_number, row in enumerate(rows, start=2):
            value = row.get(field_name, "").strip()

            if not value:
                continue

            if value in seen:
                findings.append(
                    Finding(
                        row=row_number,
                        field=field_name,
                        rule="unique",
                        severity="error",
                        message=(
                            f"Duplicate value '{value}' "
                            f"already found in row {seen[value]}"
                        ),
                    )
                )
            else:
                seen[value] = row_number

    return findings


def validate_identifier_format(
    rows: list[dict[str, str]],
    fields: list[dict],
) -> list[Finding]:
    findings: list[Finding] = []

    identifier_fields = [
        field["name"]
        for field in fields
        if field.get("name", "").endswith("_id")
    ]

    for row_number, row in enumerate(rows, start=2):
        for field_name in identifier_fields:
            value = row.get(field_name, "").strip()

            if value and " " in value:
                findings.append(
                    Finding(
                        row=row_number,
                        field=field_name,
                        rule="identifier_format",
                        severity="error",
                        message=(
                            f"Identifier '{value}' contains spaces"
                        ),
                    )
                )

    return findings


def validate_columns(
    rows: list[dict[str, str]],
    fields: list[dict],
) -> list[Finding]:
    findings: list[Finding] = []

    contract_fields = {
        field["name"]
        for field in fields
    }

    input_fields = set(rows[0].keys()) if rows else set()

    field_definitions = {
        field["name"]: field
        for field in fields
    }

    missing_fields = sorted(contract_fields - input_fields)
    unexpected_fields = sorted(input_fields - contract_fields)

    for field_name in missing_fields:
        field = field_definitions[field_name]
        required = field.get("required") is True

        findings.append(
            Finding(
                row=1,
                field=field_name,
                rule="missing_column",
                severity="error" if required else "warning",
                message=(
                    f"Required contract column '{field_name}' is missing"
                    if required
                    else f"Optional contract column '{field_name}' is missing"
                ),
            )
        )

    for field_name in unexpected_fields:
        findings.append(
            Finding(
                row=1,
                field=field_name,
                rule="unexpected_column",
                severity="warning",
                message=f"Input column '{field_name}' is not defined in the contract",
            )
        )

    return findings
