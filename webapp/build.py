#!/usr/bin/env python3
"""Build webapp/index.html by embedding the pipeline prompt sources into app.src.html.

The web app must always run the exact same prompts as the repository pipeline,
so the sources are injected verbatim at build time instead of being copied by hand.
Run this after any change under knowledge-base/, then commit the regenerated index.html.
"""
import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SOURCES = {
    "input_router": "knowledge-base/input-router/SKILL.md",
    "input_schema": "knowledge-base/input-router/resources/output_schema.json",
    "product_framing": "knowledge-base/product-framing/SKILL.md",
    "user_story": "knowledge-base/knowledge/user-story-skill/SKILL.md",
    "template_skill": "knowledge-base/prd-template/SKILL.md",
    "prd_template": "knowledge-base/prd-template/resources/prd-template.md",
    "diagram_writer": "knowledge-base/prd-template/diagram-writer/SKILL.md",
    "reviewer": "knowledge-base/prd-reviewer.md",
}

PLACEHOLDER = '<script type="application/json" id="prompt-data">{"__placeholder__": true}</script>'
MARKER_OPEN = '<script type="application/json" id="prompt-data">'
MARKER_CLOSE = '</script>'


def collect_payload(root=ROOT):
    return {key: (root / path).read_text(encoding="utf-8") for key, path in SOURCES.items()}


def render_html(root=ROOT):
    template = (root / "webapp" / "app.src.html").read_text(encoding="utf-8")
    if PLACEHOLDER not in template:
        raise RuntimeError("app.src.html is missing the prompt-data placeholder")

    # "</" must not appear inside the JSON payload or the browser would close the script tag early.
    payload = json.dumps(collect_payload(root), ensure_ascii=False).replace("</", "<\\/")
    return template.replace(PLACEHOLDER, f"{MARKER_OPEN}{payload}{MARKER_CLOSE}")


def extract_embedded_payload(html):
    start = html.index(MARKER_OPEN) + len(MARKER_OPEN)
    end = html.index(MARKER_CLOSE, start)
    return json.loads(html[start:end])


def main():
    parser = argparse.ArgumentParser(description="Build or verify webapp/index.html.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Verify index.html is in sync with app.src.html and knowledge-base sources.",
    )
    args = parser.parse_args()

    out_path = ROOT / "webapp" / "index.html"
    expected = render_html()

    if args.check:
        if not out_path.is_file():
            print(json.dumps({"status": "error", "message": "webapp/index.html is missing; run build.py"}))
            sys.exit(1)
        if out_path.read_text(encoding="utf-8") != expected:
            print(json.dumps({"status": "error", "message": "webapp/index.html is out of date; run build.py"}))
            sys.exit(1)
        print(json.dumps({"status": "success", "message": "webapp/index.html is in sync"}))
        return

    out_path.write_text(expected, encoding="utf-8")
    print(json.dumps({"status": "success", "path": str(out_path), "embedded_sources": len(SOURCES)}))


if __name__ == "__main__":
    main()
