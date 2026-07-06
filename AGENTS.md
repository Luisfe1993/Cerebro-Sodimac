# AGENTS.md — Cerebro Sodimac (FP&A)

Este proyecto usa el patrón **LLM Wiki de Andrej Karpathy** (segundo cerebro).

**El schema canónico y todas las reglas de trabajo están en [`CLAUDE.md`](CLAUDE.md).**
Léelo y síguelo al pie de la letra antes de tocar nada. Aplica igual seas
GitHub Copilot (VS Code), Claude Code, Codex u otro agente.

## Resumen operativo (detalle completo en CLAUDE.md)
- **`row/`** = fuentes brutas del usuario. **Inmutables**: solo se leen, nunca se editan.
- **`wiki/`** = propiedad del agente. Aquí creas/actualizas páginas interconectadas,
  con `index.md` (catálogo) y `log.md` (registro cronológico).
- **Operaciones:** Ingest (procesar una fuente), Query (responder con citas y archivar
  la respuesta como página), Lint (chequeo de salud).
- **Reglas clave:** prioriza siempre `row/`; toda cifra lleva cita; nunca inventes
  datos financieros; ingesta progresiva (pocas fuentes por sesión); actualiza
  `index.md` y `log.md` en cada cambio.

## Cómo trabajar desde este chat (VS Code)
1. Abre la carpeta `cerebro-sodimac` como workspace en VS Code.
2. Pídeme en el chat: *"Lee CLAUDE.md e ingiere las fuentes nuevas de row/"* o
   *"Responde esta pregunta contra el wiki con citas"*.
3. Yo aplico los cambios directamente en los archivos Markdown.
