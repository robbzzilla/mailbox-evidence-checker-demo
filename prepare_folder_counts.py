"""Prepare a folder-only evidence batch from a normalized, redacted CSV."""

import argparse
import csv
from datetime import datetime
import json
from pathlib import Path


COLUMNS = (
    "mailbox", "item", "coverage_confirmed", "source_count",
    "approved_exclusions", "target_count", "skipped_items",
)


def read_checks(path):
    checks = []
    seen = set()
    with path.open(encoding="utf-8-sig", newline="") as source:
        rows = csv.DictReader(source, strict=True)
        if tuple(rows.fieldnames or ()) != COLUMNS:
            raise ValueError("Expected these CSV headers in order: " + ",".join(COLUMNS))
        for row in rows:
            if None in row or None in row.values():
                raise ValueError(f"Line {rows.line_num} must have seven fields.")
            fields = {key: value.strip() for key, value in row.items()}
            mailbox, item = fields["mailbox"], fields["item"]
            if not mailbox or not item or (mailbox, item) in seen:
                raise ValueError(f"Line {rows.line_num} needs a unique mailbox and folder pair.")
            seen.add((mailbox, item))
            coverage = fields["coverage_confirmed"].lower()
            if coverage not in ("true", "false"):
                raise ValueError(f"Line {rows.line_num} coverage_confirmed must be true or false.")
            fields["coverage_confirmed"] = coverage == "true"
            for column in COLUMNS[3:]:
                value = fields[column]
                if value.isdecimal():
                    fields[column] = int(value)
                elif not value and column in ("target_count", "skipped_items"):
                    fields[column] = None
                else:
                    raise ValueError(f"Line {rows.line_num} {column} must be a nonnegative integer.")
            if fields["approved_exclusions"] > fields["source_count"]:
                raise ValueError(f"Line {rows.line_num} exclusions exceed the source count.")
            checks.append(dict(fields, kind="folder"))
    if not checks:
        raise ValueError("The CSV needs at least one folder row.")
    return checks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("--source-cutoff", required=True)
    parser.add_argument("--target-cutoff", required=True)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    try:
        for value in (args.source_cutoff, args.target_cutoff):
            if datetime.fromisoformat(value).utcoffset() is None:
                raise ValueError("Cutoffs need a time and timezone offset.")
        batch = {
            "source_cutoff": args.source_cutoff,
            "target_cutoff": args.target_cutoff,
            "checks": read_checks(args.csv_path),
        }
        payload = json.dumps(batch, indent=2) + "\n"
        with args.output.open("x", encoding="utf-8", newline="\n") as output:
            output.write(payload)
    except (OSError, ValueError, csv.Error) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
