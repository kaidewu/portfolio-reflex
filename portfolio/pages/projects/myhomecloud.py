import reflex as rx

from portfolio.components.layout.main import main

@rx.page(route="/projects/myhomecloud")
def my_home_cloud() -> rx.Component:
    return main(
        rx.container(
            "MyHomeCloud Page!"
        )
    )