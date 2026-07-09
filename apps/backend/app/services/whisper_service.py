from faster_whisper import WhisperModel

class WhisperService:

    def __init__(self):

        self.model = WhisperModel(
            "base",
            device="cpu",
            compute_type="int8"
        )

    def transcribe(self, video_path):

        segments, info = self.model.transcribe(
            video_path,
            beam_size=5
        )

        transcript = []
        full_text = []

        for segment in segments:

            transcript.append(
                {
                    "start": segment.start,
                    "end": segment.end,
                    "text": segment.text.strip()
                }
            )

            full_text.append(segment.text.strip())

        return {
            "text": " ".join(full_text),
            "segments": transcript,
            "language": info.language
        }