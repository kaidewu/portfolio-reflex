import reflex as rx

from portfolio.components.layout.main import main

def contact():
    return main(
        rx.container(
            rx.box(
                "Contact Page!"
            )
        )
    )