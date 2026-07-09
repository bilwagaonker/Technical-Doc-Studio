from pathlib import Path
import cv2
import numpy as np


class FrameService:

    @staticmethod
    def extract_frames(
        video_path: str,
        output_folder: str,
        scene_threshold: float = 0.92,
        minimum_gap: float = 1.5
    ):

        output_folder = Path(output_folder)
        output_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        capture = cv2.VideoCapture(video_path)

        fps = capture.get(cv2.CAP_PROP_FPS)

        previous_gray = None

        last_saved_time = -100

        frame_number = 0

        extracted_frames = []

        while True:

            success, frame = capture.read()

            if not success:
                break

            timestamp = frame_number / fps

            gray = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2GRAY
            )

            gray = cv2.GaussianBlur(
                gray,
                (5, 5),
                0
            )

            save = False

            if previous_gray is None:

                save = True

            else:

                difference = cv2.absdiff(
                    previous_gray,
                    gray
                )

                score = np.mean(difference)

                if (
                    score > scene_threshold
                    and
                    timestamp - last_saved_time >= minimum_gap
                ):
                    save = True

            if save:

                image_name = (
                    f"frame_{len(extracted_frames):05}.png"
                )

                image_path = output_folder / image_name

                cv2.imwrite(
                    str(image_path),
                    frame
                )

                extracted_frames.append(

                    {

                        "frame": len(extracted_frames) + 1,

                        "frameNumber": frame_number,

                        "timestamp": round(
                            timestamp,
                            2
                        ),

                        "image": image_name,

                        "path": str(image_path)

                    }

                )

                previous_gray = gray

                last_saved_time = timestamp

            frame_number += 1

        capture.release()

        return extracted_frames