import tkinter as tk
from tkinter import ttk
# -------------------------------------------------------------------
def create_frame(root):
    """Luo framen ja reunukset"""
    # Luo frame widgetin (padding = (left, top, right, bottom), jottei muut framet näy alta)
    frame = ttk.Frame(root, width=400, height=400, style = "blue.TFrame", padding = f"100 100 100 100")
    frame.grid(column = 0, row = 0)

    # Makes the frame expand to fill any extra space if the window is resized
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)

    return frame
# -------------------------------------------------------------------
def create_label(frame, teksti, tyyli, pystyrivi, vaakarivi, x_left, x_right, y_up, y_down):
    """Luo teksti-labelin ja asettaa sen frameen"""

    ttk.Label(frame, text = teksti, style = tyyli) \
        .grid(column = pystyrivi, row = vaakarivi, columnspan = 1, padx = [x_left, x_right], pady = [y_up, y_down])
# -------------------------------------------------------------------
def create_button(frame, teksti, tyyli, funktio, pystyrivi, vaakarivi, x_left, x_right, y_up, y_down):
    """Luo buttonin ja asettaa sen frameen"""

    ttk.Button(frame, text = teksti, style = tyyli, command = funktio) \
        .grid(column = pystyrivi, row = vaakarivi, columnspan = 1, rowspan = 1, \
              padx = [x_left, x_right], pady = [y_up, y_down])
# -------------------------------------------------------------------
def create_entry(frame, teksti_muuttuja, pystyrivi, vaakarivi, x_left, x_right, y_up, y_down):
    """Luo entry-kirjoituspalkin ja asettaa sen frameen"""

    entry = ttk.Entry(frame, textvariable = teksti_muuttuja, width = 20, style = "bw.TEntry")
    entry.grid(column = pystyrivi, row = vaakarivi, columnspan = 1, padx = [x_left, x_right], pady = [y_up, y_down])
    return entry
# -------------------------------------------------------------------