#!/usr/bin/env python3
"""
extract_pdfs.py — Extrae texto de los PDF de row/ a extracted/ (paso de apoyo de lectura).

Los PDF de row/ son la FUENTE DE LA VERDAD (inmutables). Este script produce texto
plano por página en extracted/<misma ruta relativa>.txt para que el agente pueda leer
y CITAR por página (p. ej. "EF-Junio-2025.pdf · p.12"). No modifica row/.

Uso:
    python tools/extract_pdfs.py                 # extrae solo lo que falta / cambió
    python tools/extract_pdfs.py --force         # re-extrae todo
    python tools/extract_pdfs.py --only "EF-Junio-2025.pdf"   # filtra por subcadena
"""
from __future__ import annotations
import argparse
import hashlib
import sys
from pathlib import Path

try:
    import pdfplumber
except ImportError:
    sys.exit("Falta pdfplumber. Instala con: python -m pip install pdfplumber")

ROOT = Path(__file__).resolve().parent.parent
ROW = ROOT / "row"
OUT = ROOT / "extracted"
PAGE_SEP = "\n\n----- [pág. {n}] -----\n\n"


def file_md5(path: Path) -> str:
    h = hashlib.md5()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def extract_one(pdf: Path, dest: Path, force: bool) -> str:
    dest.parent.mkdir(parents=True, exist_ok=True)
    stamp = dest.with_suffix(".md5")
    current = file_md5(pdf)
    if not force and dest.exists() and stamp.exists() and stamp.read_text().strip() == current:
        return "skip (sin cambios)"
    parts: list[str] = []
    with pdfplumber.open(pdf) as doc:
        n_pages = len(doc.pages)
        for i, page in enumerate(doc.pages, start=1):
            parts.append(PAGE_SEP.format(n=i))
            parts.append(page.extract_text() or "[página sin texto extraíble]")
    header = f"# Extracción de texto — {pdf.name}\n\n> Derivado de `{pdf.relative_to(ROOT).as_posix()}` ({n_pages} págs). NO es fuente; la fuente es el PDF.\n"
    dest.write_text(header + "".join(parts), encoding="utf-8")
    stamp.write_text(current, encoding="utf-8")
    return f"OK ({n_pages} págs)"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true", help="re-extrae todo")
    ap.add_argument("--only", default="", help="filtra por subcadena del nombre")
    args = ap.parse_args()

    pdfs = sorted(p for p in ROW.rglob("*.pdf") if args.only.lower() in p.name.lower())
    if not pdfs:
        print("No se encontraron PDF que coincidan.")
        return
    print(f"{len(pdfs)} PDF a procesar → {OUT.relative_to(ROOT).as_posix()}/\n")
    for pdf in pdfs:
        rel = pdf.relative_to(ROW)
        dest = OUT / rel.with_suffix(".txt")
        try:
            status = extract_one(pdf, dest, args.force)
        except Exception as e:  # noqa: BLE001
            status = f"ERROR: {e}"
        print(f"  {rel.as_posix():<60} {status}")


if __name__ == "__main__":
    main()
