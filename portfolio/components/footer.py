import reflex as rx

from datetime import date

def footer() -> rx.Component:
    return rx.box(
        f"© {date.today().year} Kaide Wu. All rights Reserved.",
        alignItems="center",
        opacity={0.4},
        fontSize="sm"
    )