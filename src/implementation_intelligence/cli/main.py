import argparse

from implementation_intelligence.core.engine import validate


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate customer data against a target contract."
    )

    parser.add_argument(
        "--contract",
        required=True,
        help="Path to the target contract JSON file.",
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to the customer CSV file.",
    )

    args = parser.parse_args()

    findings = validate(
        args.contract,
        args.input,
    )

    print(f"Findings: {len(findings)}")

    for finding in findings:
        print(
            f"row={finding.row} "
            f"field={finding.field} "
            f"rule={finding.rule} "
            f"severity={finding.severity} "
            f"message={finding.message}"
        )


if __name__ == "__main__":
    main()
