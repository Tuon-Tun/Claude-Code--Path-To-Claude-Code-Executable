#!/usr/bin/env python3
import argparse
import json
import os
import re
import sys
import tempfile


REVIEWER_NOTE_PATTERN = re.compile(
    r"(?ms)^> \[!WARNING\] REVIEWER'S NOTE \(RN-\d+\)\n"
    r"(?:^> .*\n?)+"
    r"(?:\n|$)"
)

DIAGRAM_FENCE_PATTERN = re.compile(
    r"(?im)^```(?:plantuml|xml)\s*$"
)


def strip_reviewer_notes(markdown_content):
    return REVIEWER_NOTE_PATTERN.sub("", markdown_content)


def find_export_warnings(markdown_content, strip_notes=True):
    warnings = []
    if strip_notes and REVIEWER_NOTE_PATTERN.search(markdown_content):
        warnings.append("Reviewer notes were removed from the DOCX export.")
    if DIAGRAM_FENCE_PATTERN.search(markdown_content):
        warnings.append(
            "Diagram code fences are exported as source text unless pre-rendered images are provided."
        )
    return warnings


def prepare_markdown_for_export(input_file, strip_notes=True):
    with open(input_file, "r", encoding="utf-8") as file:
        markdown_content = file.read()

    warnings = find_export_warnings(markdown_content, strip_notes=strip_notes)
    if strip_notes:
        markdown_content = strip_reviewer_notes(markdown_content)

    return markdown_content, warnings


def convert_md_to_docx(input_file, output_file, strip_notes=True):
    """
    Convert a Markdown file to a DOCX file.
    """
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file not found: {input_file}")

    try:
        import pypandoc
    except ImportError as exc:
        raise RuntimeError(
            "pypandoc is not installed. Install pypandoc-binary or pypandoc first."
        ) from exc

    output_dir = os.path.dirname(os.path.abspath(output_file))
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    extra_args = [
        "--toc",
        "--standalone",
        "-V",
        "geometry:margin=1in",
    ]

    markdown_content, warnings = prepare_markdown_for_export(
        input_file, strip_notes=strip_notes
    )

    temp_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".md",
            delete=False,
            encoding="utf-8",
        ) as temp_file:
            temp_file.write(markdown_content)
            temp_path = temp_file.name

        try:
            pypandoc.convert_file(
                temp_path,
                "docx",
                outputfile=output_file,
                extra_args=extra_args,
            )
        except OSError as exc:
            raise RuntimeError(
                "Pandoc is not installed or not available in PATH."
            ) from exc
        except Exception as exc:
            raise RuntimeError(f"Failed to convert Markdown to DOCX: {exc}") from exc
    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)

    return os.path.abspath(output_file), warnings


def sanitize_filename(filename):
    name = (filename or "PRD_Document.docx").strip()
    if not name.lower().endswith(".docx"):
        name = f"{name}.docx"
    return re.sub(r'[<>:"/\\|?*]+', "_", name)


def default_docx_path(input_file):
    base_path = os.path.splitext(os.path.abspath(input_file))[0]
    return f"{base_path}.docx"


def convert_markdown_content_to_docx(
    markdown_content, filename, output_dir=None, strip_notes=True
):
    if not output_dir:
        raise ValueError(
            "output_dir is required when converting inline markdown content."
        )

    safe_filename = sanitize_filename(filename)
    target_dir = os.path.abspath(output_dir)
    os.makedirs(target_dir, exist_ok=True)
    output_path = os.path.join(target_dir, safe_filename)

    temp_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".md",
            delete=False,
            encoding="utf-8",
        ) as temp_file:
            temp_file.write(markdown_content)
            temp_path = temp_file.name

        return convert_md_to_docx(temp_path, output_path, strip_notes=strip_notes)
    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)


def main():
    parser = argparse.ArgumentParser(description="Convert a Markdown PRD to DOCX.")
    parser.add_argument("input", nargs="?", help="Path to the input Markdown file")
    parser.add_argument("output", nargs="?", help="Path to the output DOCX file")
    parser.add_argument(
        "--input_path",
        help="Preferred path to the approved Markdown PRD file",
    )
    parser.add_argument(
        "--output_path",
        help="Preferred target DOCX path",
    )
    parser.add_argument(
        "--filename",
        help="Output DOCX filename when using inline markdown content",
    )
    parser.add_argument(
        "--markdown_content",
        help="Inline Markdown content to convert into DOCX",
    )
    parser.add_argument(
        "--output_dir",
        help="Optional directory where the DOCX file should be written",
    )
    parser.add_argument(
        "--keep_review_notes",
        action="store_true",
        help="Keep inline reviewer notes in the DOCX export. Default is to remove them.",
    )

    args = parser.parse_args()

    try:
        input_path = args.input_path or args.input
        output_path = args.output_path or args.output

        strip_notes = not args.keep_review_notes

        if input_path:
            output_target = output_path or default_docx_path(input_path)
            output_path, warnings = convert_md_to_docx(
                input_path, output_target, strip_notes=strip_notes
            )
        elif args.markdown_content is not None:
            output_path, warnings = convert_markdown_content_to_docx(
                args.markdown_content,
                args.filename or "PRD_Document.docx",
                args.output_dir,
                strip_notes=strip_notes,
            )
        else:
            parser.error(
                "Provide --input_path with --output_path, a positional input file, "
                "or --markdown_content with --filename and --output_dir."
            )

        print(json.dumps({"status": "success", "path": output_path, "warnings": warnings}))
    except Exception as exc:
        print(json.dumps({"status": "error", "message": str(exc)}))
        sys.exit(1)


if __name__ == "__main__":
    main()
