import reflex as rx

from kaide_portfolio.components.layout.main import main

def works():
    return main(
        rx.container(
            rx.box(
                "My Projects!"
            )
        )
    )