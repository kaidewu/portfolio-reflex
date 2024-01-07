import reflex as rx

from portfolio.components.layout.main import main

@rx.page(route="/projects/cloudy")
def cloudy() -> rx.Component:
    return main(
        rx.container(
            "Cloudy Page!"
        )
    )