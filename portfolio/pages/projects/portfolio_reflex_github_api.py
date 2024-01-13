import reflex as rx

from portfolio.components.layout.main import main
from portfolio.components.projects import title

@rx.page(route="/projects/portfolio-reflex-github-api")
def portfolio_reflex_github_api() -> rx.Component:
    return main(
        rx.container(
            title(
                "Portfolio Reflex Github API"
            ),
            "Portfolio Reflex Using Github API Page!"
        )
    )