import tkinter as tk
from tkinter import ttk
import globals
# -------------------------------------------------------------------
from color_dict import colors_dict
from layout_common_functions import create_frame, create_label, create_entry, create_button, create_combobox, \
    on_click, on_drag, on_release, set_combobox
from levels import *
import player_controls
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

    create_label(starting_frame, "Choose User", "white.TLabel", 1, 2, 1, 1, 1, 5)

    # Luodaan teksti-muuttuja
    current_player_name = tk.StringVar()
    # Luodaan valikko, joka käyttää luotua teksti-muuttujaa
    player_combobox = create_combobox(starting_frame, current_player_name, 1, 3, 1, 1, 1, 10)
    # Asettaa pelaaja-nimet valikkoon
    set_player_combobox(player_combobox)

    # (frame, teksti, funktio (joka tapahtuu nappulasta) lambda-muodossa, jottei se tapahdu koko ajan, 
    # pystyrivi, vaakarivi, x_left, x_right, y_up, y_down)
    create_button(starting_frame, "Create New User", "bw.TButton", lambda:create_user(root, player_combobox), 1, 4, 1, 1, 1, 10)
    create_button(starting_frame, "Delete User", "bw.TButton", lambda:delete_user(root, player_combobox), 1, 6, 1, 1, 1, 10)

    create_button(starting_frame, "Start Game", "bw.TButton", \
                  lambda:create_level_frame(root, starting_frame, current_player_name), 1, 8, 1, 1, 10, 1)
# -------------------------------------------------------------------
def set_player_combobox(player_combobox):
    """Täyttää pelaaja-nimi valikon tiedostosta"""

    player_infos_list = player_controls.player_data_loader()

    player_names = []

    for user in player_infos_list:
        player_names.append(user["username"])

    #print(player_names)
    set_combobox(player_combobox, player_names)
# -------------------------------------------------------------------
def get_player_name(current_player_name):
    """Palauttaa valitun pelaaja-nimen"""

    chosen_name = current_player_name.get()
    return chosen_name
# -------------------------------------------------------------------
def create_user(root, player_combobox):
    """Luo välilehden uuden pelaajan lisäämiselle"""

    player_creation_frame = ttk.Frame(root, width=200, height=200, style = "blue2.TFrame")
    player_creation_frame.grid(column = 0, row = 0)

    player_creation_frame.tkraise()

    # create_label(frame, teksti, tyyli, pystyrivi, vaakarivi, x_left, x_right, y_up, y_down)
    create_label(player_creation_frame, f"Create username (3 letters)", "white.TLabel", 0, 1, 10, 10, 100, 5)

    name_variable = tk.StringVar()
    name_entry = create_entry(player_creation_frame, name_variable, 0, 2, 10, 10, 5, 20)

    create_button(player_creation_frame, "Accept", "bw.TButton", \
                  lambda:player_controls.player_creation(player_creation_frame, name_variable, player_combobox), 0, 3, 1, 1, 10, 100)
# -------------------------------------------------------------------
def delete_user(root, player_combobox):
    """Luo välilehden uuden pelaajan poistamiseksi"""

    player_delete_frame = ttk.Frame(root, width=200, height=200, style = "blue2.TFrame")
    player_delete_frame.grid(column = 0, row = 0)

    player_delete_frame.tkraise()

    # create_label(frame, teksti, tyyli, pystyrivi, vaakarivi, x_left, x_right, y_up, y_down)
    create_label(player_delete_frame, f"Delete username (3 letters)", "white.TLabel", 0, 1, 10, 10, 100, 5)

    name_variable = tk.StringVar()
    name_entry = create_entry(player_delete_frame, name_variable, 0, 2, 10, 10, 5, 20)

    create_button(player_delete_frame, "Accept", "bw.TButton", \
                  lambda:player_controls.player_deletion(player_delete_frame, name_variable, player_combobox), 0, 3, 1, 1, 10, 100)
# -------------------------------------------------------------------
def create_level_frame(root, starting_frame, current_player_name):
    """Luo kentän valinta-välilehden"""

    chosen_name = get_player_name(current_player_name)
    print(chosen_name)

    if len(chosen_name) == 3:
        """Luo level-välilehden ja sen sisällön"""
        level_frame = create_frame(root)
        level_frame.tkraise()

        create_label(level_frame, "Easy", "white.TLabel", 2, 3, 1, 1, 10, 5)
        create_levels(level_frame, root, starting_frame, chosen_name, "Easy", 1, 4)

        create_label(level_frame, "Medium", "white.TLabel", 2, 6, 1, 1, 10, 5)
        create_levels(level_frame, root, starting_frame, chosen_name, "Medium", 1, 7)

        create_label(level_frame, "Hard", "white.TLabel", 2, 9, 1, 1, 10, 5)
        create_levels(level_frame, root, starting_frame, chosen_name, "Hard", 1, 10)
# -------------------------------------------------------------------
def create_levels(level_frame, root, starting_frame, chosen_name, difficulty, pystyrivi, vaakarivi):
    """Luo nappulat leveleille, eivät ole loopissa, koska se ei anna numeroinnin toimia"""
    
    create_button(level_frame, "1", "bw2.TButton", lambda:start_level(root, starting_frame, f"{difficulty} 1", chosen_name), \
                  pystyrivi, vaakarivi, 1, 1, 1, 1)
    create_button(level_frame, "2", "bw2.TButton", lambda:start_level(root, starting_frame, f"{difficulty} 2", chosen_name), \
                  pystyrivi+1, vaakarivi, 1, 1, 1, 1)
    create_button(level_frame, "3", "bw2.TButton", lambda:start_level(root, starting_frame, f"{difficulty} 3", chosen_name), \
                  pystyrivi+2, vaakarivi, 1, 1, 1, 1)
    create_button(level_frame, "4", "bw2.TButton", lambda:start_level(root, starting_frame, f"{difficulty} 4", chosen_name), \
                  pystyrivi+3, vaakarivi, 1, 1, 1, 1)
    create_button(level_frame, "5", "bw2.TButton", lambda:start_level(root, starting_frame, f"{difficulty} 5", chosen_name), \
                  pystyrivi+4, vaakarivi, 1, 1, 1, 1)
    create_button(level_frame, "6", "bw2.TButton", lambda:start_level(root, starting_frame, f"{difficulty} 6", chosen_name), \
                  pystyrivi+5, vaakarivi, 1, 1, 1, 1)
# -------------------------------------------------------------------
def start_level(root, starting_frame, level_name, chosen_name):
    """Luo game-välilehden ja sen sisällön"""

    game_frame = create_frame(root)
    game_frame.tkraise()

    # create_label(frame, teksti, tyyli, pystyrivi, vaakarivi, x_left, x_right, y_up, y_down)
    create_label(game_frame, f"Level {level_name}", "white.TLabel", 0, 1, 1, 1, 5, 40)

    # Luodaan canvas, jolle voidaan piirtää kuvoita/kuvia ja liikuttaa niitä
    canvas = tk.Canvas(game_frame, height = 500, width = 490, highlightthickness = 1, bg = "#000066")
    canvas.grid(column = 0, row = 2, columnspan = 10, rowspan = 10, padx = [1, 1], pady = [1, 1])

    globals.moves_done = 0
    #print("moves_done reset in start_level:", globals.moves_done)

    if level_name == "Easy 1":
        locked, original_colors, shuffled_colors, ori_shuffled_colors = create_level_easy_1(canvas, colors_dict)

    elif level_name == "Easy 2":
        locked, original_colors, shuffled_colors, ori_shuffled_colors = create_level_easy_2(canvas, colors_dict)

    elif level_name == "Easy 3":
        locked, original_colors, shuffled_colors, ori_shuffled_colors = create_level_easy_3(canvas, colors_dict)

    elif level_name == "Easy 4":
        locked, original_colors, shuffled_colors, ori_shuffled_colors = create_level_easy_4(canvas, colors_dict)

    elif level_name == "Easy 5":
        locked, original_colors, shuffled_colors, ori_shuffled_colors = create_level_easy_5(canvas, colors_dict)

    elif level_name == "Easy 6":
        locked, original_colors, shuffled_colors, ori_shuffled_colors = create_level_easy_6(canvas, colors_dict)

    # Bindataan hiiren painallus, vetäminen ja irti-päästäminen eventteihin
    canvas.bind("<Button-1>", lambda event:on_click(event, canvas, locked))
    canvas.bind("<B1-Motion>", lambda event:on_drag(event, canvas, locked))
    canvas.bind("<ButtonRelease-1>", lambda event:on_release(event, root, starting_frame, canvas, locked, level_name, \
                                                             original_colors, shuffled_colors, ori_shuffled_colors, chosen_name))
# -------------------------------------------------------------------
def game_complete(root, starting_frame, original_colors, current_colors, level_number, chosen_name):

    #print("original_colors", original_colors)
    
    if current_colors == original_colors:
        print("Level complete!")
        create_game_complete_frame(root, starting_frame, level_number, chosen_name)

# -------------------------------------------------------------------
def create_game_complete_frame(root, starting_frame, level_name, chosen_name):

    game_complete_frame = ttk.Frame(root, width=200, height=200, style = "blue.TFrame")
    game_complete_frame.grid(column = 0, row = 0)

    game_complete_frame.tkraise()

    # create_label(frame, teksti, tyyli, pystyrivi, vaakarivi, x_left, x_right, y_up, y_down)
    create_label(game_complete_frame, f"Level complete!", "white.TLabel", 0, 1, 10, 10, 10, 20)

    create_label(game_complete_frame, f"You took {globals.moves_done} moves!", "white.TLabel", 0, 2, 10, 10, 10, 20)

    if level_name[:-2] == "Easy":
        level = "1." + level_name[-1]

    elif level_name[:-2] == "Medium":
        level = "2." + level_name[-1]

    elif level_name[:-2] == "Hard":
        level = "3." + level_name[-1]

    player_controls.score_comparison(chosen_name, level, globals.moves_done, game_complete_frame)

    # Jos ei ole viimeinen level
    if level_name != "Hard 6":
        next_level = ""
        next_number = int(level_name[-1]) + 1

        if next_number > 6:
            if level_name[:-2] == "Easy":
                next_level = "Medium 1"

            if level_name[:-2] == "Medium":
                next_level = "Hard 1"
        else:
            next_level = level_name[:-1] + str(next_number)

        print("next_level", next_level)

        create_button(game_complete_frame, "Next level", "bw2.TButton", lambda:start_level(root, starting_frame, next_level, chosen_name), \
                  0, 7, 1, 1, 1, 1)

        create_button(game_complete_frame, "Go to Main", "bw2.TButton", lambda:starting_frame.tkraise(), \
                  0, 8, 1, 1, 1, 10)

# -------------------------------------------------------------------