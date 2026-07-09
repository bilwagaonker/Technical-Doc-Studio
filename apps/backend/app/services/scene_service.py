import cv2
import numpy as np
from pathlib import Path


class SceneService:

    def __init__(self):

        # similarity threshold
        self.similarity_threshold = 0.97

    ####################################################################
    # Remove duplicate screenshots
    ####################################################################

    def filter_frames(self, frames):

        if len(frames) <= 1:
            return frames

        filtered = []

        previous_image = None

        for frame in frames:

            image = cv2.imread(frame["path"])

            if image is None:
                continue

            gray = cv2.cvtColor(
                image,
                cv2.COLOR_BGR2GRAY
            )

            gray = cv2.resize(
                gray,
                (320, 180)
            )

            if previous_image is None:

                filtered.append(frame)

                previous_image = gray

                continue

            similarity = self.compare(
                previous_image,
                gray
            )

            if similarity < self.similarity_threshold:

                filtered.append(frame)

                previous_image = gray

        print(
            f"Frames after filtering : {len(filtered)}"
        )

        return filtered

    ####################################################################
    # Compare two screenshots
    ####################################################################

    def compare(
        self,
        image1,
        image2
    ):

        result = cv2.matchTemplate(

            image1,

            image2,

            cv2.TM_CCOEFF_NORMED

        )

        return float(result[0][0])