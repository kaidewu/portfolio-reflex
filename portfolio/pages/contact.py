import reflex as rx

from portfolio.components.layout.main import main

def contact() -> rx.Component:
    return main(
        rx.container(
            rx.box(
                "Contact Page!"
            )
        )
    )