import reflex as rx
from portfolio.components.paragraph import paragraph

def about_me() -> rx.Component:
    return rx.container(
        rx.box(
            rx.heading(
                "About me",
                as_="h2",
                fontSize="2em",
                variant="section-title",
                textDecorationThickness="2.5px",
                fontWeight="bold",
                pb="2"
            ),
            paragraph(
                """
                A System Administrator that currently employed as an Implantation Consultant for Hospital Information Systems (HIS). 
                An avid tech enthusiast, engaging in personal programming projects, staying abreast of cutting-edge technological advancements, 
                and continuously broadening my skillset. 
                """
            )
        ),
        delay="0.1",
        pt="10",
        fontSize="17"
    )