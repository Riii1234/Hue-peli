import tkinter as tk
from tkinter import ttk
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

    entry = ttk.Entry(frame, textvariable = teksti_muuttuja, width = 20, style = "bw.TEntry")
    entry.grid(column = pystyrivi, row = vaakarivi, columnspan = 1, padx = [x_left, x_right], pady = [y_up, y_down])
    return entry
# -------------------------------------------------------------------
def create_combobox(frame, teksti_muuttuja, pystyrivi, vaakarivi, x_left, x_right, y_up, y_down):

    combobox = ttk.Combobox(frame, textvariable = teksti_muuttuja, state = "readonly", width = 20, style = "bw.TCombobox")
    combobox.grid(column = pystyrivi, row = vaakarivi, columnspan = 1, padx = [x_left, x_right], pady = [y_up, y_down])
    return combobox
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
def on_release(event, canvas, locked, original_colors, current_colors):
    """Siirtää palikoita riippuen hiiren painalluksen vapautuksen kohdasta"""
     
    if canvas.selected:
        if canvas.selected not in locked:
            pieces_on_place = canvas.find_overlapping(event.x, event.y, event.x, event.y)
            piece_under = pieces_on_place[0]
            #print("piece_under", piece_under)
            if event.y > 79 and event.y < 120:
                move_pieces(canvas, piece_under, 79)

            elif event.y > 119 and event.y < 160:
                move_pieces(canvas, piece_under, 119)

            elif event.y > 159 and event.y < 200:
                move_pieces(canvas, piece_under, 159)

            elif event.y > 199 and event.y < 240:
                move_pieces(canvas, piece_under, 199)

            elif event.y > 239 and event.y < 280:
                move_pieces(canvas, piece_under, 239)

            elif event.y > 279 and event.y < 320:
                move_pieces(canvas, piece_under, 279)

            elif event.y > 319 and event.y < 360:
                move_pieces(canvas, piece_under, 319)

            elif event.y > 359 and event.y < 400:
                move_pieces(canvas, piece_under, 359)

            elif event.y > 399 and event.y < 440:
                move_pieces(canvas, piece_under, 399)

            else:
                move_under_piece(canvas, canvas.selected)

    game_complete(original_colors, current_colors)
# -------------------------------------------------------------------
def move_pieces(canvas, under_piece, selected_y):
    """Siirtää liikutetun palikan ja sen alle jäävän paikkoja"""

    canvas.moveto(canvas.selected, 99, selected_y)
    move_under_piece(canvas, under_piece)
# -------------------------------------------------------------------
def move_under_piece(canvas, game_piece):
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

    canvas.moveto(game_piece, 99, original_y_coord)
# -------------------------------------------------------------------
def game_complete(original_colors, current_colors):

    if current_colors == original_colors:
        pass
