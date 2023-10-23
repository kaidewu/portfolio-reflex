import reflex as rx

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
                    f"© {date.today().year} Kaide Wu. All rights Reserved.",
                    style=footer_item_style,
                ),
                rx.hstack(
                    rx.link(
                        rx.image(src="/Icons/GithubIcon.svg", height="1.75em"),
                        href="https://github.com/kaidewu",
                    ),
                    rx.link(
                        rx.image(src="/Icons/LinkedinIcon.svg", height="1.75em"),
                        href="https://linkedin.com/in/kaidewu",
                    ),
                    rx.link(
                        rx.icon(tag="email", height="40px", width="28px"),
                        href="mailto:kaidewu@outlook.es",
                    ),
                    spacing="1em",
                ),
                justify="space-between",
                padding_bottom="2em",
                min_width="100%",
            ),
        ),
        **style,
    )