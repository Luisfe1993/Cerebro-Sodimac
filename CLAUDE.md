# CLAUDE.md — Cerebro Sodimac (FP&A)

> **Schema del wiki** (capa 3 del patrón LLM Wiki de Andrej Karpathy).
> Define **cómo cualquier agente de IA debe trabajar dentro de esta carpeta**.
> Este es el archivo canónico; `AGENTS.md` (para VS Code / Copilot / Codex) apunta aquí.
>
> Idea central: en vez de releer los documentos brutos en cada conversación (RAG),
> el agente **construye y mantiene una wiki persistente e interconectada** que se
> compone capa sobre capa. El conocimiento se compila una vez y se mantiene al día,
> no se vuelve a derivar en cada pregunta. Tú curas las fuentes y haces las preguntas;
> el agente hace todo el trabajo pesado (resumir, cruzar referencias, archivar, registrar).
>
> "Obsidian es el IDE; el LLM es el programador; el wiki es el código." — Karpathy

---

## 1. Contexto del propietario

- **Quién soy:** Analista preparándome para un cargo de **FP&A (Financial Planning & Analysis)** en **Sodimac**.
- **Objetivo del cerebro:** Convertirme en experto en Sodimac — su negocio, su industria (retail de mejoramiento del hogar / home improvement), sus finanzas, sus KPIs y los procesos de FP&A — para llegar al cargo con contexto profundo y trazable.
- **Sodimac en una línea:** Retailer de mejoramiento del hogar y construcción del **grupo Falabella** (Chile y otros países de LatAm). Formatos: tiendas Sodimac, Homecenter, Constructor, Imperial, etc.
- **Enfoque analítico:** pensamiento de segundo orden, foco en drivers de negocio, unit economics de retail, comparativa vs. peers (Home Depot, Lowe's, Falabella retail), y siempre atado a datos verificables.

## 2. Arquitectura de carpetas (3 capas)

```
cerebro-sodimac/
├── CLAUDE.md          ← este archivo (reglas). NO es contenido de la wiki.
├── row/               ← CAPA 3: archivos BRUTOS del usuario. NO se modifican jamás.
└── wiki/              ← CAPA 2: propiedad de la IA. Aquí crea/actualiza/mantiene.
    ├── index.md       ← índice maestro (tipo "índice de libro").
    ├── log.md         ← registro cronológico de todo lo ingerido/cambiado.
    ├── empresa/       ← páginas sobre Sodimac (modelo de negocio, formatos, geografía, grupo Falabella).
    ├── industria/     ← retail de mejoramiento del hogar, mercado LatAm, peers, ciclo del sector.
    ├── finanzas/      ← estados financieros, márgenes, capital, deuda, drivers financieros.
    ├── kpis/          ← KPIs de retail y de FP&A (SSS, ticket, tráfico, GMROI, etc.).
    ├── fpna/          ← procesos de FP&A: presupuesto, forecast, cierre, variance analysis, reporting.
    ├── conceptos/     ← conceptos transversales de finanzas/contabilidad citados en las fuentes.
    ├── checklists/    ← checklists accionables (análisis de resultados, red flags, etc.).
    └── fuentes/       ← una ficha por documento bruto ingerido (metadata + qué aporta).
```

## 3. Reglas de trabajo (obligatorias)

### 3.1 Fuentes y trazabilidad
- **Prioriza SIEMPRE los archivos de `row/`.** Toda afirmación factual (cifras, fechas, hechos de la empresa) debe salir de un documento bruto y llevar **cita**: `[Fuente: <archivo> · <página/sección> · <año>]`.
- Si un dato **no** está en `row/`, puedes usar conocimiento general SOLO si lo marcas explícitamente como `> [!note] Conocimiento externo — validar contra fuente` y nunca lo presentas como cifra oficial de Sodimac.
- **Nunca inventes cifras financieras.** Si falta el dato, dilo y regístralo como pendiente en el `log.md`.

### 3.2 Idioma y estilo
- Wiki en **español** (Sodimac/Falabella operan en LatAm). Términos técnicos financieros pueden quedar en inglés cuando sea el estándar (p. ej. *same-store sales*, *forecast*, *variance*).
- Páginas concisas, accionables y **muy interconectadas** con enlaces Markdown `[[wikilink]]` (compatibles con Obsidian) o `[texto](ruta.md)`.
- Cada página: título, resumen de 2-3 líneas, cuerpo, "Relacionado" (links), y "Fuentes".

### 3.3 Interconexión (grafo de conocimiento)
- Cada concepto/página debe enlazar a los conceptos con los que se relaciona, para que el grafo de Obsidian muestre el "cerebro".
- Cuando ingieras un documento nuevo, actualiza los enlaces cruzados de las páginas afectadas.

### 3.4 Mantenimiento de `index.md` y `log.md`
- Tras cada cambio: **actualiza `index.md`** (añade la página nueva con su link + resumen de una línea) y **añade una entrada a `log.md`** (fecha, qué se ingirió/creó/cambió).
- El `log.md` es cronológico y append-only (no borres historial).

### 3.5 Modo de ingesta (progresivo)
- **No proceses todo de golpe.** Trabaja en modo piloto/progresivo: pocas fuentes por sesión.
- Antes de una ingesta grande, **pregúntame** por alcance, prioridad y dudas.
- Detecta y reporta **contradicciones** entre fuentes (p. ej. cifras que no cuadran entre años) en lugar de resolverlas silenciosamente.

### 3.6 Confianza de las páginas (query-time trust)
- Cada página lleva en su frontmatter YAML un campo `estado:` con uno de:
  `borrador` · `verificado` · `obsoleto`.
- Las páginas **semilla** (creadas sin fuente bruta) van como `borrador` y deben
  reescribirse con datos citados cuando llegue la fuente real.
- Objetivo: que a query-time el agente pueda **confiar** en las páginas `verificado`
  sin releer el documento bruto (ese es el ahorro de tokens del patrón).

## 3.7 Operaciones (Ingest · Query · Lint)

**Ingest** (al añadir una fuente a `row/`):
1. Lee la fuente y comenta conmigo los puntos clave.
2. Crea una **ficha de fuente** en `wiki/fuentes/`.
3. Crea/actualiza las páginas de entidad y concepto afectadas (una fuente puede
   tocar 10-15 páginas). **Fusiona**, no dupliques.
4. Actualiza `index.md` y añade una entrada a `log.md`.

**Query** (al hacer una pregunta contra el wiki):
1. Lee primero `index.md`, localiza páginas relevantes y entra a ellas.
2. Responde **con citas**.
3. Si la respuesta es valiosa (una comparación, un análisis, una conexión nueva),
   **archívala como página nueva** en el wiki para que el conocimiento se acumule
   y no se pierda en el chat.

**Lint** (chequeo de salud periódico, cuando yo lo pida):
- Busca: contradicciones entre páginas, afirmaciones obsoletas superadas por fuentes
  nuevas, páginas huérfanas (sin enlaces entrantes), conceptos mencionados sin página
  propia, referencias cruzadas faltantes, vacíos de datos.
- **No borres archivos** ni crees páginas de contenido unilateralmente: reporta y
  propón. Corrige solo metadata (frontmatter) cuando el valor sea inequívoco.
- Registra el lint en `log.md`.

## 4. Áreas prioritarias a optimizar (para mi rol de FP&A)

1. **Modelo de negocio y drivers** de Sodimac (qué mueve ventas y márgenes).
2. **Estructura financiera**: P&L, márgenes, capital de trabajo, capex, deuda.
3. **KPIs de retail y FP&A**: same-store sales, ticket promedio, tráfico, m² de sala, GMROI, inventario, rotación.
4. **Procesos de FP&A**: ciclo presupuestario, forecasting, cierre mensual, análisis de variaciones, reporting a la gerencia.
5. **Industria y peers**: dinámica del sector home improvement, comparables (Home Depot, Lowe's), grupo Falabella.
6. **Conceptos contables/financieros** relevantes citados en las fuentes.

## 5. Convenciones de archivos

### 5.1 Frontmatter YAML (en cada página del wiki)
```yaml
---
tipo: entidad | concepto | kpi | proceso | caso | fuente | checklist | sintesis
titulo: <título>
descripcion: <resumen de una línea>
tags: [<tag1>, <tag2>]
fecha: YYYY-MM-DD
estado: borrador | verificado | obsoleto
fuentes: [<archivo-en-row-o-ficha-de-fuente>]
---
```

### 5.2 `index.md` (orientado a contenido)
Catálogo de TODO el wiki: cada página con su link + resumen de una línea, agrupado
por categoría. El agente lo lee primero al responder y lo actualiza en cada ingest.

### 5.3 `log.md` (cronológico, append-only)
Cada entrada empieza con un prefijo consistente para poder filtrar con herramientas:
```
## [YYYY-MM-DD] ingest | <título de la fuente>
## [YYYY-MM-DD] query  | <pregunta>
## [YYYY-MM-DD] lint   | <resumen>
```

## 6. Al empezar cada sesión
1. Lee primero `wiki/index.md` y `wiki/log.md` para saber qué existe.
2. Busca las páginas relevantes antes de crear nuevas (evita duplicados).
3. Si vas a ingerir de `row/`, confirma conmigo el alcance.
