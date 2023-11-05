import reflex as rx
from dotenv import load_dotenv

load_dotenv()


config = rx.Config(
    port=3000,
    app_name="portfolio",
    username="Kaide Wu",
    telemetry_enabled=False,
    frontend_packages={
        "typewriter-effect"
    }
)