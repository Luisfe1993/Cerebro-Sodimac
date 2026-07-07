#!/usr/bin/env python3
"""
lint.py — Chequeo de salud del wiki (patrón LLM Wiki de Karpathy).

Reporta, sin modificar nada:
- Huérfanos: páginas sin enlaces entrantes (excluye index.md y log.md).
- Enlaces rotos: links markdown a .md inexistentes.
- Frontmatter incompleto: faltan campos requeridos.
- Estado: páginas con estado != verificado (borrador/obsoleto).
- Cobertura: PDF de row/ sin extraer y/o sin citar en el wiki.

Uso:
    python tools/lint.py           # reporte legible
    python tools/lint.py --strict  # además, exit code 1 si hay hallazgos
"""
from __future__ import annotations
import argparse
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
ROW = ROOT / "row"
EXTRACTED = ROOT / "extracted"
ARCHIVE = "_archive_piloto"
REQUIRED_FM = ["tipo", "titulo", "descripcion", "estado", "fuentes"]
LINK_RE = re.compile(r"\]\(([^)]+?\.md)(?:#[^)]*)?\)")


def wiki_pages() -> list[Path]:
    return sorted(p for p in WIKI.rglob("*.md") if ARCHIVE not in p.parts)


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    fm: dict[str, str] = {}
    for line in text[3:end].splitlines():
        m = re.match(r"([A-Za-z_]+):\s*(.*)", line)
        if m:
            fm[m.group(1)] = m.group(2).strip()
    return fm


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()

    pages = wiki_pages()
    content = {p: p.read_text(encoding="utf-8", errors="replace") for p in pages}
    names = {p.name for p in pages}

    findings = 0
    print(f"# Lint del cerebro — {date.today().isoformat()}\n")
    print(f"Páginas activas: {len(pages)}\n")

    # 1. Huérfanos
    print("## 1. Huérfanos (sin enlaces entrantes)")
    orphans = []
    for p in pages:
        if p.name in ("index.md", "log.md"):
            continue
        inbound = sum(1 for q in pages if q != p and p.name in content[q])
        if inbound == 0:
            orphans.append(p.relative_to(WIKI).as_posix())
    if orphans:
        findings += len(orphans)
        for o in orphans:
            print(f"  🔴 {o}")
    else:
        print("  🟢 ninguno")

    # 2. Enlaces rotos
    print("\n## 2. Enlaces rotos (.md inexistente)")
    broken = []
    for p in pages:
        for m in LINK_RE.finditer(content[p]):
            rel = m.group(1)
            if rel.startswith(("http://", "https://")):
                continue
            if not (p.parent / rel).resolve().exists():
                broken.append(f"{p.name} -> {rel}")
    if broken:
        findings += len(broken)
        for b in broken:
            print(f"  🔴 {b}")
    else:
        print("  🟢 ninguno")

    # 3. Frontmatter
    print("\n## 3. Frontmatter incompleto")
    fm_issues = []
    for p in pages:
        if p.name in ("index.md", "log.md"):
            continue
        fm = frontmatter(content[p])
        missing = [k for k in REQUIRED_FM if k not in fm]
        if missing:
            fm_issues.append(f"{p.name}: falta {', '.join(missing)}")
    if fm_issues:
        findings += len(fm_issues)
        for f in fm_issues:
            print(f"  🟡 {f}")
    else:
        print("  🟢 completo")

    # 4. Estado
    print("\n## 4. Estado != verificado")
    estado_issues = []
    for p in pages:
        if p.name in ("index.md", "log.md"):
            continue
        est = frontmatter(content[p]).get("estado", "")
        if est and est != "verificado":
            estado_issues.append(f"{p.name}: {est}")
    if estado_issues:
        for e in estado_issues:
            print(f"  🟡 {e}")
    else:
        print("  🟢 todas verificadas")

    # 5. Cobertura de fuentes
    print("\n## 5. Cobertura de PDF (row/ → extracted/ → citado en wiki)")
    all_wiki_text = "\n".join(content.values())
    pdfs = sorted(ROW.rglob("*.pdf"))
    sin_extraer, sin_citar = [], []
    for pdf in pdfs:
        rel = pdf.relative_to(ROW)
        txt = EXTRACTED / rel.with_suffix(".txt")
        extracted_ok = txt.exists()
        cited = pdf.stem in all_wiki_text or pdf.name in all_wiki_text
        if not extracted_ok:
            sin_extraer.append(rel.as_posix())
        if not cited:
            sin_citar.append(rel.as_posix())
    print(f"  PDF totales: {len(pdfs)} | extraídos: {len(pdfs) - len(sin_extraer)} | citados en wiki: {len(pdfs) - len(sin_citar)}")
    if sin_extraer:
        print("  ⏳ sin extraer:")
        for s in sin_extraer:
            print(f"     - {s}")
    if sin_citar:
        print("  ⏳ sin citar en el wiki (no ingeridos):")
        for s in sin_citar:
            print(f"     - {s}")
    if not sin_extraer and not sin_citar:
        print("  🟢 cobertura completa")

    # Resumen
    status = "🟢 Verde" if findings == 0 else ("🟡 Amarillo" if findings < 5 else "🔴 Rojo")
    print(f"\n## Resumen: {status}  ({findings} hallazgos estructurales; {len(sin_extraer)} sin extraer, {len(sin_citar)} sin citar)")

    if args.strict and (findings or sin_extraer or sin_citar):
        sys.exit(1)


if __name__ == "__main__":
    main()
