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
├── tools/             ← utilidades. `extract_pdfs.py` convierte row/*.pdf → extracted/*.txt.
                       `lint.py` chequea salud del wiki (huérfanos, enlaces, cobertura).
├── row/               ← CAPA 3: archivos BRUTOS del usuario (PDF). NO se modifican jamás.
│   ├── README.md      ← tabla de estado de ingesta (✅ ingerido / ⏳ pendiente).
│   ├── _inbox/        ← bandeja de PENDIENTES (aún sin ingerir).
│   ├── Estados Financieros - Sodimac Chile/   ← EF anuales y trimestrales (CLP, NIIF).
│   ├── Memoria Anual - Sodimac Chile/         ← memorias integradas.
│   └── Grupo Falabella/                        ← memorias, EF y plan de inversiones del grupo.
├── extracted/         ← texto derivado de los PDF (apoyo de lectura del agente). NO es fuente.
└── wiki/              ← CAPA 2: propiedad de la IA. Aquí crea/actualiza/mantiene.
    ├── index.md       ← índice maestro (tipo "índice de libro").
    ├── log.md         ← registro cronológico de todo lo ingerido/cambiado.
    ├── empresa/       ← entidades: Sodimac Chile, Grupo Falabella, marcas/formatos, gobierno corporativo.
    ├── finanzas/      ← P&L, balance, deuda, flujo de caja, capex/inversiones (por entidad).
    ├── series/        ← tablas de tiempo (ingresos, EBITDA, márgenes, SSS, inventario) trimestre/año.
    ├── kpis/          ← KPIs de retail y de FP&A (SSS, rotación, productividad m², días CxC/CxP, GMROI).
    ├── industria/     ← sector construcción Chile, mercado home improvement LatAm, peers, ciclo.
    ├── fpna/          ← procesos/checklists de FP&A: presupuesto, forecast, cierre, variance, reporting.
    ├── conceptos/     ← conceptos transversales (EBITDA, NIIF, alcance entidad vs segmento, leverage).
    ├── sintesis/      ← visión ejecutiva que se actualiza en cada ingesta.
    └── fuentes/       ← una ficha por documento bruto ingerido (metadata + qué aporta).
```

### 2.1 Flujo de lectura de PDF (obligatorio)
- El agente **no lee el binario del PDF**. Antes de ingerir, corre `python tools/extract_pdfs.py`
  (o `--only "<nombre>"`) para generar el texto en `extracted/<misma ruta>.txt`.
- Lee el `.txt` de `extracted/` para sintetizar, pero **cita siempre el PDF de `row/`**
  con su página: `[Fuente: EF-Junio-2025.pdf · p.7 · 2025]`.
- `extracted/` es **derivado**: nunca es fuente, no se cita como tal, y se puede regenerar.

### 2.2 Entidades del corpus (fijar perímetro SIEMPRE)
- **Sodimac S.A. (Chile)** — entidad legal + filiales, CLP, NIIF (EF y memorias Sodimac). Foco del rol FP&A.
- **Grupo Falabella (LatAm)** — consolidado del grupo, US$/CLP según documento; Sodimac como engine.
- No mezclar monedas ni perímetros. Ver `conceptos/alcance-sodimac-sa-vs-segmento`.

## 3. Reglas de trabajo (obligatorias)

### 3.1 Fuentes y trazabilidad
- **Prioriza SIEMPRE los archivos de `row/`.** Toda afirmación factual (cifras, fechas, hechos de la empresa) debe salir de un documento bruto y llevar **cita**: `[Fuente: <archivo> · <página/sección> · <año>]`.
- **Los archivos de `row/` no se mueven una vez citados** (las rutas de las citas son estables). Los documentos pendientes viven en `row/_inbox/`; al ingerirlos, muévelos a la raíz de `row/` y actualiza la tabla de estado en `row/README.md`.
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
3. **Archiva las respuestas valiosas como "query pages".** Si una pregunta produce una
   comparación, un análisis, un bridge o una conexión nueva, créala como página en la
   carpeta que corresponda (normalmente `wiki/sintesis/` o `wiki/fpna/`), con frontmatter
   `tipo: analisis`, citas a `row/`, y enlázala desde las páginas relacionadas y el `index.md`.
   Así el conocimiento **se acumula** en lugar de perderse en el chat (principio central del patrón).

**Lint** (chequeo de salud — correr periódicamente y tras cada ola):
- Ejecuta **`python tools/lint.py`** (o `--strict` para exit code 1 si hay hallazgos).
  Reporta: huérfanos, enlaces rotos, frontmatter incompleto, `estado` != verificado y
  cobertura PDF (row → extracted → citado en wiki).
- Complementa con revisión cualitativa: contradicciones entre páginas, afirmaciones
  obsoletas superadas por fuentes nuevas, conceptos mencionados sin página propia, vacíos de datos.
- **No borres archivos** ni crees páginas de contenido unilateralmente: reporta y
  propón. Corrige solo metadata (frontmatter) cuando el valor sea inequívoco.
- Registra cada pasada de lint en `log.md` (`## [fecha] lint | <resumen>`).

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
tipo: entidad | concepto | kpi | proceso | caso | fuente | checklist | sintesis | serie | analisis
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
