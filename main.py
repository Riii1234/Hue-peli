import tkinter as tk
from tkinter import ttk
# -------------------------------------------------------------------
def start_terminal():
    """Käynnistää terminaalin ja luo tyylit widgeteille"""
    # Luo ruudun ja antaa sille yläpalkkiin nimen
    root = tk.Tk()
    root.title("Hue-Peli")

    # Ruudun aloituskoko ja taustaväri
    root.geometry("600x600+0+0")
    root.configure(bg = "#000066")

    # Tekee reunukset
    root['borderwidth'] = 2
    root['relief'] = 'sunken'

    # Antaa columneille ja row:eille painoa, jotta asiat saadaan keskitettyä
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Mahdollistaa ruudun koon muuttamisen
    root.resizable(1, 1)
    
    # Mahdollistaa tyylien käyttämisen
    style = ttk.Style()
    # Printtaa mahdolliset teemat
    print(style.theme_names())
    # Valitsee käytettävän teeman (vaikuttaa nappuloiden ja palkkien reunoihin etc.)
    style.theme_use("default")

    # Luodaan tyylejä käytettäville widgeteille (label, frame, button, entry) 
    # Nimen (esim. "white.TLabel") jälkimmäistä osaa ei voi vaihtaa
    style.configure("blue.TLabel", foreground = "white", background = "#000066", font = ("Helvetica", 11))
    style.configure("blue2.TLabel", foreground = "white", background = "#000066", font = ("Helvetica", 30))
    style.configure("blue3.TLabel", foreground = "white", background = "#000066", font = ("Helvetica", 26))
    style.configure("white.TLabel", foreground = "#000066", background = "white", font = ("Helvetica", 11))
    
    style.configure("blue.TFrame", background = "#000066")
    style.configure("white.TFrame", background = "white")
    style.configure("blue2.TFrame", background = "#000066")

    style.configure("blue.TButton", foreground = "white", background = "#000066", borderwidth = 3, \
                    relief="raised", font = ("Helvetica", 11))
    style.configure("blue2.TButton", foreground = "white", background = "#000066", borderwidth = 1, \
                    relief="raised", font = ("Helvetica", 9))
    style.configure("blue3.TButton", foreground = "white", background = "#000066", borderwidth = 1, \
                    relief="raised", font = ("Helvetica", 17))
    style.configure("blue4.TButton", foreground = "white", background = "#000088", borderwidth = 1, \
                    relief="raised", font = ("Helvetica", 9))
    
    style.configure("blue.TEntry", foreground = "white", fieldbackground = "#000066", \
                    insertcolor = "white", font = ("Helvetica", 10))
    
    style.configure("blue.TCombobox", foreground = "#000066", font = ("Helvetica", 10))
    
    return root
# -------------------------------------------------------------------
# Käynnistetään terminaali
root = start_terminal()

from layout import create_start

create_start(root)

