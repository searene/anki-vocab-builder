from typing import Callable

from vocab_builder.anki.IAnkiService import IAnkiService
import aqt
from anki.notes import Note


class DefaultAnkiService(IAnkiService):

    def show_add_card_dialog(self) -> None:
        aqt.mw.onAddCard()

    def show_tooltip(self, tooltip: str) -> None:
        aqt.utils.tooltip("The word has been copied into the clipboard.", 3000)

    def add_to_did_add_note_hook(self, callback: Callable[[Note], None]) -> None:
        aqt.gui_hooks.add_cards_did_add_note.append(callback)

    def remove_did_add_note_hood(self, callback: Callable[[Note], None]) -> None:
        aqt.gui_hooks.add_cards_did_add_note.remove(callback)
