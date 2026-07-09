from pathlib import Path
from datetime import datetime
import re

from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT


class ExportService:

    def __init__(self):
        pass

    def _safe(self, value, default=""):

        if value is None:
            return default

        return str(value)

    def _safe_filename(self, name):

        name = self._safe(name, "SAP_Documentation")

        name = re.sub(r'[\\/*?:"<>|]', "", name)

        name = name.replace(" ", "_")

        return name

    def export_docx(

        self,

        documentation,

        frame_folder,

        output_folder="app/storage/output"

    ):

        output_folder = Path(output_folder)

        output_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        frame_folder = Path(frame_folder)

        document = Document()

        ###############################################################
        # Cover
        ###############################################################

        transaction = documentation.get(
            "transaction",
            "SAP Documentation"
        )

        title = document.add_heading(
            transaction,
            level=1
        )

        title.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

        subtitle = document.add_paragraph()

        subtitle.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

        subtitle.add_run(
            documentation.get(
                "title",
                "Technical Process Documentation"
            )
        ).bold = True

        document.add_paragraph(
            f"Generated : {datetime.now():%d-%b-%Y %H:%M}"
        )

        document.add_page_break()

        ###############################################################
        # Purpose
        ###############################################################

        document.add_heading(
            "Purpose",
            level=1
        )

        document.add_paragraph(
            documentation.get(
                "purpose",
                "Purpose not generated."
            )
        )

        ###############################################################
        # Prerequisites
        ###############################################################

        prereq = documentation.get(
            "prerequisites",
            []
        )

        if prereq:

            document.add_heading(
                "Prerequisites",
                level=1
            )

            for item in prereq:

                document.add_paragraph(
                    str(item),
                    style="List Bullet"
                )

        ###############################################################
        # Procedure
        ###############################################################

        document.add_heading(
            "Procedure",
            level=1
        )

        steps = documentation.get(
            "steps",
            []
        )

        if not steps:

            document.add_paragraph(
                "No procedural steps generated."
            )

        for index, step in enumerate(steps, start=1):

            document.add_heading(
                f"Step {step.get('step', index)}",
                level=2
            )

            if step.get("title"):

                run = document.add_paragraph().add_run(
                    step["title"]
                )

                run.bold = True

            document.add_paragraph(
                step.get(
                    "description",
                    ""
                )
            )

            ###########################################################
            # SAP Fields
            ###########################################################

            fields = step.get(
                "fields",
                []
            )

            if fields:

                document.add_heading(
                    "Fields",
                    level=3
                )

                table = document.add_table(
                    rows=1,
                    cols=2
                )

                table.style = "Light Grid"

                hdr = table.rows[0].cells

                hdr[0].text = "Field"

                hdr[1].text = "Description"

                for field in fields:

                    row = table.add_row().cells

                    if isinstance(field, dict):

                        row[0].text = self._safe(
                            field.get("name")
                        )

                        row[1].text = self._safe(
                            field.get("description")
                        )

                    else:

                        row[0].text = self._safe(field)

                        row[1].text = ""

            ###########################################################
            # Expected Result
            ###########################################################

            if step.get("expected_result"):

                document.add_heading(
                    "Expected Result",
                    level=3
                )

                document.add_paragraph(
                    step["expected_result"]
                )

            ###########################################################
            # Screenshot
            ###########################################################

            image_name = step.get("image")

            if image_name:

                image_path = frame_folder / image_name

                if image_path.exists():

                    document.add_picture(
                        str(image_path),
                        width=Inches(6.3)
                    )

                    caption = document.add_paragraph(
                        f"Figure {index}"
                    )

                    caption.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

        ###############################################################
        # Notes
        ###############################################################

        notes = documentation.get(
            "notes",
            []
        )

        if notes:

            document.add_heading(
                "Notes",
                level=1
            )

            for note in notes:

                document.add_paragraph(
                    str(note),
                    style="List Bullet"
                )

        ###############################################################
        # Warnings
        ###############################################################

        warnings = documentation.get(
            "warnings",
            []
        )

        if warnings:

            document.add_heading(
                "Warnings",
                level=1
            )

            for warning in warnings:

                document.add_paragraph(
                    str(warning),
                    style="List Bullet"
                )

        ###############################################################
        # Footer
        ###############################################################

        section = document.sections[0]

        footer = section.footer

        footer.paragraphs[0].text = (
            "Generated by AI Technical Documentation Studio"
        )

        ###############################################################
        # Save
        ###############################################################

        filename = self._safe_filename(transaction)

        output_file = output_folder / f"{filename}.docx"

        document.save(output_file)

        return output_file