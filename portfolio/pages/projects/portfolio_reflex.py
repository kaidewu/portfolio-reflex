import reflex as rx

from portfolio.components.layout.main import main

@rx.page(route="/projects/portfolio-reflex")
def portfolio_reflex() -> rx.Component:
    return main(
        rx.container(
            "Portfolio Reflex Page!"
        )
    )