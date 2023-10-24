import reflex as rx

from portfolio.components.layout.main import main

def index() -> rx.Component:
    return main(
        rx.container(
            rx.box(
                rx.heading(
                    "Hey, I'm Kaide",
                    as_="h3",
                    variant="section-title"
                ),
                rx.text(
                    "I'm actually working in ",
                    rx.link(
                        "Laberit",
                        href="https://www.laberit.com/",
                        passHref=True,
                        scroll={False},
                        fontWeight="bold"
                    ),
                    " as a Consultant and Implanter of an Hospital Information System (HIS).",
                    " as a Consultant and Implanter of an Hospital Information System (HIS).",
                    textAlign="justify"
                ),
                delay={0.1},
                pt={10}
            )
        )
    )