from faster_whisper import WhisperModel
import re


class WhisperService:

    def __init__(self):

        self.model = WhisperModel(
            "base",
            device="cpu",
            compute_type="int8"
        )

    def clean_text(self, text):

        text = re.sub(r"\s+", " ", text)

        fillers = {
            "uh",
            "um",
            "okay",
            "ok",
            "hmm",
            "actually",
            "basically"
        }

        words = []

        for word in text.split():

            if word.lower() not in fillers:
                words.append(word)

        return " ".join(words)

    def transcribe(self, video_path):

        segments, info = self.model.transcribe(
            video_path,
            beam_size=5
        )

        transcript = []

        timeline = []

        for segment in segments:

            cleaned = self.clean_text(segment.text)

            transcript.append(cleaned)

            timeline.append({

                "start": round(segment.start,2),

                "end": round(segment.end,2),

                "text": cleaned

            })

        return {

            "language": info.language,

            "duration": info.duration,

            "transcript": " ".join(transcript),

            "timeline": timeline

        }