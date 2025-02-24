
# -------------------------------------------------------------------
def create_level(canvas, x1, y1, x2, y2, colors):
    """Luodaan levelin palikat"""

    for i in range(len(colors)):
        # x1, y1 = vasen yläkulma, x2, y2 = oikea alakulma, width on reunukset
        canvas.create_rectangle(x1, y1, x2, y2, fill = colors[i], width = 0)
        y1 += 40
        y2 += 40
# -------------------------------------------------------------------
def create_level_easy_1(canvas, colors_dict):
    """Luodaan easy level 1"""
    import colour_shuffling

    original_colors = [colors_dict["r_15"], colors_dict["r_20"], colors_dict["r_25"], colors_dict["r_30"], \
              colors_dict["r_35"], colors_dict["r_40"], colors_dict["r_45"], colors_dict["r_50"], \
                colors_dict["r_55"], colors_dict["r_60"], colors_dict["r_65"]]
    lock_list = [0,-1]
    
    shuffled_colors = colour_shuffling.shuffle_list(original_colors, lock_list)

    create_level(canvas, 100, 40, 400, 80, shuffled_colors)

    # Luodaan pisteet lukossa oleville palikoille
    dot1 = canvas.create_oval(248, 58, 252, 62, tags = "point", fill = "black")
    dot2 = canvas.create_oval(248, 458, 252, 462, tags = "point", fill = "black")

    # Palauttaa tuplessa lukossa olevat ja väri-listat
    return ([1, 11, 12, 13], original_colors, shuffled_colors)
# -------------------------------------------------------------------
              
