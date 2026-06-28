from pathlib import Path
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

from app.services.metadata_service import MetadataService
from app.services.frame_service import FrameService
from app.services.index_service import IndexService
from app.services.ocr_service import OCRService
from app.services.sap_detector import SAPDetector



class VideoPipeline:

    @staticmethod
    def process(video_path: str):

        metadata = MetadataService.extract(video_path)
        ocr_service = OCRService()
        sap_detector = SAPDetector()
        
        frame_folder = (
            Path("app/storage/frames")
            / Path(video_path).stem
        )

        frames = FrameService.extract_frames(
            video_path,
            str(frame_folder)
        )
        
        ocr_results = ocr_service.process_folder(frame_folder)
        sap_results = []
        for result in ocr_results:
            image_path = frame_folder / result["image"]
            sap_result = sap_detector.process(image_path,result)
            sap_results.append(sap_result)
            
        index_path = (
            Path("app/storage/indexes")
            / f"{Path(video_path).stem}.json"
        )

        IndexService.save(
            sap_results,
            index_path
        )

        return {
            "metadata": metadata,
            "framesExtracted": len(sap_results),
            "frameFolder": str(frame_folder),
            "indexFile": str(index_path)
        }