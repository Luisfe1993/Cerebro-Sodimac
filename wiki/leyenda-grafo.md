---
tipo: meta
type: note
titulo: Leyenda de colores del grafo (Foam)
descripcion: Código de colores de los nodos del grafo de Foam por categoría (carpeta).
tags: [meta, foam, grafo, leyenda]
fecha: 2026-07-08
estado: verificado
fuentes: [.vscode/settings.json]
---

# Leyenda de colores del grafo (Foam)

**Resumen:** Los nodos del grafo de Foam se colorean por **categoría** (según la carpeta
de la página), usando el campo `type:` del frontmatter. Los colores se definen en
[`.vscode/settings.json`](../.vscode/settings.json) → `foam.graph.style.node`.

## Código de colores

| Color | Categoría (`type`) | Carpeta | Qué agrupa |
|---|---|---|---|
| <span style="color:#4c9aff">■</span> Azul | `empresa` | `empresa/` | Entidades: Sodimac Chile, Grupo Falabella, marcas, estrategia, gobierno |
| <span style="color:#2ecc71">■</span> Verde | `finanzas` | `finanzas/` | P&L, balance, flujo de caja, plan de inversiones |
| <span style="color:#1abc9c">■</span> Turquesa | `series` | `series/` | Tablas de tiempo (ingresos, márgenes, operativo) |
| <span style="color:#e67e22">■</span> Naranja | `kpis` | `kpis/` | Indicadores de retail y FP&A |
| <span style="color:#e74c3c">■</span> Rojo | `fpna` | `fpna/` | Procesos/checklists de FP&A |
| <span style="color:#9b59b6">■</span> Morado | `conceptos` | `conceptos/` | Conceptos transversales (EBITDA, alcance) |
| <span style="color:#f1c40f">■</span> Amarillo | `sintesis` | `sintesis/` | Visión ejecutiva (páginas vivas) |
| <span style="color:#95a5a6">■</span> Gris | `fuentes` | `fuentes/` | Fichas de documentos brutos ingeridos |
| <span style="color:#c9a227">■</span> Dorado | `note` (default) | (raíz / sin `type`) | `index`, `log`, esta leyenda y notas sin categoría |

## Cómo funciona
- Cada página lleva `type: <categoría>` en su frontmatter; Foam mapea ese valor al color.
- Para cambiar un color, edita el hex en [`.vscode/settings.json`](../.vscode/settings.json)
  y reabre el grafo (`Ctrl+Shift+P` → `Foam: Show Graph`).
- Nodos **grises huecos** (no de esta tabla) = *placeholders*: páginas referenciadas que
  aún no existen.

## Relacionado
- [Índice maestro](index.md)
- [Log del cerebro](log.md)
