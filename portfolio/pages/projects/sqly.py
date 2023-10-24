import reflex as rx

from portfolio.components.layout.main import main

@rx.page(route="/projects/sqly")
def sqly() -> rx.Component:
    return main(
        rx.container(
            "SQL Generator Page!"
        )
    )