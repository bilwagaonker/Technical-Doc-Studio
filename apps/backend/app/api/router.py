from fastapi import APIRouter, File, UploadFile, HTTPException

from app.services.upload_service import UploadService
from app.services.video_service import VideoService
import traceback

router = APIRouter()

upload_service = UploadService()
video_service = VideoService()


@router.get("/")
async def health():

    return {
        "status": "running",
        "service": "AI Technical Documentation Studio"
    }


@router.post("/upload")
async def upload_video(

    file: UploadFile = File(...)

):

    try:

        video_path = upload_service.save(file)

        result = video_service.process_video(
            video_path
        )

        return {

            "success": True,

            "message": "Documentation generated successfully.",

            "result": result

        }

    except Exception as ex:
        
        traceback.print_exc()
        
        raise HTTPException(

            status_code=500,

            detail=str(ex)

        )