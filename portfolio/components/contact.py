import reflex as rx
from portfolio.constants import MAIL
from portfolio.state.state import ClipboardState

def contact() -> rx.Component:
    return rx.container(
        rx.box(
            rx.heading(
                "@Contact",
                as_="h2",
                fontSize="2em",
                variant="section-title",
                textDecorationThickness="2.5px",
                fontWeight="bold",
                pb="2"
            ),
            rx.box(
                rx.box(
                    rx.input(
                        id="mail",
                        is_read_only=True,
                        class_name="text-lg bg-transparent w-full",
                        value="kaidewu@outlook.es"
                    ),
                    rx.tooltip(
                        rx.link(
                            rx.button(
                                rx.icon(tag="email", height="40px", width="28px")
                            ),
                            href=f"mailto:{MAIL}",
                            ml="3"  
                        ),
                        label="Open mail",
                        has_arrow=True
                    ),
                    as_="article",
                    class_name="col-span-3 xl:col-span-2 w-full overflow-hidden line-clamp-1",
                    display="inline-flex",
                    align_items="center"
                ),
                rx.box(
                    rx.link(
                        rx.image(
                            src="/Icons/GithubIcon.svg", 
                            h="7",
                            w="8",
                            display="inline-flex", 
                            pr="0.5", 
                            alignItems="center"
                        ),
                        "@kaidewu",
                        href="https://github.com/kaidewu/",
                        scroll="false",
                        p="3",
                        _hover={
                            "textDecoration": "underline"
                        },
                        font_size="17",
                        is_external=True
                    ),
                ),
                class_name="grid grid-cols-2 flex-wrap md:flex-nowrap items-center gap-3"
            )
        ),
        delay="0.1",
        pt="10",
        pb="10"
    )