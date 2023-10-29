import reflex as rx

from portfolio.components.layout.main import main

@rx.page(route="/projects/portfolio-reflex-github-api")
def portfolio_reflex_github_api() -> rx.Component:
    return main(
        rx.container(
            "Portfolio Reflex Using Github API Page!"
        )
    )