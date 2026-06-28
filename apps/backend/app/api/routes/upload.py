from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, UploadFile, File
from app.services.pipeline import VideoPipeline

router = APIRouter()

UPLOAD_FOLDER = Path("app/storage/uploads")
UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)


@router.post("/")
async def upload_video(
    file: UploadFile = File(...)
):

    file_id = uuid4().hex

    extension = Path(file.filename).suffix

    destination = UPLOAD_FOLDER / f"{file_id}{extension}"

    with open(destination, "wb") as buffer:
        buffer.write(await file.read())

    pipeline = VideoPipeline.process(
    str(destination)
    )

    return {
        "jobId": file_id,
        "status": "Completed",
        "pipeline": pipeline
    }