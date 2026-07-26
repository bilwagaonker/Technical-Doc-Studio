# 🏗 System Architecture

## Overview

AI Technical Documentation Studio converts SAP demonstration videos into structured technical documentation using a fully automated AI pipeline.

The application combines Computer Vision, OCR, Speech Recognition, Retrieval Augmented Generation (RAG), and Large Language Models to generate:

- Technical Documentation
- Business Process Procedures (BPP)
- Quick Reference Guides (QRG)
- Markdown Documentation
- HTML Knowledge Articles

---

## High Level Architecture

```
                SAP Demo Video
                        │
                        ▼
              Video Processing Pipeline
                        │
     ┌──────────────────┼──────────────────┐
     ▼                  ▼                  ▼
 Frame Extraction      OCR            Speech-to-Text
     │                  │                  │
     └──────────────┬───┴──────────────────┘
                    ▼
             Step Builder Engine
                    │
                    ▼
            AI Documentation Engine
          (LLM + Knowledge Retrieval)
                    │
                    ▼
             Structured JSON Output
                    │
                    ▼
      DOCX | HTML | Markdown | PDF
```

---

## Backend

FastAPI

Main Services

- Metadata Service
- Frame Service
- OCR Service
- SAP Detection
- Whisper Service
- Documentation Service
- Export Service

---

## Frontend

Next.js

Components

- Upload Zone
- Processing Pipeline
- Output Downloads
- Recent Jobs

---

## AI Stack

Computer Vision

- OpenCV

OCR

- Tesseract OCR

Speech Recognition

- Whisper

Embeddings

- Sentence Transformers

Vector Database

- FAISS

LLM

- Ollama