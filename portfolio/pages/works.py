import reflex as rx


from portfolio.components.layout.main import main
from portfolio.components.project_item import project_item

def works() -> rx.Component:
    return main(
        rx.container(
            rx.text(
                "I'm actually working in ",
                rx.link(
                    "Laberit",
                    href="https://www.laberit.com/",
                    passHref=True,
                    scroll="false",
                    fontWeight="bold"
                ),
                " as a Consultant and Implanter of an Hospital Information System (HIS).",
                textAlign="justify"
            ),
        )
    )
