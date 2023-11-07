import reflex as rx

from portfolio.constants import GITHUB_PORTFOLIO_REFLEX_URL
from portfolio.components.logo import logo

def navbar() -> rx.Component:
    return rx.box(
        rx.container(
            rx.flex(
                rx.heading(
                    logo(),
                    as_="h1",
                    size="lg",
                    letterSpacing="tighter"
                ),
                align="center",
                mr="5"
            ),
            rx.stack(
                rx.link(
                    "Works",
                    href="/works",
                    scroll="false",
                    p="3",
                    _hover={
                        "textDecoration": "underline",
                        "top": "-10px",
                        "position": "relative"
                    }
                ),
                rx.link(
                    "Projects",
                    href="/projects",
                    scroll="false",
                    p="3",
                    _hover={
                        "textDecoration": "underline",
                        "top": "-10px",
                        "position": "relative"
                    }
                ),
                rx.link(
                    "Contact",
                    href="/contact",
                    scroll="false",
                    p="3",
                    _hover={
                        "textDecoration": "underline",
                        "top": "-10px",
                        "position": "relative"
                    }
                ),
                rx.link(
                    rx.image(src="/Icons/GithubIcon.svg", height="1.2em", display="inline-flex", pr="0.5", alignItems="center"),
                    "Source",
                    href=GITHUB_PORTFOLIO_REFLEX_URL,
                    scroll="false",
                    p="3",
                    _hover={
                        "textDecoration": "underline",
                        "top": "-10px",
                        "position": "relative"
                    },
                    is_external=True
                ),
                direction="row",
                display={'base': 'none', 'md': 'flex'},
                width={'base': 'full', 'md': 'auto'},
                pt="5px",
                flexGrow="1",
                mt={'base': 4, 'md': 0}
            ),
            rx.box(
                rx.box(
                    rx.color_mode_button(
                        rx.color_mode_icon(),
                        _hover={
                            "transform": "translateY(5px)",
                            "transition": "transform 1s ease-in-out"
                        }
                    ),
                    style={
                        "display": "inline-block",
                    }
                ),
                rx.box(
                    rx.menu(
                        rx.menu_button(
                            rx.icon(tag="hamburger"),
                            as_="IconButton",
                            variant="outline",
                            aria_label="Options"
                        ),
                        rx.menu_list(
                            rx.link(
                                rx.menu_item("Works"),
                                href="/works"
                            ),
                            rx.link(
                                rx.menu_item("Projects"),
                                href="/projects"
                            ),
                            rx.link(
                                rx.menu_item("Contact"),
                                href="/contact"
                            ),
                            rx.link(
                                rx.menu_item("Source"),
                                href=GITHUB_PORTFOLIO_REFLEX_URL,
                                is_external=True
                            )
                        ),
                        is_lazy=True,
                        id="navbar-menu"
                    ),
                    ml="2",
                    display={'base': 'inline-block', 'md': 'none'}
                ),
                flex="1",
                align="right",
                pt="5"
            ),
            display="flex",
            p="2",
            maxW="container.md",
            wrap="wrap",
            align="center",
            justify="space-between"
        ),
        position="fixed",
        w="100%",
        as_="nav",
        backdropFilter="blur(5px)",
        zIndex="2"
    )