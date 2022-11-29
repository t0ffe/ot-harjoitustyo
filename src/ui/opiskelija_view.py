from tkinter import ttk, constants


class Opiskleija_view:
    def __init__(self, root):
        self._root = root
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        wip = ttk.Label(master=self._frame, text="OPISKELIJA NÄKYMÄ WIP")

        self._frame.grid_columnconfigure(0, weight=1)

        wip.grid(padx=5, pady=5, sticky=constants.EW)
