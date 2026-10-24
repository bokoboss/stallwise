#!/usr/bin/env python3
"""Validate Stallwise JSON Schemas and their examples.

- Every *.schema.json under schemas/<version>/ must be a valid Draft 2020-12 schema.
- Every examples/*.json must validate against the schema named by its prefix.
- Every examples/invalid/*.json must FAIL validation.

Usage: python3 scripts/validate_schemas.py [schemas/v0]
Requires: jsonschema>=4.18 (with referencing).
"""
import json
import pathlib
import sys

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

PREFIX_TO_SCHEMA = {
    "project": "project.schema.json",
    "rule-set": "rule-set.schema.json",
    "layout": "layout.schema.json",
    "cli": "cli.schema.json",
    "imagery-source": "imagery-source.schema.json",
}


def schema_for(path: pathlib.Path) -> str:
    stem = path.name
    # invalid files are named <description>.<prefix>.json
    parts = stem.split(".")
    for prefix, schema in PREFIX_TO_SCHEMA.items():
        if parts[0] == prefix or (len(parts) >= 2 and parts[-2] == prefix):
            return schema
    raise SystemExit(f"cannot map {path} to a schema")


def main() -> int:
    root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "schemas/v0")
    schemas = {p.name: json.loads(p.read_text(encoding="utf-8")) for p in root.glob("*.schema.json")}
    failures = 0

    resources = []
    for name, schema in schemas.items():
        Draft202012Validator.check_schema(schema)
        resources.append((schema["$id"], Resource.from_contents(schema)))
    registry = Registry().with_resources(resources)
    print(f"ok    {len(schemas)} schemas are valid Draft 2020-12")

    def validator(name):
        return Draft202012Validator(schemas[name], registry=registry, format_checker=FormatChecker())

    for path in sorted((root / "examples").glob("*.json")):
        errors = list(validator(schema_for(path)).iter_errors(json.loads(path.read_text(encoding="utf-8"))))
        if errors:
            failures += 1
            print(f"FAIL  {path} should be valid:")
            for e in errors[:5]:
                print(f"        {'/'.join(map(str, e.absolute_path))}: {e.message[:200]}")
        else:
            print(f"ok    {path}")

    for path in sorted((root / "examples" / "invalid").glob("*.json")):
        valid = validator(schema_for(path)).is_valid(json.loads(path.read_text(encoding="utf-8")))
        if valid:
            failures += 1
            print(f"FAIL  {path} should be rejected")
        else:
            print(f"ok    {path} rejected")

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
