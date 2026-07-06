# Copilot / VS Code — Instrucciones del proyecto

Este repositorio es un **LLM Wiki (segundo cerebro) de Karpathy** sobre **Sodimac**
para un rol de **FP&A**.

El schema completo y las reglas están en [`../CLAUDE.md`](../CLAUDE.md) (canónico) y
resumidas en [`../AGENTS.md`](../AGENTS.md). **Síguelos siempre.**

Reglas imprescindibles al asistir en este workspace:
- **No modifiques nunca** los archivos de `row/` (fuentes brutas inmutables).
- Solo el agente escribe en `wiki/`. Mantén páginas concisas e interconectadas.
- Toda afirmación factual (cifras, fechas) debe llevar **cita** a una fuente de `row/`.
  Si el dato no está en `row/`, no lo inventes: márcalo como pendiente en `wiki/log.md`.
- En cada cambio: actualiza `wiki/index.md` y añade una entrada a `wiki/log.md`.
- Ingesta **progresiva**: pocas fuentes por sesión; pregunta antes de ingestas grandes.
