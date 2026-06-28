from pathlib import Path
import re

import cv2
import pytesseract


class OCRService:

    def __init__(self):

        pytesseract.pytesseract.tesseract_cmd = (
            r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        )

    def preprocess(self, image):

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        gray = cv2.GaussianBlur(gray, (3, 3), 0)

        gray = cv2.threshold(
            gray,
            0,
            255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU,
        )[1]

        return gray

    def clean_text(self, text):

        text = re.sub(r"\s+", " ", text)

        text = re.sub(r"[^\w\s:/().,-]", "", text)

        text = text.replace("|", "")

        text = text.strip()

        return text

    def detect_transaction(self, text):

        patterns = [

            r"\bVA\d{2}\b",
            r"\bME\d{2}N\b",
            r"\bVL\d{2}N\b",
            r"\bXD\d{2}\b",
            r"\bFB\d{2}\b",
            r"\bMM\d{2}\b",
            r"\bSE\d{2}\b",
            r"\bSM\d{2}\b",

        ]

        for pattern in patterns:

            match = re.search(pattern, text)

            if match:
                return match.group()

        return None

    def extract(self, image_path):

        image = cv2.imread(str(image_path))

        processed = self.preprocess(image)

        data = pytesseract.image_to_data(
            processed,
            output_type=pytesseract.Output.DICT,
        )

        words = []

        confidences = []

        for i in range(len(data["text"])):

            word = data["text"][i].strip()

            if not word:
                continue

            confidence = float(data["conf"][i])

            if confidence < 40:
                continue

            words.append(word)

            confidences.append(confidence)

        text = " ".join(words)

        text = self.clean_text(text)

        transaction = self.detect_transaction(text)

        average_confidence = (
            sum(confidences) / len(confidences)
            if confidences
            else 0
        )

        return {

            "text": text,

            "transaction": transaction,

            "confidence": round(
                average_confidence,
                2,
            ),

            "wordCount": len(words),

        }

    def process_folder(self, frame_folder):

        frame_folder = Path(frame_folder)

        results = []

        for image in sorted(frame_folder.glob("*.png")):

            result = self.extract(image)

            result["image"] = image.name

            results.append(result)

        return results