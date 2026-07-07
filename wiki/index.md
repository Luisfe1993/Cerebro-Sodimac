# Índice maestro — Cerebro Sodimac (FP&A)

> Índice tipo "índice de libro". El agente lo lee primero. Cada página con link + resumen de una línea.
> Reconstruido desde cero (Ola 0) sobre el corpus real de `row/`. El wiki piloto anterior está en `_archive_piloto/`.

## Estado
- **Corpus en `row/`:** ~24 PDF (EF y memorias de Sodimac Chile + Grupo Falabella + plan de inversiones + estatutos).
- **Fuentes ingeridas:** 9 EF Sodimac + 4 Memorias Sodimac + EF Falabella FSA 2025 + Plan Inversiones 2026 + presentación corporativa.
- **Páginas del wiki:** 20.
- **Última actualización:** 2026-07-07.

## Cómo usar este cerebro
1. Deja PDF nuevos en `row/_inbox/`.
2. Corre `python tools/extract_pdfs.py` para generar el texto en `extracted/`.
3. Pídeme que ingiera; construyo/actualizo el wiki citando el PDF por página.
4. Explora el grafo con Foam (`Foam: Show Graph`).

---

## Empresa
- [Sodimac Chile — entidad](empresa/sodimac-chile.md) — Perfil de Sodimac S.A.: 87 tiendas, 12.874 trabajadores, MM$2.555.786 ventas 2025. ✅
- [Grupo Falabella — ecosistema y engines](empresa/grupo-falabella.md) — Ingresos grupo MM$11.342.386; Sodimac = mayor engine (38% revenue). ✅

## Finanzas
- [Estado de resultados — Sodimac 2025](finanzas/estado-resultados-sodimac-2025.md) — P&L FY2025: ingresos +5,5%, ganancia MM$11.397 (×18 vs 2024). ✅
- [Balance — Sodimac 2025](finanzas/balance-sodimac-2025.md) — Activos MM$1.553.835; arrendamientos IFRS 16 (MM$762.508) e intercompañía Falabella dominan. ✅
- [Flujo de caja — Sodimac 2025](finanzas/flujo-de-caja-sodimac-2025.md) — FCO MM$123.698, capex MM$33.343, arrendamientos MM$100.244. ✅
- [Plan de inversiones del grupo 2026](finanzas/plan-inversiones-grupo-2026.md) — Capex grupo +40% a US$900M; Sodimac: reconversión Maestro→Sodimac y remodelaciones. ✅

## Series (tablas de tiempo)
- [Serie anual — Ingresos, márgenes y resultado 2021-2025](series/ingresos-y-resultado-anual.md) — Auge 2021 → pérdida 2023 → recuperación; ventas MM$3.256k→2.556k. ✅
- [Evolución 2025 YTD + Q1-2026](series/evolucion-2025-ytd.md) — Acumulados 3M/6M/9M/12M y arranque 2026 plano (+0,95%). ✅
- [Serie operativa anual 2022-2025](series/operativo-anual.md) — Tiendas, superficie, dotación (-16%) y productividad; venta/trabajador en máximo. ✅

## KPIs
- [Indicadores operativos — Sodimac 2025](kpis/indicadores-operativos-2025.md) — Venta/m², ticket medio, rotación de inventario (~4,36×), red y actividad. ✅

## FP&A
- [Checklist — Análisis de resultados](fpna/checklist-analisis-resultados.md) — Guía accionable trimestral/anual anclada a las cuentas reales de Sodimac. ✅

## Conceptos
- [Alcance: Sodimac S.A. vs Grupo Falabella](conceptos/alcance-sodimac-sa-vs-grupo.md) — Perímetro/moneda: entidad Chile (CLP) ≠ grupo LatAm (US$). ✅
- _(Ola 3b)_ EBITDA, SSS, marcas/formatos y estrategia — pendientes de re-ingesta desde fuentes reales (están en `_archive_piloto/`).

## Industria
- _(Ola 4)_ Sector construcción Chile, home improvement LatAm, peers.

## Síntesis
- [Visión ejecutiva — Sodimac S.A.](sintesis/vision-ejecutiva-sodimac.md) — Tesis en 5 líneas + números ancla FY2025 (página viva). ✅

## Fuentes
- [EF Sodimac Diciembre 2025](fuentes/ef-sodimac-diciembre-2025.md) — Estados financieros anuales auditados (M$, NIIF).
- [EF Sodimac Junio 2025](fuentes/ef-sodimac-junio-2025.md) — Estados intermedios 6M25 (no auditados).
- [Memoria Sodimac 2025](fuentes/memoria-sodimac-2025.md) — Memoria integrada (perfil operativo + sostenibilidad).
- [Serie histórica EF Sodimac Chile (2021-2026)](fuentes/ef-sodimac-serie-historica.md) — 9 EF anuales e intermedios para las series.
- [Serie de Memorias Sodimac Chile (2022-2025)](fuentes/memorias-sodimac-serie.md) — Memorias para la serie operativa.
- [EF Falabella FSA 2025](fuentes/ef-falabella-fsa-2025.md) — EF consolidados del grupo (CLP) + nota de segmentos.
- [Plan de Inversiones Falabella 2026](fuentes/plan-inversiones-falabella-2026.md) — Capex 2026 del grupo por negocio (US$).
- [Presentación corporativa Falabella 1Q26](fuentes/falabella-corporate-presentation-1Q2026.md) — Contexto del grupo en US$.

## Archivo
- `_archive_piloto/` — wiki de la fase piloto anterior (páginas hechas con 2 fuentes de chat; conserva SSS, EBITDA, marcas, estrategia para re-ingesta).

## Leyenda
✅ verificado con cita · ⚠️ borrador/pendiente de fuente
