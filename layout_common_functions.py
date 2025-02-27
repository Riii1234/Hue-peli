import tkinter as tk
from tkinter import ttk

import globals
from globals import original_y_coord, original_x_coord
# -------------------------------------------------------------------
def create_frame(root):
    """Luo framen ja reunukset"""
    # Luo frame widgetin
    frame = ttk.Frame(root, width=600, height=600, style = "blue.TFrame")
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

    entry = ttk.Entry(frame, textvariable = teksti_muuttuja, width = 3, style = "bw.TEntry")
    entry.grid(column = pystyrivi, row = vaakarivi, columnspan = 1, padx = [x_left, x_right], pady = [y_up, y_down])
    return entry
# -------------------------------------------------------------------
def create_combobox(frame, teksti_muuttuja, pystyrivi, vaakarivi, x_left, x_right, y_up, y_down):
    """Luo valikon ja asettaa sen frameen"""

    combobox = ttk.Combobox(frame, textvariable = teksti_muuttuja, state = "readonly", width = 20, style = "bw.TCombobox")
    combobox.grid(column = pystyrivi, row = vaakarivi, columnspan = 1, padx = [x_left, x_right], pady = [y_up, y_down])
    return combobox
# -------------------------------------------------------------------
def set_combobox(combobox, info_list):
    """Täyttää valikon listan tiedoilla"""

    # Sijoitetaan tiedot valikkoon
    combobox.configure(values = info_list)
    # Asetetaan uusim nimi näkyville valikkoon
    combobox.set(info_list[-1])
# -------------------------------------------------------------------
def delete_from_combobox(combobox, deleted_item):
    """Poistaa yhden tiedon comboboxista"""

    options = list(combobox['values'])
    print("options, deleted_item", options, deleted_item)
    options.remove(deleted_item)

    combobox['values'] = options
    combobox.set(options[-1])
# -------------------------------------------------------------------
def on_click(event, canvas, locked):
    """Hiirtä klikkaamalla valitsee kohdalla olevan palasen"""

    selected = canvas.find_overlapping(event.x, event.y, event.x, event.y)
    if selected:
        canvas.selected = selected[-1]
        if canvas.selected not in locked:
            # Moves the selected piece to the top layer
            canvas.tag_raise(canvas.selected)
            canvas.startxy = (event.x, event.y)
            #print(selected, canvas.selected, canvas.startxy)
            global original_y_coord
            original_y_coord = event.y
            global original_x_coord
            original_x_coord = event.x
    else:
        canvas.selected = None
# -------------------------------------------------------------------
def on_drag(event, canvas, locked):
    """Liikuttaa valittua palikkaa"""

    if canvas.selected:
        if canvas.selected not in locked:
            # Calculate distance moved from last position
            dx, dy = event.x-canvas.startxy[0], event.y-canvas.startxy[1]
            # Move the selected item
            canvas.move(canvas.selected, dx, dy)

            # Update last position
            canvas.startxy = (event.x, event.y)
# -------------------------------------------------------------------
def on_release(event, root, starting_frame, game_frame, level_frame, canvas, locked, level_number, original_colors, level_colors, ori_level_colors, chosen_name):
    """Siirtää palikoita riippuen hiiren painalluksen vapautuksen kohdasta"""
     
    if canvas.selected:
        if canvas.selected not in locked:
            pieces_on_place = canvas.find_overlapping(event.x, event.y, event.x, event.y)
            piece_under = pieces_on_place[0]
            #print("piece_under", piece_under)

            if level_number[:-2] == "Medium":

                if event.x > 99 and event.x < 200:
                    selected_x = 99
                elif event.x > 199 and event.x < 300:
                    selected_x = 199
                elif event.x > 299 and event.x < 400:
                    selected_x = 299
                else:
                    global original_x_coord
                    if original_x_coord > 99 and original_x_coord < 200:
                        selected_x = 99
                    elif original_x_coord > 199 and original_x_coord < 300:
                        selected_x = 199
                    elif original_x_coord > 299 and original_x_coord < 400:
                        selected_x = 299

            else:
                selected_x = 99

            if event.y > 79 and event.y < 120:
                move_pieces(canvas, piece_under, selected_x, 79, level_colors, ori_level_colors)

            elif event.y > 119 and event.y < 160:
                move_pieces(canvas, piece_under, selected_x, 119, level_colors, ori_level_colors)

            elif event.y > 159 and event.y < 200:
                move_pieces(canvas, piece_under, selected_x, 159, level_colors, ori_level_colors)

            elif event.y > 199 and event.y < 240:
                move_pieces(canvas, piece_under, selected_x, 199, level_colors, ori_level_colors)

            elif event.y > 239 and event.y < 280:
                move_pieces(canvas, piece_under, selected_x, 239, level_colors, ori_level_colors)

            elif event.y > 279 and event.y < 320:
                move_pieces(canvas, piece_under, selected_x, 279, level_colors, ori_level_colors)

            elif event.y > 319 and event.y < 360:
                move_pieces(canvas, piece_under, selected_x, 319, level_colors, ori_level_colors)

            elif event.y > 359 and event.y < 400:
                move_pieces(canvas, piece_under, selected_x, 359, level_colors, ori_level_colors)

            elif event.y > 399 and event.y < 440:
                move_pieces(canvas, piece_under, selected_x, 399, level_colors, ori_level_colors)

            else:
                move_under_piece(canvas, canvas.selected, selected_x)

    from layout import game_complete
    game_complete(root, starting_frame, game_frame, level_frame, original_colors, level_colors, level_number, chosen_name)
# -------------------------------------------------------------------
def move_pieces(canvas, under_piece, selected_x, selected_y, level_colors, ori_level_colors):
    """Siirtää liikutetun palikan ja sen alle jäävän paikkoja"""

    # Palikoiden liikuttamisen laskemista varten väliaikainen lista
    temp_level_colors = []
    for color in level_colors:
        temp_level_colors.append(color)

    canvas.moveto(canvas.selected, selected_x, selected_y)

    # Mikä numero palikka alla
    #print("under_piece", under_piece)

    # Mikä väri liikkuu alta ja mikä sen alkuperäinen paikka oli
    for i in range(len(level_colors)):
        if level_colors[i] == ori_level_colors[int(under_piece)-1]:
            temp_place = i
            under_color = level_colors[i]
            #print("temp_place, under_color", temp_place, under_color)

    # Mitä väriä siirretään ja mikä sen alkuperäinen paikka oli
        if level_colors[i] == ori_level_colors[int(canvas.selected)-1]:
            temp_place2 = i
            moving_color = level_colors[i]
            #print("temp_place2, moving_color", temp_place2, moving_color)

    # Siirretään värit pelaus-listassa
    level_colors[temp_place] = moving_color
    level_colors[temp_place2] = under_color
    
    #print("level_colors", level_colors)
    #print("ori_level_colors", ori_level_colors)

    if level_colors != temp_level_colors:

        globals.moves_done += 1
        #print("moves_done", globals.moves_done)

    move_under_piece(canvas, under_piece, selected_x)
# -------------------------------------------------------------------
def move_under_piece(canvas, game_piece, selected_x):
    """Siirtää liikutetun palikan alle jäävän palikan"""

    global original_y_coord

    if original_y_coord > 79 and original_y_coord < 120:
        original_y_coord = 79

    elif original_y_coord > 119 and original_y_coord < 160:
        original_y_coord = 119

    elif original_y_coord > 159 and original_y_coord < 200:
        original_y_coord = 159

    elif original_y_coord > 199 and original_y_coord < 240:
        original_y_coord = 199

    elif original_y_coord > 239 and original_y_coord < 280:
        original_y_coord = 239

    elif original_y_coord > 279 and original_y_coord < 320:
        original_y_coord = 279

    elif original_y_coord > 319 and original_y_coord < 360:
        original_y_coord = 319

    elif original_y_coord > 359 and original_y_coord < 400:
        original_y_coord = 359

    elif original_y_coord > 399 and original_y_coord < 440:
        original_y_coord = 399

    canvas.moveto(game_piece, selected_x, original_y_coord)
# -------------------------------------------------------------------