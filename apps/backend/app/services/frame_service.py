from pathlib import Path
import cv2
import numpy as np


class FrameService:

    @staticmethod
    def extract_frames(
        video_path: str,
        output_folder: str,
        threshold: float = 0.92,
        min_gap_seconds: float = 1.0
    ):

        Path(output_folder).mkdir(parents=True, exist_ok=True)

        capture = cv2.VideoCapture(video_path)

        fps = capture.get(cv2.CAP_PROP_FPS)

        previous_gray = None

        last_saved_time = -100

        frame_number = 0

        frames = []

        while True:

            success, frame = capture.read()

            if not success:
                break

            current_time = frame_number / fps

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            gray = cv2.GaussianBlur(gray, (5, 5), 0)

            save_frame = False

            if previous_gray is None:
                save_frame = True

            else:

                similarity = cv2.matchTemplate(
                    gray,
                    previous_gray,
                    cv2.TM_CCOEFF_NORMED
                )[0][0]

                if (
                    similarity < threshold
                    and current_time - last_saved_time >= min_gap_seconds
                ):
                    save_frame = True

            if save_frame:

                filename = f"frame_{len(frames):05}.png"

                filepath = Path(output_folder) / filename

                cv2.imwrite(str(filepath), frame)

                frames.append(
                    {
                        "frameNumber": frame_number,
                        "timestamp": round(current_time, 2),
                        "image": filename
                    }
                )

                previous_gray = gray

                last_saved_time = current_time

            frame_number += 1

        capture.release()

        return frames