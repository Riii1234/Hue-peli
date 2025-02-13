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
    
    return root
# -------------------------------------------------------------------
from layout_common_functions import create_frame, create_label, create_entry, create_button, \
    on_click, on_drag, on_release
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

    if level_number == "Easy 1":
        locked, game_pieces = create_level_easy_1(canvas)

    # Bindataan hiiren painallus, vetäminen ja irti-päästäminen eventteihin
    canvas.bind("<Button-1>", lambda event:on_click(event, canvas))
    canvas.bind("<B1-Motion>", lambda event:on_drag(event, canvas, locked))
    canvas.bind("<ButtonRelease-1>", lambda event:on_release(event, canvas, locked))
# -------------------------------------------------------------------
def create_level_easy_1(canvas):
    """Luodaan easy level 1"""

    colors = ["#FFB4B4", "#FF9B9B", "#FF8282", "#FF6969", "#FF5050", "#FF3737", "#FF1E1E",\
              "#FF0505", "#EB0000", "#D20000", "#B90000"]
    # r_15, r_20, r_25, r_30, r_35, r_40, r_45, r_50, r_55, r_60, r_65

    game_pieces = create_level(canvas, 100, 40, 400, 80, colors)

    # Luodaan pisteet lukossa oleville palikoille
    dot1 = canvas.create_oval(248, 58, 252, 62, tags = "point", fill = "black")
    dot2 = canvas.create_oval(248, 458, 252, 462, tags = "point", fill = "black")

    # Palauttaa listassa lukossa olevat
    return ([1, 11, 12, 13], game_pieces)
# -------------------------------------------------------------------
def create_level(canvas, x1, y1, x2, y2, colors):
    """Luodaan levelin palikat"""
    game_pieces = []

    for i in range(len(colors)):
        # x1, y1 = vasen yläkulma, x2, y2 = oikea alakulma, width on reunukset
        piece = canvas.create_rectangle(x1, y1, x2, y2, fill = colors[i], width = 0)
        y1 += 40
        y2 += 40
        game_pieces.append(piece)

    return game_pieces
# -------------------------------------------------------------------
original_y_coord = 0
# Käynnistetään terminaali
root = start_terminal()
create_start(root)

