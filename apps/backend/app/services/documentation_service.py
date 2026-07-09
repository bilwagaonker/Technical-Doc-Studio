from pathlib import Path
import json
import os
import re
import pickle
import hashlib

import faiss
import numpy as np
import ollama

from bs4 import BeautifulSoup
from docx import Document
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer


class DocumentationService:

    def __init__(self):

        self.model = "qwen2.5:7b"

        self.embedding_model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        self.documents = []

        self.document_sources = []

        self.index = None
        
        self.embedding_folder = Path("knowledge/embeddings")

        self.embedding_folder.mkdir(
        parents=True,
        exist_ok=True
        )

        self.index_file = self.embedding_folder / "faiss.index"

        self.documents_file = self.embedding_folder / "documents.pkl"

        self.metadata_file = self.embedding_folder / "metadata.json"

        self.initialize_index()
        
    ####################################################################
    #INITIALIZE INDEX
    ####################################################################
    def initialize_index(self):

        current_hash = self.calculate_hash()

        try:

            with open(self.metadata_file, "r", encoding="utf-8") as f:
                metadata = json.load(f)

            if metadata.get("hash") == current_hash:

                print("Loading Knowledge Base...")

                self.load_index()

                return

        except Exception as ex:

            print(f"Invalid knowledge cache: {ex}")

        print("Rebuilding Knowledge Base...")

        self.load_knowledge()
            
    #SAVE INDEX
            
    def save_index(self):

        faiss.write_index(

        self.index,

        str(self.index_file)

        )

        with open(

            self.documents_file,

            "wb"

        ) as file:

            pickle.dump(

            {

                "documents": self.documents,

                "sources": self.document_sources

            },

            file)

        metadata = {

            "documents": len(self.documents),

            "sources": len(

                set(self.document_sources)

            ),

            "hash": self.calculate_hash()

        }

        with open(

            self.metadata_file,

            "w",

            encoding="utf8"

        ) as file:

            json.dump(

                metadata,

                file,

                indent=4

            )

        print("Knowledge Base Saved")
        
    #LOAD INDEX
    def load_index(self):

        self.index = faiss.read_index(

            str(self.index_file)

        )

        with open(

            self.documents_file,

            "rb"

        ) as file:

            data = pickle.load(file)

        self.documents = data["documents"]

        self.document_sources = data["sources"]

        print(

            f"Loaded {len(self.documents)} chunks"

        )
    #####################################################################
    # KNOWLEDGE LOADER
    #####################################################################

    def load_knowledge(self):

        folders = [

            "knowledge/blogs",

            "knowledge/sop",

            "knowledge/qrgs",

            "knowledge/sap_help"

        ]

        self.documents = []

        self.document_sources = []

        for folder in folders:

            if not Path(folder).exists():
                continue

            for file in Path(folder).rglob("*"):

                suffix = file.suffix.lower()

                try:

                    text = ""

                    if suffix == ".html":

                        with open(file, encoding="utf8") as f:

                            soup = BeautifulSoup(
                                f,
                                "html.parser"
                            )

                            text = soup.get_text(
                                separator=" "
                            )

                    elif suffix == ".pdf":

                        reader = PdfReader(file)

                        pages = []

                        for page in reader.pages:

                            extracted = page.extract_text()

                            if extracted:
                                pages.append(extracted)

                        text = "\n".join(pages)

                    elif suffix == ".docx":

                        document = Document(file)

                        text = "\n".join(

                            p.text

                            for p in document.paragraphs

                        )

                    elif suffix == ".md":

                        text = file.read_text(
                            encoding="utf8"
                        )

                    elif suffix == ".txt":

                        text = file.read_text(
                            encoding="utf8"
                        )

                    if len(text.strip()) < 100:
                        continue

                    chunks = self.chunk_document(text)

                    for chunk in chunks:

                        self.documents.append(chunk)

                        self.document_sources.append(
                            file.name
                        )

                except Exception as ex:

                    print(file)

                    print(ex)

        self.build_index()

    #####################################################################
    # CHUNK DOCUMENTS
    #####################################################################

    def chunk_document(

        self,

        text,

        chunk_size=600,

        overlap=120

    ):

        words = text.split()

        chunks = []

        start = 0

        while start < len(words):

            end = start + chunk_size

            chunk = " ".join(

                words[start:end]

            )

            chunks.append(chunk)

            start += chunk_size - overlap

        return chunks

    #####################################################################
    # BUILD VECTOR INDEX
    #####################################################################

    def build_index(self):

        if not self.documents:

            return

        embeddings = self.embedding_model.encode(

            self.documents,

            show_progress_bar=True

        )

        embeddings = np.array(

            embeddings,

            dtype=np.float32

        )

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(

            dimension

        )

        self.index.add(
            embeddings
        )
        
        self.save_index()

    #####################################################################
    # SEARCH
    #####################################################################

    def retrieve(

        self,

        query,

        top_k=5

    ):

        if self.index is None:

            return []

        embedding = self.embedding_model.encode(

            [query]

        )

        embedding = np.array(

            embedding,

            dtype=np.float32

        )

        distance, index = self.index.search(

            embedding,

            top_k

        )

        results = []

        for i in index[0]:

            results.append(

                {

                    "source": self.document_sources[i],

                    "content": self.documents[i]

                }

            )

        return results
    
    #CALCULATE HASH
    def calculate_hash(self):

        folders = [

            "knowledge/blogs",

            "knowledge/qrgs",

            "knowledge/sap_help",

            "knowledge/sop"

        ]

        hash_md5 = hashlib.md5()

        for folder in folders:

            if not Path(folder).exists():

                continue

            for file in sorted(

                Path(folder).rglob("*")

            ):
                if file.is_file():

                    hash_md5.update(

                    str(file).encode()

                    )

                hash_md5.update(

                    str(

                        file.stat().st_mtime

                    ).encode()

                )

        return hash_md5.hexdigest()

    #####################################################################
    # PROMPT
    #####################################################################

    def build_prompt(
    self,
    metadata,
    steps,
    references
    ):

        reference_text = "\n\n".join(
        r["content"]
        for r in references
        )

        step_text = ""

        for step in steps:

            step_text += f"""

    STEP {step['step']}

    Frame:
    {step['frame']}

    OCR:
    {step['ocr']}

    Speech:
    {step['speech']}

    Transaction:
    {step['transaction']}

----------------------------------------
"""

        return f"""
You are an SAP Functional Consultant.

Your task is to convert the extracted SAP video information into a professional
step-by-step Quick Reference Guide.

Rules
For every detected screenshot:

1. Read the OCR text.
2. Read the speech transcript.
3. Merge both.
4. Correct OCR mistakes.
5. Produce a meaningful title.
6. Produce a concise description (2–4 sentences).
7. If speech is empty, infer the action from the OCR.
8. Never leave title or description blank.
9. Preserve the image filename exactly.

Return ONLY JSON.

Do NOT write explanations.

Do NOT use markdown.

Do NOT wrap inside ```json.

1. Ignore unreadable OCR.
2. Ignore website names.
3. Ignore timestamps.
4. Ignore browser text.
5. Ignore watermarks.
6. Merge OCR with speech.
7. Correct OCR mistakes.
8. Do not invent SAP fields.
9. One screenshot = one step.
10. Return ONLY JSON.

Reference Documentation

{reference_text}

------------------------------------------------

Video Metadata

{json.dumps(metadata, indent=2)}

------------------------------------------------

Detected Steps

{step_text}

------------------------------------------------

Return JSON

{{
    "transaction":"",
    "title":"",
    "purpose":"",
    "steps":[
        {{
            "step":1,
            "title":"",
            "description":"",
            "image":"frame_00001.png"
        }}
    ]
}}
"""
#######################
#CALL
###################
    def call_llm(self, prompt):

        response = ollama.chat(

            model=self.model,
            format="json",
            messages=[

                {

                    "role":"user",

                    "content":prompt

                }

            ]

        )

        return response["message"]["content"]


    #####################################################################
    # GENERATE
    #####################################################################
    def generate(self, metadata, steps):

        transaction = ""

        for s in steps:

            if s["transaction"]:

                transaction = s["transaction"]

            break

        query = transaction

        references = self.retrieve(query, top_k=5)

        prompt = self.build_prompt(
            metadata,
            steps,
            references
        )

        response = self.call_llm(prompt)
        print(response)

        documentation = self.normalize_output(response, steps)

        return documentation
    
    #####################################################################
    # NORMALIZE
    #####################################################################

    
    
    def normalize_output(self, text, steps):

    # --------------------------------------------
    # Extract JSON from Ollama response
    # --------------------------------------------

        match = re.search(
            r"```json\s*(.*?)\s*```",
            text,
            re.DOTALL
        )

        if match:
            text = match.group(1)

        else:
            start = text.find("{")
            end = text.rfind("}")

            if start != -1 and end != -1:
                text = text[start:end + 1]

        data = json.loads(text)

    # --------------------------------------------
    # Basic Documentation
    # --------------------------------------------

        documentation = {

        "transaction": data.get(
            "transaction",
            "SAP_DOCUMENT"
        ),

        "title": data.get(
            "title",
            "SAP Documentation"
        ),

        "purpose": data.get(
            "purpose",
            ""
        ),

        "steps": []

        }

        generated_steps = data.get("steps", [])

    # --------------------------------------------
    # Merge LLM output with pipeline steps
    # --------------------------------------------

        for index, original in enumerate(steps):

            # Get generated step (if available)
            generated = {}

            if index < len(generated_steps):
                generated = generated_steps[index]

        # Safely determine image filename
            image = original.get("image")

            if not image:

                frame = original.get("frame")

                if isinstance(frame, str):

                    if frame.endswith(".png"):
                        image = frame

                    else:
                        image = f"{frame}.png"

                elif isinstance(frame, int):

                    image = f"frame_{frame:05}.png"

                elif isinstance(original.get("frameNumber"), int):

                    image = f"frame_{original['frameNumber']:05}.png"

            else:

                image = f"frame_{index:05}.png"

            documentation["steps"].append({

                "step": index + 1,

                "title": generated.get(
                    "title",
                ""
                ),

                "description": generated.get(
                    "description",
                ""
                ),

                "image": image

            })

        return documentation