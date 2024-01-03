import os

from tkinter import *
from tkinter.ttk import Frame, Scrollbar


# A canvas widget with scroll bars and some useful bindings


def wheel_event(event, widget=None):
    """Handle scrollwheel event.

    For wheel up, event.delta = 120*n on Windows, -1*n on darwin,
    where n can be > 1 if one scrolls fast.  Flicking the wheel
    generates up to maybe 20 events with n up to 10 or more 1.
    Macs use wheel down (delta = 1*n) to scroll up, so positive
    delta means to scroll up on both systems.

    X-11 sends Control-Button-4,5 events instead.

    The widget parameter is needed so browser label bindings can pass
    the underlying canvas.

    This function depends on widget.yview to not be overridden by
    a subclass.
    """
    up = {EventType.MouseWheel: event.delta > 0,
          EventType.ButtonPress: event.num == 4}
    lines = -5 if up[event.type] else 5
    widget = event.widget if widget is None else widget
    widget.yview(SCROLL, lines, 'units')
    return 'break'


class ScrolledCanvas:

    def __init__(self, master, **opts):
        if 'yscrollincrement' not in opts:
            opts['yscrollincrement'] = 17
        self.master = master
        self.frame = Frame(master)
        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.canvas = Canvas(self.frame, **opts)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.vbar = Scrollbar(self.frame, name="vbar")
        self.vbar.grid(row=0, column=1, sticky="nse")
        self.hbar = Scrollbar(self.frame, name="hbar", orient="horizontal")
        self.hbar.grid(row=1, column=0, sticky="ews")
        self.canvas['yscrollcommand'] = self.vbar.set
        self.vbar['command'] = self.canvas.yview
        self.canvas['xscrollcommand'] = self.hbar.set
        self.hbar['command'] = self.canvas.xview
        self.canvas.bind("<Key-Prior>", self.page_up)
        self.canvas.bind("<Key-Next>", self.page_down)
        self.canvas.bind("<Key-Up>", self.unit_up)
        self.canvas.bind("<Key-Down>", self.unit_down)
        self.canvas.bind("<MouseWheel>", wheel_event)
        self.canvas.bind("<Button-4>", wheel_event)
        self.canvas.bind("<Button-5>", wheel_event)
        # if isinstance(master, Toplevel) or isinstance(master, Tk):
        # self.canvas.bind("<Alt-Key-2>", self.zoom_height)
        self.canvas.focus_set()

    def page_up(self, event):
        self.canvas.yview_scroll(-1, "page")
        return "break"

    def page_down(self, event):
        self.canvas.yview_scroll(1, "page")
        return "break"

    def unit_up(self, event):
        self.canvas.yview_scroll(-1, "unit")
        return "break"

    def unit_down(self, event):
        self.canvas.yview_scroll(1, "unit")
        return "break"
    # def zoom_height(self, event):
    #     zoomheight.zoom_height(self.master)
    #     return "break"
