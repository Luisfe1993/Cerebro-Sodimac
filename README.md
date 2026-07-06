# Cerebro Sodimac — LLM Wiki (FP&A)

Segundo cerebro construido con el patrón **LLM Wiki de Andrej Karpathy**
([gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)) para desarrollar
expertise en **Sodimac** (grupo Falabella) de cara a un rol de **FP&A**.

## Arquitectura (3 capas)
- **`row/`** — fuentes brutas del usuario. Inmutables: la IA solo lee, nunca modifica.
- **`wiki/`** — propiedad de la IA: páginas interconectadas + `index.md` + `log.md`.
- **`CLAUDE.md`** / **`AGENTS.md`** — schema: reglas de cómo la IA construye y mantiene el wiki.

## Cómo usarlo
1. Abre esta carpeta en **VS Code**. Instala la extensión recomendada **Foam** (visor de grafo, reemplaza a Obsidian).
2. Deja documentos oficiales (memorias, estados financieros, earnings) en `row/`.
3. Pide al agente (Copilot o Claude Code): *"Lee CLAUDE.md e ingiere las fuentes nuevas de row/ con citas"*.
4. Explora el grafo con `Foam: Show Graph`.

## Estado actual
- 2 fuentes ingeridas (Sodimac PR 2Q2025, Falabella Corp Presentation 1Q2026).
- 11 páginas en el wiki. Ver [`wiki/index.md`](wiki/index.md) y el historial en [`wiki/log.md`](wiki/log.md).

## Reglas clave
- Toda cifra lleva **cita** a una fuente de `row/`. No se inventan datos.
- Ingesta **progresiva** (pocas fuentes por sesión).
- Solo fuentes públicas (Falabella/CMF); no cargar material interno confidencial.
