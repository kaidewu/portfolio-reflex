import reflex as rx

from portfolio.components.layout.main import main

def works():
    return main(
        rx.container(
            rx.box(
                "My Projects!"
            )
        )
    )