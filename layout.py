import tkinter as tk
from tkinter import ttk
# -------------------------------------------------------------------
from layout_common_functions import create_frame, create_label, create_entry, create_button, \
    on_click, on_drag, on_release
from levels import *
# -------------------------------------------------------------------
def create_start(root):
    """Luo starting-välilehden ja nostaa sen esille"""

    # Luo aloitus-framen eli välilehden, johon voidaan sijoittaa widgetit
    starting_frame = create_frame(root)

    create_starting_frame(starting_frame, root)

    # Aloitus-frame (mikä näkyy käynnistettäessä)
    starting_frame.tkraise()
    
    # Ohjelman aloitus
    root.mainloop()
# -------------------------------------------------------------------
def create_starting_frame(starting_frame, root):
    """Luo starting-välilehden sisällön"""

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

    create_button(starting_frame, "Start Game", "bw.TButton", lambda:create_level_frame(root), 1, 8, 1, 1, 10, 1)
# -------------------------------------------------------------------
def create_user():
    print("Created user!")
# -------------------------------------------------------------------
def delete_user():
    pass
# -------------------------------------------------------------------
def create_level_frame(root):
    """Luo level-välilehden ja sen sisällön"""
    level_frame = create_frame(root)
    level_frame.tkraise()

    create_label(level_frame, "Easy", "white.TLabel", 2, 3, 1, 1, 10, 5)
    create_levels(level_frame, root, "Easy", 1, 4)

    create_label(level_frame, "Medium", "white.TLabel", 2, 6, 1, 1, 10, 5)
    create_levels(level_frame, root, "Medium", 1, 7)

    create_label(level_frame, "Hard", "white.TLabel", 2, 9, 1, 1, 10, 5)
    create_levels(level_frame, root, "Hard", 1, 10)
# -------------------------------------------------------------------
def create_levels(level_frame, root, difficulty, pystyrivi, vaakarivi):
    
    create_button(level_frame, "1", "bw2.TButton", lambda:start_level(root, f"{difficulty} 1"), \
                  pystyrivi, vaakarivi, 1, 1, 1, 1)
    create_button(level_frame, "2", "bw2.TButton", lambda:start_level(root, f"{difficulty} 2"), \
                  pystyrivi+1, vaakarivi, 1, 1, 1, 1)
    create_button(level_frame, "3", "bw2.TButton", lambda:start_level(root, f"{difficulty} 3"), \
                  pystyrivi+2, vaakarivi, 1, 1, 1, 1)
# -------------------------------------------------------------------
def start_level(root, level_number):
    """Luo game-välilehden ja sen sisällön"""

    game_frame = create_frame(root)
    game_frame.tkraise()

    # create_label(frame, teksti, tyyli, pystyrivi, vaakarivi, x_left, x_right, y_up, y_down)
    create_label(game_frame, f"Level {level_number}", "white.TLabel", 0, 1, 1, 1, 5, 40)

    # Luodaan canvas, jolle voidaan piirtää kuvoita/kuvia ja liikuttaa niitä
    canvas = tk.Canvas(game_frame, height = 500, width = 490, highlightthickness = 1, bg = "#000066")
    canvas.grid(column = 0, row = 2, columnspan = 10, rowspan = 10, padx = [1, 1], pady = [1, 1])

    from color_dict import colors_dict

    if level_number == "Easy 1":
        locked = create_level_easy_1(canvas, colors_dict)

    # Bindataan hiiren painallus, vetäminen ja irti-päästäminen eventteihin
    canvas.bind("<Button-1>", lambda event:on_click(event, canvas))
    canvas.bind("<B1-Motion>", lambda event:on_drag(event, canvas, locked))
    canvas.bind("<ButtonRelease-1>", lambda event:on_release(event, canvas, locked))
# -------------------------------------------------------------------

