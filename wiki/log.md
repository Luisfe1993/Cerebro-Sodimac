# Log — Cerebro Sodimac (FP&A)

> Registro cronológico (append-only) de todo lo ingerido, creado o modificado.
> No borrar historial. Entrada más reciente arriba.

---

## [2026-07-07] build | Checklist de FP&A (análisis de resultados)
- Creada `fpna/checklist-analisis-resultados`: guía accionable de 8 bloques (setup, ingresos, márgenes, GAV, no operacional, balance/capital de trabajo, flujo de caja, red flags, entregable), anclada a las cuentas y ratios reales de Sodimac S.A.
- `index.md` actualizado (sección FP&A).

## [2026-07-07] ingest | Ola 2 — serie histórica EF Sodimac Chile (2021-2026)
- Extraídos e ingeridos 7 EF adicionales: anuales 2021, 2022, 2023, 2024 e intermedios mar-2025, sep-2025, mar-2026 (jun/dic-2025 ya estaban).
- Creadas 3 páginas: `series/ingresos-y-resultado-anual`, `series/evolucion-2025-ytd`, `fuentes/ef-sodimac-serie-historica`.
- Hallazgo clave: ventas pico 2021 (MM$3.255.724, utilidad MM$228.951) → caída a piso 2023 (MM$2.364.993, **pérdida MM$44.529**) → recuperación 2024-2025 (MM$2.555.786, utilidad MM$11.397). 1T-2026 casi plano (+0,95%).
- Patrimonio erosionado de MM$283.322 (2021) a MM$126.148 (2025).
- `index.md` y `sintesis/vision-ejecutiva` actualizados.

## [2026-07-07] ingest | Ola 1 (piloto) — EF dic-2025 + EF jun-2025 + Memoria Sodimac 2025
- Leídos y sintetizados los estados financieros anuales FY2025 (P&L, balance, patrimonio, flujo de caja) y datos operativos de la Memoria 2025.
- Creadas 10 páginas verificadas con cita:
  - fuentes: ef-sodimac-diciembre-2025, ef-sodimac-junio-2025, memoria-sodimac-2025.
  - empresa: sodimac-chile.
  - finanzas: estado-resultados-sodimac-2025, balance-sodimac-2025, flujo-de-caja-sodimac-2025.
  - kpis: indicadores-operativos-2025.
  - conceptos: alcance-sodimac-sa-vs-grupo.
  - sintesis: vision-ejecutiva-sodimac.
- Hallazgos ancla FY2025: ingresos MM$2.555.786 (+5,5%), ganancia MM$11.397 (×18 vs 2024), FCO MM$123.698, arrendamientos IFRS 16 MM$762.508, CxP Falabella MM$268.177.
- `index.md` actualizado. **Pendiente:** revisión del usuario antes de Ola 2 (serie trimestral).

## [2026-07-07] setup | Ola 0 — reseteo + corpus real + pipeline de extracción
- Usuario cargó ~24 PDF reales en `row/` (EF y memorias de Sodimac Chile + Grupo Falabella + plan inversiones + estatutos).
- Detectados y **eliminados** duplicados: carpeta "Memorias - Sodimac Colombia" era copia exacta (MD5) de las memorias de Chile.
- Creado `tools/extract_pdfs.py` (pdfplumber) → texto a `extracted/`. Validado: EF-Diciembre-2025 extrae P&L/balance con cifras (5/104 págs vacías = carta auditoría Deloitte, imágenes).
- Extraídos los 3 PDF del piloto (EF jun-2025, EF dic-2025, Memoria Sodimac 2025).
- **Wiki piloto archivado** en `wiki/_archive_piloto/` (11 páginas de la fase anterior con 2 fuentes de chat).
- `CLAUDE.md` actualizado: nueva taxonomía (empresa/finanzas/series/kpis/industria/fpna/conceptos/sintesis/fuentes), flujo de lectura PDF→extracted→cita, entidades del corpus.
- `index.md` reconstruido. Decisiones del usuario: extracción sí, reseteo sí, Colombia eliminada, alcance = Sodimac Chile **y** Grupo, piloto OK.
- **Siguiente:** Ola 1 — ingerir los 3 PDF del piloto y construir la base del wiki con citas.

## [2026-07-06] ingest | Sodimac PR 2Q2025 + Falabella Corp Presentation 1Q2026 (piloto)
- Ingeridas 2 fuentes brutas en `row/`:
  - `sodimac-press-release-2Q2025.md` (Sodimac S.A. Chile, CLP, NIIF).
  - `falabella-corporate-presentation-1Q2026.md` (grupo Falabella, US$).
- Creadas fichas de fuente en `wiki/fuentes/` (2).
- Creadas/actualizadas 11 páginas del wiki (todas `verificado` salvo `fpna/variance-analysis`):
  - empresa: sodimac-vision-general (actualizada), grupo-falabella, marcas-formatos, estrategia.
  - finanzas: estado-resultados-sodimac-sa, endeudamiento-balance-sodimac-sa.
  - kpis: same-store-sales (actualizada), indicadores-retail.
  - conceptos: alcance-sodimac-sa-vs-segmento, ebitda.
- Contradicción/nota de perímetro registrada: Sodimac S.A. (Chile, CLP) vs segmento Sodimac LatAm (US$) NO son homologables → página `conceptos/alcance-sodimac-sa-vs-segmento`.
- `index.md` actualizado. Configurado Foam (reemplazo de Obsidian) y `.vscode/`.
- **Pendiente:** ingerir más trimestres, memoria anual, y peers para benchmarking.

## [2026-07-06] setup | Alineación con el gist oficial de Karpathy + multi-agente
- Proyecto movido a `C:\Users\luissande\projects\cerebro-sodimac`.
- `CLAUDE.md` alineado 1:1 con el patrón oficial: operaciones Ingest/Query/Lint,
  frontmatter YAML con `estado`, convención de `index.md`/`log.md`, query-time trust.
- Añadidos `AGENTS.md` y `.github/copilot-instructions.md` para usar el cerebro
  **desde VS Code / Copilot** (este chat), no solo desde Claude Code.

## [2026-07-06] setup | Inicialización de la estructura
- Creada la arquitectura de 3 capas del patrón LLM Wiki (Karpathy).
- Creado `CLAUDE.md` con contexto (FP&A / Sodimac), reglas de fuentes y trazabilidad.
- Creado `row/README.md` con la lista de documentos brutos a conseguir (Falabella/CMF).
- Creado `wiki/index.md` y `wiki/log.md`.
- Creadas páginas **semilla** de ejemplo (marcadas para validar con fuentes reales):
  - `empresa/sodimac-vision-general.md`
  - `kpis/same-store-sales.md`
  - `fpna/variance-analysis.md`
- **Pendiente:** el usuario debe añadir documentos brutos en `row/` para la primera ingesta real.
