"""Slice pages [start..end] (1-indexed inclusive) from a PDF into a new file.

Usage:
    python scripts/slice_pdf.py <src.pdf> <dst.pdf> <start> <end>
"""
from __future__ import annotations
import sys
from pathlib import Path
import pypdfium2 as pdfium


def slice_pdf(src: Path, dst: Path, start: int, end: int) -> None:
    with pdfium.PdfDocument(str(src)) as src_doc:
        n = len(src_doc)
        if not (1 <= start <= end <= n):
            raise ValueError(f"Page range {start}-{end} out of bounds (PDF has {n} pages)")
        with pdfium.PdfDocument.new() as dst_doc:
            # import_pages accepts 0-indexed page indices
            dst_doc.import_pages(src_doc, list(range(start - 1, end)))
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst_doc.save(str(dst))
    print(f"Wrote {dst} ({end - start + 1} pages, {dst.stat().st_size:,} bytes)")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(__doc__, file=sys.stderr)
        sys.exit(2)
    slice_pdf(Path(sys.argv[1]), Path(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
