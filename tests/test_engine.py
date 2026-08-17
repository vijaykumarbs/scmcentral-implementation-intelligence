from implementation_intelligence.core.engine import validate


def test_item_master_sample():
    findings = validate(
        "examples/contracts/item-master.contract.json",
        "examples/input/item-master.csv",
    )

    assert len(findings) == 3

    assert any(
        finding.rule == "required"
        and finding.field == "item_name"
        and finding.row == 6
        for finding in findings
    )

    assert any(
        finding.rule == "unique"
        and finding.field == "item_id"
        and finding.row == 4
        for finding in findings
    )

    assert any(
        finding.rule == "identifier_format"
        and finding.field == "item_id"
        and finding.row == 5
        for finding in findings
    )


def test_missing_required_column(tmp_path):
    input_file = tmp_path / "missing-required.csv"

    input_file.write_text(
        "item_id,goods_service,item_type,hsn,category\n"
        "ITEM-001,Goods,RM,731815,Fasteners\n"
    )

    findings = validate(
        "examples/contracts/item-master.contract.json",
        input_file,
    )

    assert any(
        finding.rule == "missing_column"
        and finding.field == "item_name"
        and finding.severity == "error"
        for finding in findings
    )


def test_missing_optional_column(tmp_path):
    input_file = tmp_path / "missing-optional.csv"

    input_file.write_text(
        "item_id,item_name,goods_service,item_type,category\n"
        "ITEM-001,Steel Bolt,Goods,RM,Fasteners\n"
    )

    findings = validate(
        "examples/contracts/item-master.contract.json",
        input_file,
    )

    assert any(
        finding.rule == "missing_column"
        and finding.field == "hsn"
        and finding.severity == "warning"
        for finding in findings
    )
