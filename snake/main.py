import tkinter as tk
from tkinter.colorchooser import askcolor
from tkinter import ttk

from utils.tk_crutch.basic_component import BasicWindow
from utils.tk_crutch.style import *
from utils.tk_crutch.tools import specs
from utils.tk_crutch.constants import MouseEvent


class PromptDialogToplevel(tk.Toplevel):

    def __init__(self, master=None, cnf=None, **kw):
        if cnf is None:
            cnf = {}
        super().__init__(master, cnf, **kw)
        specs(self)
        self.title("警告")
        self.init_page()

    def init_page(self):
        tk.Label(
            self, text="hello", font=default_font
        ).pack()

        combobox = ttk.Combobox(self, value=('下拉选项1', '下拉选项2', '下拉选项3', '下拉选项4'))
        combobox.current(2)
        combobox.pack()
        tk.Message()


class MainFrame(tk.Frame):

    def __init__(self, master=None, cnf=None, **kw):
        if cnf is None:
            cnf = {}
        super().__init__(master, cnf, **kw)
        self.init_page()

    @staticmethod
    def handle_hello_click():
        color = askcolor()
        print(color)
        print("hello")

    @staticmethod
    def handle_dialog_click():
        PromptDialogToplevel()

    def init_page(self):
        tk.Button(
            self, cnf=primary_button_cnf, text="按 钮", command=self.handle_hello_click
        ).pack(
            cnf=float_left_px10_pack_cnf
        )

        tk.Button(
            self, cnf=primary_button_cnf, text="弹 窗", command=self.handle_dialog_click
        ).pack(
            cnf=float_left_px10_pack_cnf
        )


class MainWindow(BasicWindow):

    def __init__(self):
        super().__init__()
        self.set_specs()
        self.title("GUI应用")
        self.init_page()
        self.mainloop()

    def init_page(self):
        print(self.maxsize())
        self.bind("<Any-Button>", lambda e: self.destroy())
        MainFrame().pack()
        self.state()
        self.protocol()


if __name__ == '__main__':
    MainWindow()
