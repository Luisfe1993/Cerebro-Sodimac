# Log — Cerebro Sodimac (FP&A)

> Registro cronológico (append-only) de todo lo ingerido, creado o modificado.
> No borrar historial. Entrada más reciente arriba.

---

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
