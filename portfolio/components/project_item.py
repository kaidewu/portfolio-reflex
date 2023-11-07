import reflex as rx

def project_item(id: str, title: str, thumbnail: str, description: str) -> rx.Component:
    return rx.link(
        rx.link_box(
            rx.box(
                rx.image(
                    id="project_image",
                    src=thumbnail,
                    alt=title,
                    class_name="grid-item-thumbnail",
                    placeholder="blur"
                ),
                rx.box(
                    rx.text(
                        title,
                        id="project_title",
                        mt="2",
                        fontSize="20",
                        textColor="white"
                    ),
                    rx.text(
                        description,
                        id="project_description",
                        textColor="white"
                    ),
                    id="info"
                ),
            id="project_card",
        ),
        id="project_wrapper"
    ),
    scroll="false",
    cursor="pointer",
    href=f"/projects/{id}"
)