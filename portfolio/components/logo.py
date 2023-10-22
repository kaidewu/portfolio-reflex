import reflex as rx

import os

def logo():
    return rx.link(
        rx.box(
            rx.image(
                src=os.getenv("PROFILE_URL") if os.getenv("PROFILE_URL") is not None else "",
                alt="Profile Image",
                borderRadius="full",
                html_width="50",
                html_height="50",
                _hover={
                    "transform": "rotate(360deg)",
                    "transition": "transform 0.5s ease-in-out"
                }
            ),
            rx.text(
                "Kaide Wu",
                fontFamily="M PLUS Rounded 1c"", sans-serif",
                fontWeight="bold",
                fontSize={20},
                ml={3}
            ),
            fontWeight="bold",
            fontSize={10},
            alignItems="center",
            p={30},
            h={10},
            display="inline-flex",
            lineHeight={20}
        ),
        href="/",
        scroll={False}
    )