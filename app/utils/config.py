from dotenv import load_dotenv
import os

load_dotenv()

class Settings:

    APP_NAME = os.getenv(
        "APP_NAME",
        "AI Knowledge Assistant"
    )

    MODEL_NAME = os.getenv(
        "MODEL_NAME",
        "mistral"
    )

    TOP_K = int(
        os.getenv(
            "TOP_K",
            3
        )
    )