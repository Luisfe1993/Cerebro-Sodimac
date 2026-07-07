---
tipo: fpna
titulo: Checklist — Análisis de resultados (Sodimac S.A.)
descripcion: Checklist accionable de FP&A para analizar los resultados trimestrales/anuales de Sodimac S.A., anclado a sus cuentas reales.
tags: [fpna, checklist, analisis, sodimac-sa]
fecha: 2026-07-07
estado: verificado
fuentes: [row/Estados Financieros - Sodimac Chile/EF-Diciembre-2025.pdf, row/Estados Financieros - Sodimac Chile/EF-Septiembre-2025.pdf]
---

# Checklist — Análisis de resultados (Sodimac S.A.)

> Guía práctica para revisar un cierre trimestral/anual de **Sodimac S.A. (Chile)**. Ordenada de
> arriba (ingresos) a abajo (caja), con las cuentas reales, los ratios a calcular y las alertas
> propias del negocio. Marca cada punto al completarlo.

## 0. Setup (antes de mirar cifras)
- [ ] **Fija el perímetro**: Sodimac S.A. (Chile, CLP, NIIF), no el segmento Sodimac LatAm de Falabella. Ver [Alcance](../conceptos/alcance-sodimac-sa-vs-grupo.md).
- [ ] **Confirma el periodo**: los EF intermedios son **acumulados (YTD)**; para el trimestre aislado, resta el corte anterior.
- [ ] **Unidades**: el balance viene en **M$ (miles)**; reexpresa en MM$ para comparar con el P&L.
- [ ] Ten a mano la **columna comparativa** (año/periodo previo) y el corte anterior para el YTD.

## 1. Ingresos (crecimiento)
- [ ] **Ingresos de actividades ordinarias**: Δ YoY y Δ vs presupuesto/forecast.
- [ ] Descompón: **SSS** (orgánico) vs expansión (sin crecimiento de m² en Sodimac, casi todo es SSS) vs omnicanal.
- [ ] Cruza con [Serie anual 2021-2025](../series/ingresos-y-resultado-anual.md) y [Evolución 2025 YTD](../series/evolucion-2025-ytd.md): ¿acelera o desacelera?
- [ ] **Cuidado con la base**: 2021 fue un pico atípico; evita leer variaciones contra bases excepcionales.
- [ ] Estacionalidad: 1T ≈ 26% del año, 1S ≈ 51% (referencia 2025).

## 2. Márgenes
- [ ] **Margen bruto** (Ganancia bruta / Ingresos): rango normal ~28-30%. Explica desviaciones (mix, costo de venta, tipo de cambio de importados, promociones).
- [ ] **Margen operativo** (proxy): Ganancia bruta − costos de distribución − gastos de administración.
- [ ] Alerta: costos de distribución creciendo más rápido que ventas (en 2025 subieron +20,2%).

## 3. Gastos (GAV)
- [ ] **Gastos de administración** como % de ingresos (2025: ~25,4%). ¿Apalancamiento operativo (crece < ventas) o desapalancamiento?
- [ ] Revisa los drivers citados por la compañía: costo logístico, remuneraciones, comisiones, publicidad/promoción.

## 4. Resultado no operacional (donde se juega la última línea)
- [ ] **Costos financieros**: nivel y Δ (2025: MM$48.539, +11,5%). Relaciónalo con la deuda del balance.
- [ ] **Diferencias de cambio y reajustes**: pueden mover el resultado (2025: +4.763 FX; -1.478 reajustes).
- [ ] **Intereses con relacionadas (Falabella)**: revisa el efecto de la deuda intercompañía.
- [ ] Recuerda: el **margen neto es delgado (~0,45%)** → estas partidas deciden si hay utilidad o pérdida.

## 5. Balance y capital de trabajo
- [ ] **Inventarios** y **rotación** (costo de ventas / inventario; 2025 ≈ 4,36× ≈ 84 días). ¿Sube el inventario más que las ventas? (señal de capital de trabajo atado).
- [ ] **Arrendamientos IFRS 16** (mayor pasivo, ~MM$762.508): su servicio no aparece en el resultado operacional pero sí drena caja.
- [ ] **Cuentas por pagar a Falabella** (~MM$268.177): vigila variaciones y condiciones intercompañía.
- [ ] **Patrimonio**: ¿por qué cambia? Recuerda que el **OCI** (pérdidas actuariales, coberturas) y dividendos pueden reducirlo aunque haya utilidad.

## 6. Flujo de caja
- [ ] **FCO** y su Δ (2025: MM$123.698, -22% YoY): ¿la utilidad se convierte en caja o se queda en capital de trabajo?
- [ ] **Capex** (2025: MM$33.343) vs depreciación: ¿inversión de mantención o de crecimiento?
- [ ] **Pago de arrendamientos** (MM$100.244): réstalo para ver la caja realmente disponible.
- [ ] **Financiamiento con relacionadas**: ¿fuente o uso de caja en el periodo?

## 7. Red flags específicos de Sodimac
- [ ] Ingreso creciendo pero **margen bruto cayendo** (promociones/mix agresivo).
- [ ] **Inventario subiendo > ventas** (riesgo de obsolescencia y menor FCO).
- [ ] **Costos financieros / no operacional** comiéndose la mejora operativa.
- [ ] **Patrimonio erosionándose** pese a utilidad (OCI/dividendos).
- [ ] Desaceleración de ingresos contra base fácil (ojo con 2026 tras el rebote de 2024-2025).

## 8. Entregable (narrativa de gerencia)
- [ ] **Bridge** del resultado: precio/volumen/mix, márgenes, gastos, no operacional.
- [ ] 3-5 **bullets ejecutivos** con el "qué pasó y por qué".
- [ ] **Actualiza el forecast** si la desviación cambia la visión del año.
- [ ] Archiva el análisis como página nueva y actualiza [la síntesis ejecutiva](../sintesis/vision-ejecutiva-sodimac.md).

## Relacionado
- [Estado de resultados — Sodimac 2025](../finanzas/estado-resultados-sodimac-2025.md)
- [Balance — Sodimac 2025](../finanzas/balance-sodimac-2025.md)
- [Flujo de caja — Sodimac 2025](../finanzas/flujo-de-caja-sodimac-2025.md)
- [Indicadores operativos 2025](../kpis/indicadores-operativos-2025.md)
- [Serie anual 2021-2025](../series/ingresos-y-resultado-anual.md)
