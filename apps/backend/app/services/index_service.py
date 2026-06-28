import json
from pathlib import Path


class IndexService:

    @staticmethod
    def save(
        frames,
        destination
    ):

        Path(destination).parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(destination, "w") as file:

            json.dump(
                frames,
                file,
                indent=4
            )