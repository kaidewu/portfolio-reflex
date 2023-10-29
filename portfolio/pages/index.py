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
                    textAlign="justify"
                ),
                rx.text(
                    "As a hobby, I love immersing myself in the world of programming. I enjoy creating personal projects, exploring the latest tech trends, and continuously expanding my skills",
                    textAlign="justify"
                ),
                rx.box(
                    rx.center(
                        rx.link(
                            rx.button(
                                "My Projects",
                                rx.icon(
                                    tag="chevron_right",
                                ),
                                scroll=False,
                                color_scheme="telegram"
                            ),
                            href="/projects"
                        ),
                    ),
                    my={4}
                ),
                delay={0.1},
                pt={10}
            )
        )
    )