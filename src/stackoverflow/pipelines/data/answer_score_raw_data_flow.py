"""
The module implements a Metaflow Pipeline for creating the Raw Data Layer for the StackOverflow
Answer Score Classification use case.
"""

# Import Standard Modules
import logging
from metaflow import FlowSpec, step

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


class AnswerScoreRawDataFlow(FlowSpec):
    @step
    def start(self):
        logging.info("Starting AnswerScoreRawDataFlow")
        self.next(self.end)

    @step
    def end(self):
        print("✅ StackOverflow Badge Classification raw data created.")


if __name__ == "__main__":
    # TODO: It does not work if I do not add this!
    AnswerScoreRawDataFlow()
