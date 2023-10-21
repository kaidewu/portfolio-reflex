import reflex as rx

import os

def logo():
    return rx.link(
        rx.box(
            rx.image(
                src=os.getenv("PROFILE_URL"),
                alt="Profile Image",
                borderRadius="full",
                html_width="40",
                html_height="40",
                _hover={
                    "transform": "rotate(360deg)",
                    "transition": "transform 0.5s ease-in-out"
                }
            ),
            rx.text(
                "Kaide Wu",
                fontFamily="M PLUS Rounded 1c"", sans-serif",
                fontWeight="bold",
                ml={3}
            ),
            style={
                "font-weight": "bold",
                "font-size": "10 px",
                "align-items": "center",
                "padding": "30px",
                "line-height": "20px",
                "height": "10px",
                "display": "inline-flex"
            }
        ),
        href="/",
        scroll={False}
    )