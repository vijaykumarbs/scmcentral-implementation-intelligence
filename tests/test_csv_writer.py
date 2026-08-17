import csv

from implementation_intelligence.adapters.csv_writer import write_validated_csv
from implementation_intelligence.core.validator import Finding


def test_write_validated_csv(tmp_path):
    rows = [
        {
            "item_id": "ITEM-001",
            "item_name": "Steel Bolt",
        },
        {
            "item_id": "ITEM-002",
            "item_name": "",
        },
    ]

    findings = [
        Finding(
            row=3,
            field="item_name",
            rule="required",
            severity="error",
            message="Required field 'item_name' is empty",
        ),
    ]

    output_file = tmp_path / "validated.csv"

    write_validated_csv(
        rows,
        findings,
        output_file,
    )

    with output_file.open(
        newline="",
        encoding="utf-8",
    ) as file:
        output_rows = list(csv.DictReader(file))

    assert output_rows == [
        {
            "item_id": "ITEM-001",
            "item_name": "Steel Bolt",
            "validation_issue": "",
        },
        {
            "item_id": "ITEM-002",
            "item_name": "",
            "validation_issue": "Required field 'item_name' is empty",
        },
    ]


def test_write_validated_csv_combines_multiple_findings(tmp_path):
    rows = [
        {
            "item_id": "ITEM 001",
            "item_name": "",
        },
    ]

    findings = [
        Finding(
            row=2,
            field="item_name",
            rule="required",
            severity="error",
            message="Required field 'item_name' is empty",
        ),
        Finding(
            row=2,
            field="item_id",
            rule="identifier_format",
            severity="error",
            message="Identifier 'ITEM 001' contains spaces",
        ),
    ]

    output_file = tmp_path / "validated.csv"

    write_validated_csv(
        rows,
        findings,
        output_file,
    )

    with output_file.open(
        newline="",
        encoding="utf-8",
    ) as file:
        output_rows = list(csv.DictReader(file))

    assert (
        output_rows[0]["validation_issue"]
        == "Required field 'item_name' is empty | "
        "Identifier 'ITEM 001' contains spaces"
    )
