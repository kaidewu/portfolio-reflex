import reflex as rx

from portfolio.components.navbar import navbar
from portfolio.components.footer import footer

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