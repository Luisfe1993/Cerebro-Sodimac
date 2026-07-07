# row/ — Archivos BRUTOS (Capa 3)

Esta carpeta es **tuya**. La IA **no** modifica nada aquí; solo lee para sintetizar
la wiki. Deja aquí los documentos originales (PDF, Word, Excel, etc.).

> **Los archivos no se mueven una vez ingeridos.** Las citas del wiki apuntan a rutas
> fijas (`row/archivo`), así que reubicar un archivo rompe la trazabilidad. El estado
> "consumido vs pendiente" se lleva en esta tabla, en `wiki/log.md` y en `wiki/fuentes/`.

## Convención: PDF original + extracción `.md`

Cada fuente ideal tiene **dos artefactos** con el mismo nombre base:
- El **PDF original** — fuente de la verdad (permite re-verificar cualquier cifra).
- La **extracción `.md`** — texto legible que el agente lee y cita rápido.

> El agente cita la `.md`; el PDF respalda la trazabilidad. Si solo existe la `.md`
> (p. ej. porque el documento llegó como texto adjunto en el chat), guarda también
> el PDF original aquí para dejarlo completo.

## Estado de ingesta

Corpus real cargado por el usuario (2026-07-07). Ingesta **progresiva por olas**.

| Documento | Carpeta | Extraído | Ingerido |
|---|---|---|---|
| EF-Diciembre-2025.pdf | Estados Financieros - Sodimac Chile | ✅ | ✅ Ola 1 |
| EF-Junio-2025.pdf | Estados Financieros - Sodimac Chile | ✅ | ✅ Ola 1 |
| Memoria-Sodimac-2025.pdf | Memoria Anual - Sodimac Chile | ✅ | ✅ Ola 1 |
| EF-Marzo-2025 / Septiembre-2025 / Marzo-2026 | Estados Financieros - Sodimac Chile | ✅ | ✅ Ola 2 |
| EF-Dic 2021/2022/2023/2024 | Estados Financieros - Sodimac Chile | ✅ | ✅ Ola 2 |
| Memoria Sodimac 2022/2023/2024 | Memoria Anual - Sodimac Chile | ⏳ | ⏳ Ola 2b |
| Memorias Falabella 2021/2022/2023/2025 | Grupo Falabella | ⏳ | ⏳ Ola 3 |
| EF Grupo Falabella (FSA 2025, mar/jun/sep-25, mar-26) | Grupo Falabella/Estados Financieros | ⏳ | ⏳ Ola 3 |
| Plan-Inversiones-2026.pdf | Grupo Falabella | ⏳ | ⏳ Ola 3 |
| Estatutos-refundidos-2026.pdf | (raíz row) | ⏳ | ⏳ Ola 4 |

> ✅ hecho · ⏳ pendiente. Los documentos **nuevos** van a la bandeja [`_inbox/`](_inbox/);
> se extraen con `python tools/extract_pdfs.py` y se ingieren por olas.
> Nota: los `.md` `sodimac-press-release-2Q2025` y `falabella-corporate-presentation-1Q2026`
> son extracciones de chat de la fase piloto anterior (wiki archivado en `wiki/_archive_piloto/`).

## Qué documentos conseguir para el cerebro de Sodimac (FP&A)

Sodimac es parte del **grupo Falabella**, así que gran parte de la información
financiera oficial se reporta a nivel de Falabella S.A. y ante la **CMF (Chile)**.

### Prioridad alta (fuentes primarias)
- [ ] **Memorias Anuales de Falabella S.A.** (últimos 3-5 años) — incluyen el segmento de mejoramiento del hogar (Sodimac).
- [ ] **Estados Financieros consolidados** de Falabella (CMF Chile / IR).
- [ ] **Presentaciones de resultados trimestrales** (earnings) y sus notas.
- [ ] **Reportes de sostenibilidad / integrados** de Sodimac o Falabella.
- [ ] **Reportes 20-F / memoria** si aplica, o presentaciones a inversionistas (Investor Day).

### Prioridad media (contexto)
- [ ] Informes de la **industria de retail / home improvement** en LatAm.
- [ ] Reportes de **peers** comparables (Home Depot, Lowe's) para benchmarking de KPIs y márgenes.
- [ ] Notas de analistas / research sobre Falabella-Sodimac.
- [ ] Información pública del negocio: formatos de tienda, geografía, líneas de producto.

### Prioridad baja (enriquecimiento)
- [ ] Artículos de prensa relevantes (puedes usar la extensión web clipper para añadirlos).
- [ ] Glosarios de FP&A / retail que quieras estandarizar.

## Recomendación de flujo
1. Deja los documentos nuevos en [`_inbox/`](_inbox/) (bandeja de pendientes).
2. Pídeme que los ingiera; construyo/actualizo la wiki (modo progresivo, pocos por sesión).
3. Al terminar, el archivo pasa a la raíz de `row/` y lo marco ✅ en la tabla de arriba.

> Nota de fuentes: cuando descargues documentos oficiales, hazlo desde los sitios de
> Relación con Inversionistas de Falabella y desde la CMF. Renombra los archivos de
> forma clara, p. ej. `sodimac-press-release-1Q2025.pdf`.
