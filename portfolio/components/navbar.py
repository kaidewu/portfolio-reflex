import reflex as rx

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
                
                direction=['row'],
                display={'base': 'none', 'md': 'flex'},
                width={'base': 'full', 'md': 'auto'},
                align_items="center",
                flexGrow="1",
                mt={'base': 4, 'md': 0}
            ),
            rx.box(
                rx.link(
                    "Works",
                    href="/works",
                    scroll="false",
                    p="3",
                    _hover={
                        "textDecoration": "underline"
                    }
                ),
                rx.link(
                    rx.image(
                        src="/Icons/GithubIcon.svg", 
                        height="1.2em", 
                        display="inline-flex", 
                        pr="0.5", 
                        alignItems="center"
                    ),
                    "Source",
                    href="https://github.com/kaidewu/portfolio-reflex",
                    scroll="false",
                    p="3",
                    _hover={
                        "textDecoration": "underline"
                    },
                    is_external=True
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
                                rx.menu_item(
                                    rx.image(src="/Icons/GithubIcon.svg", height="0.9em", display="inline-flex", pr="0.5", alignItems="center"),
                                    "Source"
                                ),
                                href="https://github.com/kaidewu/portfolio-reflex",
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
                align="center",
                justify="space-between",
                display="flex",
                pt="2"
            ),
            display="flex",
            p="2",
            maxW="container.sm",
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