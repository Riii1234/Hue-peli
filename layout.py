import tkinter as tk
from tkinter import ttk
# -------------------------------------------------------------------
def start_terminal():
    """Käynnistää terminaalin ja luo tyylit widgeteille"""
    # Luo ruudun ja antaa sille yläpalkkiin nimen
    root = tk.Tk()
    root.title("Hue Peli")

    # Ruudun aloituskoko ja taustaväri
    root.geometry("500x500+0+0")
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
    
    return root
# -------------------------------------------------------------------
from layout_common_functions import create_frame, create_label, create_entry, create_button
# -------------------------------------------------------------------
def create_start(root):
    """Luo välilehdet ja niiden sisällön"""

    # Luo aloitus-framen eli välilehden, johon voidaan sijoittaa widgetit
    starting_frame = create_frame(root)

    create_starting_frame(starting_frame)

    # Aloitus-frame (mikä näkyy käynnistettäessä)
    starting_frame.tkraise()
    
    # Ohjelman aloitus
    root.mainloop()
# -------------------------------------------------------------------
def create_starting_frame(starting_frame):
    """Luo starting-välilehden ja sen sisällön"""

    # Luodaan teksti (frame, teksti, tyyli, pystyrivi, vaakarivi, x_left, x_right, y_up, y_down)
    # Widgetin alle saa tilaa lisäämällä y_down:ia ja ylle saa tilaa lisäämällä y_up:ia
    create_label(starting_frame, "Hue Peli", "white2.TLabel", 1, 1, 1, 1, 1, 40)

    create_label(starting_frame, "Username", "white.TLabel", 1, 2, 1, 1, 1, 5)

    # Luodaan teksti-muuttuja, joka muuttuu siksi mitä entryyn kirjoitetaan
    player_name = tk.StringVar()
    # Luodaan entry-kenttä, joka käyttää luotua teksti-muuttujaa
    player_entry = create_entry(starting_frame, player_name, 1, 3, 1, 1, 1, 10)

    # (frame, teksti, funktio (joka tapahtuu nappulasta) lambda-muodossa, jottei se tapahdu koko ajan, 
    # pystyrivi, vaakarivi, x_left, x_right, y_up, y_down)
    create_button(starting_frame, "Create New User", "bw.TButton", lambda:create_user(), 1, 4, 1, 1, 1, 10)
    create_button(starting_frame, "Delete User", "bw.TButton", lambda:delete_user(), 1, 6, 1, 1, 1, 10)

    create_button(starting_frame, "Start Game", "bw.TButton", lambda:create_level_frame(), 1, 8, 1, 1, 10, 1)
# -------------------------------------------------------------------
def create_user():
    print("Created user!")
# -------------------------------------------------------------------
def delete_user():
    pass
# -------------------------------------------------------------------
def create_level_frame():
    """Luo level-välilehden ja sen sisällön"""
    level_frame = create_frame(root)
    level_frame.tkraise()

    create_label(level_frame, "Easy", "white.TLabel", 2, 3, 1, 1, 10, 5)
    create_levels(level_frame, "1", 1, 4)

    create_label(level_frame, "Medium", "white.TLabel", 2, 6, 1, 1, 10, 5)
    create_levels(level_frame, "2", 1, 7)

    create_label(level_frame, "Hard", "white.TLabel", 2, 9, 1, 1, 10, 5)
    create_levels(level_frame, "3", 1, 10)
# -------------------------------------------------------------------
def create_levels(level_frame, difficulty, pystyrivi, vaakarivi):

    create_button(level_frame, f"{difficulty}.1", "bw2.TButton", lambda:start_level(f"{difficulty}.1"), \
                  pystyrivi, vaakarivi, 1, 1, 1, 1)
    create_button(level_frame, f"{difficulty}.2", "bw2.TButton", lambda:start_level(f"{difficulty}.2"), \
                  pystyrivi+1, vaakarivi, 1, 1, 1, 1)
    create_button(level_frame, f"{difficulty}.3", "bw2.TButton", lambda:start_level(f"{difficulty}.3"), \
                  pystyrivi+2, vaakarivi, 1, 1, 1, 1)
# -------------------------------------------------------------------
def start_level(level_number):

    game_frame = create_frame(root)
    game_frame.tkraise()

    create_label(game_frame, f"Level {level_number}", "white2.TLabel", 1, 2, 1, 1, 1, 40)

    # Luodaan canvas, jolle voidaan piirtää kuvoita/kuvia ja liikuttaa niitä
    canvas = tk.Canvas(game_frame, height = 400, width = 490, highlightthickness = 0, bg = "#000066")
    canvas.grid(column = 1, row = 3)

    figure1 = canvas.create_rectangle(80, 80, 120, 120, fill = "blue")


root = start_terminal()

create_start(root)



