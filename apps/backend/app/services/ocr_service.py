from pathlib import Path
import cv2
import pytesseract


class OCRService:

    def __init__(self):

        pytesseract.pytesseract.tesseract_cmd = (
            r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        )

    ####################################################################
    # Process Extracted Frames
    ####################################################################

    def process_frames(self, frames):

        results = []

        for frame in frames:

            image = cv2.imread(frame["path"])

            if image is None:
                continue

            text = self.extract_text(image)

            results.append(

                {

                    "frame": frame["frame"],

                    "frameNumber": frame["frameNumber"],

                    "timestamp": frame["timestamp"],

                    "image": frame["image"],

                    "path": frame["path"],

                    "text": text

                }

            )

        print(f"OCR completed for {len(results)} frames")

        return results

    ####################################################################
    # OCR
    ####################################################################

    def extract_text(self, image):

        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )

        gray = cv2.threshold(

            gray,

            0,

            255,

            cv2.THRESH_BINARY + cv2.THRESH_OTSU

        )[1]

        text = pytesseract.image_to_string(

            gray,

            config="--oem 3 --psm 6"

        )

        return self.clean_text(text)

    ####################################################################
    # Cleanup
    ####################################################################

    def clean_text(self, text):

        lines = []

        for line in text.splitlines():

            line = line.strip()

            if len(line) < 2:
                continue

            # Ignore OCR garbage
            if len(line.split()) == 1 and len(line) <= 3:
                continue

            lines.append(line)

        return "\n".join(lines)