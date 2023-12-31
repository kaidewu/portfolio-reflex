import reflex as rx
from portfolio.constants import NAME

config = rx.Config(
    port=3000,
    app_name="portfolio",
    username=NAME,
    telemetry_enabled=False,
    frontend_packages={
        "typewriter-effect"
    },
    tailwind={
        "theme": {
            "extend": {},
            "container": {
                "center": True,
            },
        },
        "plugins": ["@tailwindcss/typography"],
    },
)