import reflex as rx

def logo():
    return rx.link(
        rx.box(
            rx.image(
                src="https://media.licdn.com/dms/image/D4D03AQHJJfsn_R49gQ/profile-displayphoto-shrink_800_800/0/1697579468200?e=2147483647&v=beta&t=F_maiaDdmKe7klM6ltl3ivTEGHKWTNwMkhwylivvniI",#"images/kaide's photo.jpeg",
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