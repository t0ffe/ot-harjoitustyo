from tkinter import ttk, constants


class UserSelect:
    """Käyttäjän valitsemisesta vastaava näkymä."""

    def __init__(self, root, show_opiskelija_view, show_myyja_view):

        self._root = root
        self._frame = None
        self._show_opiskelija_view = show_opiskelija_view
        self._show_myyja_view = show_myyja_view

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        end_user = ttk.Button(
            master=self._frame,
            text="Opiskelija",
            command=self._handle_opiskelija
        )
        merchant = ttk.Button(
            master=self._frame,
            text="Myyjä",
            command=self._handle_myyja
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        end_user.grid(padx=5, pady=5, sticky=constants.EW)
        merchant.grid(padx=5, pady=5, sticky=constants.EW)

    def _handle_opiskelija(self):
        self._show_opiskelija_view()

    def _handle_myyja(self):
        self._show_myyja_view()
