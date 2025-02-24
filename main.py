import tkinter as tk
from tkinter import ttk
# -------------------------------------------------------------------
def start_terminal():
    """Käynnistää terminaalin ja luo tyylit widgeteille"""
    # Luo ruudun ja antaa sille yläpalkkiin nimen
    root = tk.Tk()
    root.title("Hue Peli")

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
    style.configure("white.TLabel", foreground = "white", background = "#000066", font = ("Helvetica", 11))
    style.configure("white2.TLabel", foreground = "white", background = "#000066", font = ("Helvetica", 30))
    
    style.configure("blue.TFrame", background = "#000066")

    style.configure("bw.TButton", foreground = "white", background = "#000066", borderwidth = 3, \
                    relief="raised", font = ("Helvetica", 11))
    style.configure("bw2.TButton", foreground = "white", background = "#000066", borderwidth = 1, \
                    relief="raised", font = ("Helvetica", 9))
    
    style.configure("bw.TEntry", foreground = "white", fieldbackground = "#000066", \
                    insertcolor = "white", font = ("Helvetica", 10))
    
    style.configure("bw.TCombobox", foreground = "#000066", font = ("Helvetica", 10))
    
    return root
# -------------------------------------------------------------------
from layout import create_start
original_y_coord = 0
moves_done = 0

# Käynnistetään terminaali
root = start_terminal()
create_start(root)

