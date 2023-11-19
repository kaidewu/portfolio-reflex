import reflex as rx


from portfolio.components.layout.main import main
from portfolio.components.bio import bio_section, bio_year

def works() -> rx.Component:
    return main(
        rx.container(
            rx.heading(
                "Work",
                as_="h3",
                variant="section-title",
                textDecoration="underline",
                textDecorationThickness="5px",
                pb="2",
                fontSize="1.75em"
            ),
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
            pt="1em",
            pb="1em"
        ),
        rx.container(
            rx.heading(
                "Bio",
                as_="h3",
                variant="section-title",
                textDecoration="underline",
                textDecorationThickness="5px",
                pb="2",
                fontSize="1.75em"
            ),
            bio_section(
                bio_year("2002"),
                "Born in Valencia, Spain."
            ),
            bio_section(
                bio_year("2020"),
                "Finished the baccalaureate of science."
            ),
            bio_section(
                bio_year("2022"),
                "Completed higher degree of administration of computer network systems at IES Abastos."
            ),
            bio_section(
                bio_year("2022 to present"),
                "Working in ",
                rx.link(
                    "Laberit",
                    href="https://www.laberit.com/",
                    passHref=True,
                    scroll="false",
                    fontWeight="bold"
                ),
                "."
            ),
            pt="1em",
            pb="1em"
        )
    )
