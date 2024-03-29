from __future__ import annotations

import reflex as rx
from portfolio.constants import NAME

config = rx.Config(
    app_name="portfolio",
    username=NAME,
    telemetry_enabled=False,
    frontend_packages={
        "typewriter-effect",
        "react-copy-to-clipboard"
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
    loglevel="debug"
)