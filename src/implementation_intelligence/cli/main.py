import argparse

from implementation_intelligence.adapters.csv_writer import write_validated_csv
from implementation_intelligence.core.engine import validate_with_rows


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

    parser.add_argument(
        "--output",
        help="Path to the annotated validation CSV file.",
    )

    args = parser.parse_args()

    rows, findings = validate_with_rows(
        args.contract,
        args.input,
    )

    if args.output:
        write_validated_csv(
            rows,
            findings,
            args.output,
        )

    print(f"Findings: {len(findings)}")

    if args.output:
        print(f"Output: {args.output}")

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
