#!/usr/bin/env python3
import argparse
import json
import re
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def normalize_domain_name(raw_name):
    cleaned = raw_name.strip().lower()
    cleaned = cleaned.replace("\\", " ").replace("/", " ")
    cleaned = re.sub(r"[_\s]+", "-", cleaned)
    cleaned = re.sub(r"[^a-z0-9-]", "", cleaned)
    cleaned = re.sub(r"-{2,}", "-", cleaned).strip("-")

    if not cleaned:
        raise ValueError("Domain name is empty after normalization.")

    return cleaned


def create_domain_files(domain_name, initial_content, project_root=None):
    root = Path(project_root).resolve() if project_root else PROJECT_ROOT
    base_dir = root / "domain-knowledge"
    safe_domain_name = normalize_domain_name(domain_name)

    target_dir = base_dir / safe_domain_name
    inputs_dir = target_dir / "inputs"
    prds_dir = target_dir / "PRDs"
    rules_path = target_dir / "rules.md"

    inputs_dir.mkdir(parents=True, exist_ok=True)
    prds_dir.mkdir(parents=True, exist_ok=True)

    rules_created = False
    if not rules_path.exists():
        rules_path.write_text(
            initial_content.strip() or "# Domain Rules\n",
            encoding="utf-8",
        )
        rules_created = True

    return json.dumps(
        {
            "status": "success",
            "domain_name": safe_domain_name,
            "domain_path": str(target_dir),
            "inputs_path": str(inputs_dir),
            "prds_path": str(prds_dir),
            "rules_path": str(rules_path),
            "rules_created": rules_created,
        }
    )


def main():
    parser = argparse.ArgumentParser(
        description="Create a domain folder with inputs, PRDs, and rules.md."
    )
    parser.add_argument("--domain_name", required=True, help="Domain name to initialize")
    parser.add_argument(
        "--initial_content",
        default="",
        help="Optional initial content for rules.md",
    )
    parser.add_argument(
        "--project_root",
        help="Optional project root override. Defaults to the repository root inferred from this script.",
    )

    args = parser.parse_args()

    try:
        print(
            create_domain_files(
                args.domain_name,
                args.initial_content,
                project_root=args.project_root,
            )
        )
    except Exception as exc:
        print(json.dumps({"status": "error", "message": str(exc)}))
        sys.exit(1)


if __name__ == "__main__":
    main()
