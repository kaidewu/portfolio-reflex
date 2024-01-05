import reflex as rx

from portfolio.constants import GITHUB_URL, LINKEDIN_URL, MAIL
from datetime import date

footer_item_style = {
    "font_weight": "500",
}

footer_style = {
    "vertical_align": "bottom",
    "padding_top": "4em",
    "padding_bottom": "2em",
}

def footer(style=footer_style) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.text(
                    f"Copyright © {date.today().year} Kaide Wu",
                    style=footer_item_style,
                ),
                rx.hstack(
                    rx.link(
                        rx.image(src="/Icons/GithubIcon.svg", height="1.75em"),
                        href=GITHUB_URL,
                        is_external=True
                    ),
                    rx.link(
                        rx.image(src="/Icons/LinkedinIcon.svg", height="1.75em"),
                        href=LINKEDIN_URL,
                        is_external=True
                    ),
                    rx.link(
                        rx.icon(tag="email", height="40px", width="28px"),
                        href=f"mailto:{MAIL}"
                    ),
                    spacing="1em",
                ),
                justify="space-between",
                padding_bottom="2em",
                min_width="100%",
            ),
        ),
        **style,
        as_="footer",
        textAlign="center"
    )