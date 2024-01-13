import reflex as rx

def logo():
    return rx.link(
        rx.box(
            rx.icon(
                tag="moon"
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