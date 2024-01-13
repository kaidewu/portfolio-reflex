import reflex as rx
import asyncio
from reflex.vars import Var
from typing import Dict, Any

class State(rx.State):
    """The base state."""

    @rx.var
    def current_page(self) -> str:
        """The current page."""
        return self.router.page.full_path
    
class ClipboardState(State):
    """State for the clipboard."""

    # The copied text.
    text: str = ""

    def copy(self, text: str):
        """Set the text to copy.

        Args:
            text: The text to copy.
        """
        self.text = text

    async def reset_text(self):
        """Reset the copied text."""
        # Wait in order to show the toast.
        await asyncio.sleep(2)

        # Reset the text.
        self.reset()
        self.text = ""

class TypewriterLib(rx.Component):
    """ Typewriter component """

    library="typewriter-effect"
    
    is_default=True

class Typewriter(TypewriterLib):

    tag="Typewriter"

    options: Var[Dict[Any, Any]]
    
class CopyToClipboard(rx.Component):
    """Component to copy text to clipboard."""

    library = "react-copy-to-clipboard"

    tag = "CopyToClipboard"

    # The text to copy when clicked.
    text: rx.Var[str]

    @classmethod
    def get_triggers(cls) -> set[str]:
        return super().get_triggers() | {"on_copy"}


# Convenience method to create the compoennt.
copy_to_clipboard = CopyToClipboard.create

typewrite = Typewriter.create