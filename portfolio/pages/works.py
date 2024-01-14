import reflex as rx


from portfolio.components.layout.main import main
from portfolio.components.paragraph import paragraph
from portfolio.components.bio import bio_section, bio_year
from portfolio.components.project_title import project_title

def works() -> rx.Component:
    return main(
        rx.container(
            project_title(name="WORKS"),
            rx.heading(
                "Works",
                as_="h2",
                fontSize="2em",
                variant="section-title",
                text_decoration="underline",
                fontWeight="bold",
                pt="5",
                pb="2"
            ),
            paragraph(
                "Currently employed as an Implantation Consultant for Hospital Information Systems (HIS) at ",
                rx.link(
                    "Laberit",
                    href="https://www.laberit.com/",
                    passHref=True,
                    scroll="false",
                    fontWeight="bold",
                    is_external=True
                ),
                ", responsible for seamlessly integrating and configuring HIS solutions within healthcare organizations like ",
                rx.link(
                    "IVO",
                    href="https://www.ivo.es/",
                    passHref=True,
                    scroll="false",
                    fontWeight="bold",
                    is_external=True
                ),
                ", ",
                rx.link(
                    "HCB",
                    href="https://hcbhospitales.com/",
                    passHref=True,
                    scroll="false",
                    fontWeight="bold",
                    is_external=True
                ),
                ", ",
                rx.link(
                    "Premium Madrid",
                    href="https://rehabilitacionpremiummadrid.com/",
                    passHref=True,
                    scroll="false",
                    fontWeight="bold",
                    is_external=True
                ),
                " and ",
                rx.link(
                    "Ascires",
                    href="https://www.ascires.com/",
                    passHref=True,
                    scroll="false",
                    fontWeight="bold",
                    is_external=True
                ),
                "."
            ),
            pt="1em",
            pb="1em"
        ),
        rx.container(
            rx.heading(
                "Bio",
                as_="h2",
                fontSize="2em",
                variant="section-title",
                text_decoration="underline",
                fontWeight="bold",
                pt="5",
                pb="2"
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
                "Completed higher degree of administration of computer network systems in IES Abastos."
            ),
            bio_section(
                bio_year("2022 to present"),
                "Working in ",
                rx.link(
                    "Laberit",
                    href="https://www.laberit.com/",
                    passHref=True,
                    scroll="false",
                    fontWeight="bold",
                    is_external=True
                ),
                "."
            ),
            pt="1em",
            pb="1em"
        )
    )
