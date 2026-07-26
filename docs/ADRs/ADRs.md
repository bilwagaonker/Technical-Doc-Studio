# 📐 Architecture Decision Records

*I have used all the open-source tools as much as possible so that I could learn and experiment the logic on my personal laptop as much as possible.*


## ADR-001

Use FastAPI instead of Flask.

Reason

- Better async support
- Automatic Swagger documentation
- Type validation

---

## ADR-002

Use Ollama instead of cloud LLM.

Reason

- Offline execution
- Zero API cost
- Better privacy

---

## ADR-003

Use FAISS.

Reason

- Lightweight
- Fast similarity search
- Local vector database

---

## ADR-004

Generate documentation as structured JSON first.

Reason

Separates AI generation from export rendering.

---

## ADR-005

Use OpenCV for screenshot extraction.

Reason

Reliable frame processing with minimal dependencies.