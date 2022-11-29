import unittest
from ui.myyja_view import *
from ui.opiskelija_view import *
from ui.user_select import UserSelect

from tkinter import Tk
from ui.ui import UI


class TestGeneralWindowSettings(unittest.TestCase):

    def setUp(self):
        self.window = Tk()
        self.window.title("Merkkien hallinta sovellus test")
        self.window.geometry("500x500")

        self.ui_view = UI(self.window)
        self.ui_view.start()
        print(self.ui_view)

    def test_window_title(self):
        self.assertEqual(self.window.title(),
                         "Merkkien hallinta sovellus test")

    def test_window_size(self):
        # beacause window is neve spawned so it's size is 0,0
        self.assertEqual(self.window.size(), (0, 0))
