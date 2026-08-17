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
