import reflex as rx
from portfolio.constants import PROFILE_URL

def logo():
    return rx.link(
        rx.box(
            rx.image(
                src="/profile_image.jpg",
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
                style={
                    "font-family": "'Inter', sans-serif",
                    "font-family": "'Playfair Display', serif"
                },
                fontWeight="bold",
                fontSize="20",
                ml="3"
            ),
            fontWeight="bold",
            fontSize="10",
            alignItems="center",
            p="30",
            h="10",
            display="inline-flex",
            lineHeight="10"
        ),
        href="/",
        scroll="false"
    )