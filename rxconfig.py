import reflex as rx
from portfolio.constants import USERNAME

config = rx.Config(
    app_name="portfolio",
    username=USERNAME,
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