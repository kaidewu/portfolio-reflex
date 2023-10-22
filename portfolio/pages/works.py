import reflex as rx


from portfolio.components.layout.main import main
from portfolio.components.project_item import project_item

def works() -> rx.Component:
    return main(
        rx.container(
            "Works Page"
        )
    )
