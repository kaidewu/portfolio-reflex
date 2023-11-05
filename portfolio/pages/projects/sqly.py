import reflex as rx

from portfolio.components.layout.main import main
from portfolio.components.projects import title

@rx.page(route="/projects/sqly")
def sqly() -> rx.Component:
    return main(
        rx.container(
            "SQL Generator Page!"
        )
    )