import reflex as rx

config = rx.Config(
    app_name="portfolio",
    username="Kaide Wu",
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