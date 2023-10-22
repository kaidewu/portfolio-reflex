import reflex as rx

def work_item(id: str, title: str, thumbnail: str, description: str) -> rx.Component:
    return rx.box(
        rx.link_box(
            rx.image(
                src=thumbnail,
                alt=title,
                class_name="grid-item-thumbnail",
                placeholder="blur"
            ),
            rx.link_overlay(
                rx.text(
                    title,
                    mt={2},
                    fontSize={20}
                ),
                as_="div",
                href=f"/works/{id}"
            ),
            rx.text(
                description,
                fontSize={14}
            ),
            scroll=False,
            cursor="pointer",
            href=f"/works/{id}"
        ),
        w="100%",
        textAlign="center"
    )