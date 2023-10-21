import reflex as rx

from kaide_portfolio.components.navbar import navbar
from kaide_portfolio.components.footer import footer

def main(*args):
    return rx.box(
        navbar(),
        rx.container(
            *args,
            footer(),
            maxW="container.md",
            pt={14}
        ),
        as_="main",
        pb={8}
    )