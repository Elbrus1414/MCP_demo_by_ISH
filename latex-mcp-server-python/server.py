#!/usr/bin/env python3
from __future__ import annotations

import logging
import subprocess
from pathlib import Path
from typing import List, Dict, Any

from mcp.server.fastmcp import FastMCP


logger = logging.getLogger("latex‑mcp")
logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s", force=True)  

mcp = FastMCP("latex-beamer-mcp", version="1.0.0")


def _wrap(message: str) -> Dict[str, Any]:
    return {"content": [{"type": "text", "text": message}]}


@mcp.tool()
def create_beamer_presentation(
    title: str,
    output_path: str,
    author: str = "",
    theme: str = "Madrid",
):
    """Generate a minimal Beamer .tex boilerplate and save it."""

    tex_source = f"""\\documentclass{{beamer}}
\\usetheme{{{theme}}}

\\title{{{title}}}
\\author{{{author}}}
\\date{{\\today}}

\\begin{{document}}

\\frame{{\\titlepage}}

\\begin{{frame}}
\\frametitle{{Содержание}}
\\tableofcontents
\\end{{frame}}

% ---- Add slides below this line ----

\\end{{document}}
"""
    out_path = Path(output_path).expanduser()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(tex_source, encoding="utf-8")
    logger.info("beamer .tex written → %s", out_path)
    return _wrap(f"Presentation saved to {out_path}")


@mcp.tool()
def compile_latex(input_file: str, output_dir: str = "."):
    """Compile a .tex file to PDF with *pdflatex* (two passes)."""

    tex_path = Path(input_file).expanduser()
    if not tex_path.exists():
        raise FileNotFoundError(f"Input file {tex_path} does not exist")

    out_dir = Path(output_dir).expanduser()
    out_dir.mkdir(parents=True, exist_ok=True)

    cmd: List[str] = [
        "pdflatex",
        "-interaction=nonstopmode",
        "-halt-on-error",
        f"-output-directory={out_dir}",
        str(tex_path),
    ]

    for pass_idx in (1, 2):
        proc = subprocess.run(
            cmd,
            check=False,
            stdout=subprocess.PIPE,  
            stderr=subprocess.PIPE,
            text=True,
        )
        if proc.returncode != 0:
            logger.error("pdflatex pass %d failed: %s", pass_idx, proc.stderr.strip())
            raise RuntimeError(f"pdflatex error (pass {pass_idx}): see server stderr for details")

    pdf_path = out_dir / tex_path.with_suffix(".pdf").name
    logger.info("PDF compiled → %s", pdf_path)
    return _wrap(f"PDF generated at {pdf_path}")


@mcp.tool()
def add_slide(file_path: str, slide_title: str, slide_content: str):
    """Append a \begin{frame}…\end{frame} block before \end{document}."""

    path = Path(file_path).expanduser()
    if not path.exists():
        raise FileNotFoundError(f"File {path} does not exist")

    tex = path.read_text(encoding="utf-8")
    slide = f"""

\\begin{{frame}}
\\frametitle{{{slide_title}}}
{slide_content}
\\end{{frame}}
"""
    if "\\end{document}" not in tex:
        raise ValueError("Could not find \\end{document} marker in the .tex file")

    updated = tex.replace("\\end{document}", f"{slide}\n\\end{document}")
    path.write_text(updated, encoding="utf-8")
    logger.info("Slide appended → %s", path)
    return _wrap(f'Slide "{slide_title}" appended to {path}')


if __name__ == "__main__":
    mcp.run()
