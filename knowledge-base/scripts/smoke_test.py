#!/usr/bin/env python3
import importlib.machinery
import importlib.util
import json
import os
import re
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def fail(message):
    print(json.dumps({"status": "error", "message": message}))
    sys.exit(1)


def load_json(relative_path):
    path = ROOT / relative_path
    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as exc:
        fail(f"Could not read {relative_path}: {exc}")


def load_module(name, relative_path):
    path = ROOT / relative_path
    loader = importlib.machinery.SourceFileLoader(name, str(path))
    spec = importlib.util.spec_from_loader(name, loader)
    if spec is None:
        fail(f"Could not load module spec for {relative_path}")

    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module


def assert_true(condition, message):
    if not condition:
        fail(message)


def check_input_schema():
    schema = load_json("knowledge-base/input-router/resources/output_schema.json")
    required = set(schema.get("required", []))

    expected_required = {
        "Delivery_Mode",
        "Output_Artifacts",
        "Domain_Name",
        "Feature_Name",
        "Input_Type",
        "Core_Objective",
        "Problem_Statement",
        "JTBD_Candidates",
        "Target_Users",
        "Epic_Candidates",
        "Primary_User_Story",
        "User_Story_Candidates",
        "User_Flow",
        "Business_Logic_and_Rules",
        "Functional_Requirements",
        "Non_Functional_Requirements",
        "Success_Metrics",
        "UI_UX_Requirements",
        "API_or_Integration_Notes",
        "Diagram_Requirements",
        "Assumptions",
        "Missing_Information",
    }

    assert_true(schema.get("$schema"), "Input schema is missing $schema")
    assert_true(required == expected_required, "Input schema required fields drifted")

    assert_true(
        set(schema["properties"]["Delivery_Mode"].get("enum", []))
        == {"IDE_FULL_PIPELINE", "CHAT_TEXT_ONLY"},
        "Delivery_Mode enum is invalid",
    )
    assert_true(
        set(schema["properties"]["Output_Artifacts"]["items"].get("enum", []))
        == {"Text Response", "Markdown File", "DOCX File"},
        "Output_Artifacts enum is invalid",
    )

    diagram_items = schema["properties"]["Diagram_Requirements"]["items"]
    assert_true(
        set(diagram_items.get("enum", []))
        == {"None", "Activity Diagram", "Sequence Diagram", "BPMN"},
        "Diagram_Requirements enum is invalid",
    )

    domain_pattern = schema["properties"]["Domain_Name"]["pattern"]
    assert_true(
        re.match(domain_pattern, "payment-gateway") is not None,
        "Domain_Name pattern rejects a valid slug",
    )
    assert_true(
        re.match(domain_pattern, "Payment Gateway") is None,
        "Domain_Name pattern accepts an invalid slug",
    )


def check_export_schema():
    schema = load_json("knowledge-base/docx-converter/resources/export_tool_schema.json")
    input_schema = schema.get("input_schema", {})
    one_of = input_schema.get("oneOf", [])

    assert_true(schema.get("script_path") == "knowledge-base/scripts/export_docx.py", "Export script path drifted")
    assert_true(
        {"input_path", "output_path"}.issubset(input_schema.get("properties", {})),
        "Export schema is missing file-based arguments",
    )
    assert_true(len(one_of) == 2, "Export schema must support file and inline modes")


def check_create_domain_helper():
    create_domain = load_module("create_domain", "knowledge-base/scripts/create_domain.py")

    assert_true(
        create_domain.normalize_domain_name("Payment Gateway") == "payment-gateway",
        "Domain normalization failed",
    )

    with tempfile.TemporaryDirectory() as temp_dir:
        result = json.loads(
            create_domain.create_domain_files(
                "Payment Gateway",
                "# Domain Rules\nSmoke test domain.",
                project_root=temp_dir,
            )
        )

        assert_true(result["status"] == "success", "Domain creation did not succeed")
        assert_true(Path(result["inputs_path"]).is_dir(), "inputs directory was not created")
        assert_true(Path(result["prds_path"]).is_dir(), "PRDs directory was not created")
        assert_true(Path(result["rules_path"]).is_file(), "rules.md was not created")


def check_export_helper():
    export_docx = load_module("export_docx", "knowledge-base/scripts/export_docx.py")

    assert_true(
        export_docx.sanitize_filename('PRD: Feature/Name?.docx')
        == "PRD_ Feature_Name_.docx",
        "Filename sanitization failed",
    )
    assert_true(
        export_docx.default_docx_path("domain-knowledge/demo/PRDs/demo_PRD.md").endswith(
            os.path.join("domain-knowledge", "demo", "PRDs", "demo_PRD.docx")
        ),
        "Default DOCX path failed",
    )
    assert_true(
        "REVIEWER'S NOTE" not in export_docx.strip_reviewer_notes(
            "# PRD\n\n> [!WARNING] REVIEWER'S NOTE (RN-01)\n"
            "> **Risk:** Gap.\n"
            "> **Option A:** Fix A.\n"
            "> **Option B:** Fix B.\n\n"
            "## Next\nContent\n"
        ),
        "Reviewer note stripping failed",
    )


def check_product_framing_skill():
    path = ROOT / "knowledge-base/product-framing/SKILL.md"
    assert_true(path.is_file(), "Product framing skill is missing")

    content = path.read_text(encoding="utf-8")
    assert_true("Product Framing Pack" in content, "Product framing skill is missing its output contract")
    assert_true("Done when" in content, "Product framing skill is missing acceptance criteria guidance")


def main():
    check_input_schema()
    check_export_schema()
    check_create_domain_helper()
    check_export_helper()
    check_product_framing_skill()
    print(json.dumps({"status": "success", "checks": 5}))


if __name__ == "__main__":
    main()
