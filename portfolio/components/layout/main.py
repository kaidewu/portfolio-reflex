import reflex as rx

from portfolio.components.navbar import navbar
from portfolio.components.footer import footer

def main(*args) -> rx.Component:
    return rx.box(
        navbar(),
        rx.container(
            *args,
            footer(),
            maxW="container.sm",
            pt="20"
        ),
        as_="main",
        pb="8"
    )