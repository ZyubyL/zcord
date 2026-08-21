"""
MIT LICENSE (c) ZyubyL

Generate Mermaid class diagrams from zcord modules.
"""

import inspect
from pathlib import Path

import zcord


def generate_mermaid_class_diagram(module):
    classes = {
        obj
        for _, obj in inspect.getmembers(module, inspect.isclass)
        if obj.__module__.startswith(module.__name__)
    }

    lines = [
        "---",
        "hide:",
        "  - toc",
        "  - navigation",
        "---",
        "# Zcord Class Diagram",
        "",
        "```mermaid",
        "classDiagram",
        "    direction LR",
        "",
    ]

    lines.extend(
        f"    {base.__name__} <|-- {cls.__name__}"
        for cls in sorted(classes, key=lambda x: x.__qualname__)
        for base in cls.__bases__
        if base in classes
    )

    lines.append("```")
    lines.append("")
    return "\n".join(lines)


cwd = Path.cwd()

file = cwd / "docs" / "class_diagram.md"

file.write_text(generate_mermaid_class_diagram(zcord))
