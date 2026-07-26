<div align="center">

# 🤖 AI Technical Documentation Studio

### Transform SAP Demo Videos into Professional Documentation using AI

*An end-to-end AI-powered documentation engine that converts SAP process recordings into structured technical documents with screenshots, OCR, speech recognition and Large Language Models.*

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Next.js](https://img.shields.io/badge/Next.js-Frontend-black)
![Ollama](https://img.shields.io/badge/Ollama-LLM-orange)
![License](https://img.shields.io/badge/License-MIT-blue)

</div>

---

# 📖 Overview

Writing SAP documentation manually is repetitive, time-consuming, and often inconsistent.

AI Technical Documentation Studio automates the complete documentation process by analyzing SAP demonstration videos and generating professional technical documentation in multiple formats.

Instead of spending hours creating Reference Guides from scratch, the users can simply upload a video and let AI generate the documentation. Once its generated they can review the steps, edit the documentation, and take it through the human-in-the-loop approvals.

---

# ✨ Features

## 🎥 Video Understanding

- Upload SAP demo videos
- Automatic frame extraction
- Intelligent duplicate frame removal
- Screenshot selection

---

## 🖥 SAP Screen Analysis

- OCR using Tesseract
- SAP GUI detection
- Screen classification
- Field extraction

---

## 🎙 Speech Understanding

- Whisper speech recognition
- Timestamp extraction
- Audio transcription
- Speech-to-step conversion

---

## 🧠 AI Documentation Generation

- Step generation using LLM
- Human-readable instructions
- Purpose generation
- Automatic procedure creation
- Screenshot mapping

---

## 📄 Export Formats

- DOCX
- HTML
- Markdown
- PDF *(coming soon)*

---

# 🚀 System Architecture

```
                SAP Demo Video
                        │
                        ▼
              Metadata Extraction
                        │
                        ▼
              Frame Extraction
                        │
                        ▼
             Scene Change Detection
                        │
                        ▼
                  OCR Engine
                        │
                        ▼
             SAP UI Identification
                        │
                        ▼
              Speech Recognition
                        │
                        ▼
            AI Documentation Engine
                        │
                        ▼
        DOCX • HTML • Markdown • PDF
```

---

# 🏗 Technology Stack

## Frontend

- Next.js
- TypeScript
- TailwindCSS
- React Dropzone
- Lucide Icons

---

## Backend

- FastAPI
- Python
- OpenCV
- Tesseract OCR
- Whisper
- Ollama
- Sentence Transformers
- FAISS

---

## AI Models

| Component | Model |
|------------|--------------------------|
| OCR | Tesseract |
| Speech | Whisper |
| Embeddings | all-MiniLM-L6-v2 |
| LLM | Ollama |

---

# 📂 Project Structure

```
Technical-Doc-Studio

├── frontend
│
│   ├── src
│   ├── components
│   ├── app
│   └── lib
│
├── backend
│
│   ├── api
│   ├── services
│   ├── models
│   ├── storage
│   └── knowledge
│
└── docs
```

---

# ⚙ AI Processing Pipeline

The application processes every uploaded video through a modular AI pipeline.

```
Upload Video

        │

        ▼

Metadata Extraction

        │

        ▼

Frame Extraction

        │

        ▼

Scene Filtering

        │

        ▼

OCR Processing

        │

        ▼

SAP Detection

        │

        ▼

Speech Recognition

        │

        ▼

AI Documentation Generation

        │

        ▼

Export Documents
```

---

# 📸 Generated Outputs

The application automatically produces the technical documentation pertaining to the uploaded SAP system video.

Supported formats:

- DOCX
- HTML
- Markdown
- PDF (Upcoming)

## What does the frontend look like?

<img width="1152" height="648" alt="Frontend -edited" src="https://github.com/user-attachments/assets/c939c1ff-d418-4555-8e69-b122e93ed01e" />

## What does the backend look like?

https://github.com/user-attachments/assets/670bfe2c-1cbd-4308-b6a4-5ebc03870157

---

# 🎯 Current Capabilities

✅ Automatic frame extraction

✅ OCR processing

✅ Whisper transcription

✅ SAP screen detection

✅ Screenshot mapping

✅ AI-generated procedures

✅ Multi-format export

✅ Interactive frontend

---

# 🚧 Roadmap

- Intelligent screenshot selection (differentiate with systems and gain context)
- SAP field highlighting
- Navigation arrows
- Improve the wording ability alongside the running SAP screens.
- Export to PDF
- Interactive HTML documentation
- RAG-powered documentation
- AI reviewer agent
- Agentic workflow

---


# 📌 Future Vision

The long-term goal can be to evolve AI Technical Documentation Studio into a complete AI Documentation Platform capable of:

- Understanding SAP workflows
- Learning enterprise knowledge
- Building documentation autonomously
- Generating training content
- Maintaining documentation through AI agents

---

# 👩‍💻 Author

**Bilwa Gaonker**

Business Analyst who loves designing end-to-end solutions using ML and AI to improve process and efficiency!

*"Building AI that eliminates repetitive documentation work."*

---

⭐ If you like this project, consider giving it a star!
