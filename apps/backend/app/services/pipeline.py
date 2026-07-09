from pathlib import Path

from app.services.metadata_service import MetadataService
from app.services.frame_service import FrameService
from app.services.ocr_service import OCRService
from app.services.sap_detector import SAPDetector
from app.services.whisper_service import WhisperService
from app.services.documentation_service import DocumentationService
from app.services.export_service import ExportService
from app.services.scene_service import SceneService



class VideoPipeline:

    def __init__(self):

        self.metadata = MetadataService()

        self.frames = FrameService()

        self.ocr = OCRService()

        self.sap = SAPDetector()

        self.whisper = WhisperService()

        self.documentation = DocumentationService()

        self.export = ExportService()
        
        self.scene = SceneService()

    ##############################################################

    def build_steps(
        self,
        ocr_results,
        transcript
    ):

        steps = []

        segments = transcript.get("segments", [])

        for index, result in enumerate(ocr_results):

            speech = ""

            if index < len(segments):

                speech = segments[index]["text"]

            steps.append(

                {

                    "step": index + 1,

                    "frame": result["image"],

                    "ocr": result["text"],

                    "speech": speech,

                    "transaction": result.get("transaction"),

                    "screenType": result.get("screenType"),

                    "fields": result.get("fields", []),

                    "navigation": result.get("navigation", [])

                }

            )

        return steps

    ##############################################################

    def process(
        self,
        video_path
    ):

        print("Metadata...")

        metadata = self.metadata.extract(
            video_path
        )

        ###########################################################

        print("Extracting Frames...")

        frame_folder = Path(
            "app/storage/frames"
        )

        frame_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        extracted_frames = self.frames.extract_frames(

            video_path,

            str(frame_folder)

        )
        
        extracted_frames = self.scene.filter_frames(extracted_frames)

        ###########################################################

        print("OCR...")

        ocr_results = self.ocr.process_frames(
            extracted_frames
        )

        ###########################################################

        print("SAP Detection...")

        sap_results = []

        for result in ocr_results:

            image_path = frame_folder / result["image"]

            sap_results.append(

                self.sap.process(

                    image_path,

                    result

                )

            )

        ###########################################################

        print("Speech Recognition...")

        transcript = self.whisper.transcribe(
            video_path
        )

        ###########################################################

        print("Building Steps...")

        steps = self.build_steps(

            sap_results,

            transcript

        )

        ###########################################################

        print("Generating Documentation...")

        documentation = self.documentation.generate(

            metadata,

            steps

        )

        ###########################################################

        print("Exporting DOCX...")

        output_file = self.export.export_docx(

            documentation,

            frame_folder

        )

        ###########################################################

        return {

            "metadata": metadata,

            "documentation": documentation,

            "document": str(output_file),

            "steps": len(steps),

            "frames": len(extracted_frames)

        }