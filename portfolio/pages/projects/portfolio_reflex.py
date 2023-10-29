import reflex as rx

from portfolio.components.layout.main import main
from portfolio.components.layout.project_information import project_information

@rx.page(route="/projects/portfolio-reflex")
def portfolio_reflex() -> rx.Component:
    return main(
        project_information(
            "Portfolio Reflex",
            rx.box(
                rx.text(
                    "Welcome to my portfolio build with Reflex"
                )
            )
        )
    )