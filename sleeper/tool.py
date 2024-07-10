from __future__ import annotations

import time

from griptape.artifacts import InfoArtifact
from griptape.tools import BaseTool
from griptape.utils.decorators import activity
from schema import Schema, Literal

class Sleeper(BaseTool):
    @activity(config={
            "description": "Can be used to sleep for a number of seconds",
            "schema": Schema({
                Literal(
                    "seconds",
                    description="Number of seconds to sleep for"
                ): int
            })
        })
    def generate(self, params: dict) -> InfoArtifact:
        seconds = params["values"]["seconds"]
        time.sleep(seconds)
        return InfoArtifact(f"Slept for {seconds} seconds")
