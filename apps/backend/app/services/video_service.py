from app.services.pipeline import VideoPipeline


class VideoService:

    def __init__(self):

        self.pipeline = VideoPipeline()

    def process_video(self, video_path):

        return self.pipeline.process(
            str(video_path)
        )