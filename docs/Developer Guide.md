# 👨‍💻 Developer Guide

## Project Structure

```
apps/
    backend/
        app/
            api/
            services/
            storage/
            prompts/

    frontend/
        src/
            components/
            lib/
            app/
```

---

## Backend Workflow

```
Upload Video
        ↓
Extract Metadata
        ↓
Extract Frames
        ↓
Filter Duplicate Frames
        ↓
OCR
        ↓
SAP Detection
        ↓
Speech Recognition
        ↓
Build Steps
        ↓
Generate Documentation
        ↓
Export Files
```

---

## Important Services

### pipeline.py

Main orchestration layer.

### frame_service.py

Extracts meaningful SAP screenshots.

### scene_service.py

Removes duplicate screens.

### ocr_service.py

Extracts screen text.

### whisper_service.py

Generates transcript.

### documentation_service.py

Builds procedural steps using AI.

### export_service.py

Exports DOCX, HTML and Markdown.

---

## Running Locally

Backend

```bash
cd apps/backend

uvicorn app.main:app --reload
```

Frontend

```bash
cd apps/frontend

npm install

npm run dev
```

---

## Folder Outputs

```
storage/

frames/

output/

uploads/
```
