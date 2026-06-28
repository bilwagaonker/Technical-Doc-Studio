from pathlib import Path
import cv2

class MetadataService:

    @staticmethod
    def extract(video_path: str):

        capture = cv2.VideoCapture(video_path)

        fps = capture.get(cv2.CAP_PROP_FPS)

        frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))

        width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))

        height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

        duration = frame_count / fps if fps else 0

        capture.release()

        return {
            "filename": Path(video_path).name,
            "fps": fps,
            "frameCount": frame_count,
            "duration": round(duration, 2),
            "resolution": f"{width}x{height}"
        }