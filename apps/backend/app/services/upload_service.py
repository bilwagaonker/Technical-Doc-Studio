from pathlib import Path
import shutil
import uuid

class UploadService:

    ALLOWED_EXTENSIONS = {
        ".mp4",
        ".avi",
        ".mov",
        ".mkv"
    }

    def __init__(self):

        self.upload_folder = Path(
            "app/storage/uploads"
        )

        self.upload_folder.mkdir(
            parents=True,
            exist_ok=True
        )

    def save(self, upload_file):

        extension = Path(
            upload_file.filename
        ).suffix.lower()

        if extension not in self.ALLOWED_EXTENSIONS:

            raise ValueError(
                f"Unsupported video format: {extension}"
            )

        filename = (
            f"{uuid.uuid4().hex}{extension}"
        )

        destination = (
            self.upload_folder
            / filename
        )

        with destination.open("wb") as buffer:

            shutil.copyfileobj(
                upload_file.file,
                buffer
            )

        return destination