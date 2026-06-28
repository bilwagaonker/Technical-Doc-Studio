import re
import cv2
#import pytesseract

class SAPDetector:

    SAP_KEYWORDS = [

        "SAP",
        "Command",
        "Menu",
        "Favorites",
        "System",
        "Help",
        "Enter",
        "Save",
        "Back",
        "Exit",
        "Cancel",

        "Sales Organization",
        "Distribution Channel",
        "Division",
        "Company Code",
        "Plant",
        "Storage Location",
        "Customer",
        "Material",
        "Vendor",

    ]

    TRANSACTION_PATTERNS = [

        r"\bVA\d{2}\b",
        r"\bME\d{2}N\b",
        r"\bVL\d{2}N\b",
        r"\bMM\d{2}\b",
        r"\bFB\d{2}\b",
        r"\bXD\d{2}\b",
        r"\bSE\d{2}\b",
        r"\bSM\d{2}\b",

    ]

    EXTERNAL_PATTERNS = {

        "Excel":[
            "Microsoft Excel",
            ".xlsx",
            ".xls",
            "Workbook",
            "Sheet1"
        ],

        "PDF":[
            "Adobe",
            "Acrobat",
            "PDF"
        ],

        "Browser":[
            "Chrome",
            "Edge",
            "Firefox",
            "http",
            "https"
        ]

    }

    FIELD_NAMES = [

        "Sales Organization",
        "Distribution Channel",
        "Division",
        "Plant",
        "Company Code",
        "Material",
        "Customer",
        "Vendor",
        "Ship-to Party",
        "Sold-to Party",
        "Storage Location",

    ]

    def detect_system(self, text):

        for system, words in self.EXTERNAL_PATTERNS.items():

            for word in words:

                if word.lower() in text.lower():

                    return system

        score = 0

        for keyword in self.SAP_KEYWORDS:

            if keyword.lower() in text.lower():

                score += 1

        if score >= 3:

            return "SAP"

        return "Unknown"

    def detect_transaction(self, text):

        for pattern in self.TRANSACTION_PATTERNS:

            match = re.search(pattern, text)

            if match:

                return match.group()

        return None

    def detect_screen_type(self, text):

        text = text.lower()

        if "create" in text:

            return "Create"

        if "change" in text:

            return "Change"

        if "display" in text:

            return "Display"

        if "overview" in text:

            return "Overview"

        if "selection" in text:

            return "Selection"

        if "popup" in text:

            return "Popup"

        return "Unknown"

    def detect_fields(self, text):

        fields = []

        for field in self.FIELD_NAMES:

            if field.lower() in text.lower():

                fields.append(field)

        return fields

    def detect_navigation(self, text):

        buttons = []

        navigation = [

            "Enter",
            "Save",
            "Back",
            "Exit",
            "Cancel",
            "Execute",
            "Continue",
            "Next",
            "Previous"

        ]

        for item in navigation:

            if item.lower() in text.lower():

                buttons.append(item)

        return buttons

    def detect_highlight_regions(self, image):

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        edges = cv2.Canny(gray,50,150)

        contours,_ = cv2.findContours(
            edges,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        highlights=[]

        for contour in contours:

            x,y,w,h=cv2.boundingRect(contour)

            if w<60:
                continue

            if h<18:
                continue

            if w>700:
                continue

            if h>120:
                continue

            highlights.append({

                "x":int(x),

                "y":int(y),

                "width":int(w),

                "height":int(h)

            })

        return highlights

    def process(self,image_path,ocr_result):

        image=cv2.imread(str(image_path))

        text=ocr_result["text"]

        ocr_result["system"]=self.detect_system(text)

        ocr_result["transaction"]=self.detect_transaction(text)

        ocr_result["screenType"]=self.detect_screen_type(text)

        ocr_result["fields"]=self.detect_fields(text)

        ocr_result["navigation"]=self.detect_navigation(text)

        ocr_result["highlightRegions"]=self.detect_highlight_regions(image)

        return ocr_result