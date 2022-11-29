from ui.user_select import UserSelect
from ui.myyja_view import Myyja_view
from ui.opiskelija_view import Opiskleija_view


class UI:
    """Sovelluksen käyttöliittymästä vastaava luokka."""

    def __init__(self, root):

        self._root = root
        self._current_view = None

    def start(self):
        self._show_user_select()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_user_select(self):
        self._hide_current_view()

        self._current_view = UserSelect(
            self._root,
            self._show_opiskelija_view,
            self._show_myyja_view
        )

        self._current_view.pack()

    def _show_myyja_view(self):
        self._hide_current_view()

        self._current_view = Myyja_view(
            self._root
        )

        self._current_view.pack()

    def _show_opiskelija_view(self):
        self._hide_current_view()

        self._current_view = Opiskleija_view(
            self._root
        )

        self._current_view.pack()
