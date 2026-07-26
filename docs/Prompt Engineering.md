 # 🤖 Prompt Engineering

The Documentation Service uses prompt engineering to convert OCR and transcript data into structured SAP documentation.

---

## Input

- OCR Text
- Speech Transcript
- SAP Screen Detection
- Knowledge Base Retrieval

---

## Prompt Goals

Generate:

- Title
- Purpose
- Step Number
- Step Description
- Screenshot Mapping

---

## Output Format

```json
{
  "transaction": "",
  "title": "",
  "purpose": "",
  "steps": []
}
```

---

## Prompt Design Principles

- Ignore OCR noise
- Preserve SAP terminology
- Keep steps sequential
- One screenshot per step
- Do not hallucinate fields
- Generate concise documentation