import reflex as rx

from portfolio.components.layout.main import main
from portfolio.components.projects import title

@rx.page(route="/projects/portfolio-reflex")
def portfolio_reflex() -> rx.Component:
    return main(
        "Portfolio Reflex",
        rx.box(
            rx.text(
                "Welcome to my portfolio build with Reflex"
            )
        )
    )