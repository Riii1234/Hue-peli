
# -------------------------------------------------------------------
def create_level(canvas, x1, y1, x2, y2, original_colors, lock_list):
    """Luodaan levelin palikat"""
    import colour_shuffling

    shuffled_colors = colour_shuffling.shuffle_list(original_colors, lock_list)

    ori_shuffled_colors = []
    for color in shuffled_colors:
        ori_shuffled_colors.append(color)

    for i in range(len(shuffled_colors)):
        # x1, y1 = vasen yläkulma, x2, y2 = oikea alakulma, width on reunukset
        canvas.create_rectangle(x1, y1, x2, y2, fill = shuffled_colors[i], width = 0)
        y1 += 40
        y2 += 40

    return (shuffled_colors, ori_shuffled_colors)
# -------------------------------------------------------------------
def create_easy_dots(canvas):

    # Luodaan pisteet lukossa oleville palikoille
    dot1 = canvas.create_oval(248, 58, 252, 62, tags = "point", fill = "black")
    dot2 = canvas.create_oval(248, 458, 252, 462, tags = "point", fill = "black")
# -------------------------------------------------------------------
def create_level_easy_1(canvas, colors_dict):
    """Luodaan easy level 1"""
    
    original_colors = [colors_dict["r_15"], colors_dict["r_20"], colors_dict["r_25"], colors_dict["r_30"], \
              colors_dict["r_35"], colors_dict["r_40"], colors_dict["r_45"], colors_dict["r_50"], \
                colors_dict["r_55"], colors_dict["r_60"], colors_dict["r_65"]]
    lock_list = [0,-1]
    
    shuffled_colors, ori_shuffled_colors= create_level(canvas, 100, 40, 400, 80, original_colors, lock_list)

    create_easy_dots(canvas)

    # Palauttaa tuplessa lukossa olevat ja väri-listat
    return ([1, 11, 12, 13], original_colors, shuffled_colors, ori_shuffled_colors)
# -------------------------------------------------------------------
def create_level_easy_2(canvas, colors_dict):
    """Luodaan easy level 2"""
    
    original_colors = [colors_dict["b_15"], colors_dict["b_20"], colors_dict["b_25"], colors_dict["b_30"], \
              colors_dict["b_35"], colors_dict["b_40"], colors_dict["b_45"], colors_dict["b_50"], \
                colors_dict["b_55"], colors_dict["b_60"], colors_dict["b_65"]]
    lock_list = [0,-1]
    
    shuffled_colors, ori_shuffled_colors = create_level(canvas, 100, 40, 400, 80, original_colors, lock_list)

    create_easy_dots(canvas)

    # Palauttaa tuplessa lukossa olevat ja väri-listat
    return ([1, 11, 12, 13], original_colors, shuffled_colors, ori_shuffled_colors)
# -------------------------------------------------------------------
def create_level_easy_3(canvas, colors_dict):
    """Luodaan easy level 3"""
    
    original_colors = [colors_dict["g_15"], colors_dict["g_20"], colors_dict["g_25"], colors_dict["g_30"], \
              colors_dict["g_35"], colors_dict["g_40"], colors_dict["g_45"], colors_dict["g_50"], \
                colors_dict["g_55"], colors_dict["g_60"], colors_dict["g_65"]]
    lock_list = [0,-1]
    
    shuffled_colors, ori_shuffled_colors = create_level(canvas, 100, 40, 400, 80, original_colors, lock_list)

    create_easy_dots(canvas)

    # Palauttaa tuplessa lukossa olevat ja väri-listat
    return ([1, 11, 12, 13], original_colors, shuffled_colors, ori_shuffled_colors)
# -------------------------------------------------------------------
def create_level_easy_4(canvas, colors_dict):
    """Luodaan easy level 4"""
    
    original_colors = [colors_dict["p_15"], colors_dict["p_20"], colors_dict["p_25"], colors_dict["p_30"], \
              colors_dict["p_35"], colors_dict["p_40"], colors_dict["p_45"], colors_dict["p_50"], \
                colors_dict["p_55"], colors_dict["p_60"], colors_dict["p_65"]]
    lock_list = [0,-1]
    
    shuffled_colors, ori_shuffled_colors = create_level(canvas, 100, 40, 400, 80, original_colors, lock_list)

    create_easy_dots(canvas)

    # Palauttaa tuplessa lukossa olevat ja väri-listat
    return ([1, 11, 12, 13], original_colors, shuffled_colors, ori_shuffled_colors)
# -------------------------------------------------------------------
def create_level_easy_5(canvas, colors_dict):
    """Luodaan easy level 5"""
    
    original_colors = [colors_dict["y_15"], colors_dict["y_20"], colors_dict["y_25"], colors_dict["y_30"], \
              colors_dict["y_35"], colors_dict["y_40"], colors_dict["y_45"], colors_dict["y_50"], \
                colors_dict["y_55"], colors_dict["y_60"], colors_dict["y_65"]]

    lock_list = [0,-1]
    
    shuffled_colors, ori_shuffled_colors = create_level(canvas, 100, 40, 400, 80, original_colors, lock_list)

    create_easy_dots(canvas)

    # Palauttaa tuplessa lukossa olevat ja väri-listat
    return ([1, 11, 12, 13], original_colors, shuffled_colors, ori_shuffled_colors)
# -------------------------------------------------------------------
def create_level_easy_6(canvas, colors_dict):
    """Luodaan easy level 6"""
    
    original_colors = [colors_dict["t_15"], colors_dict["t_20"], colors_dict["t_25"], colors_dict["t_30"], \
              colors_dict["t_35"], colors_dict["t_40"], colors_dict["t_45"], colors_dict["t_50"], \
                colors_dict["t_55"], colors_dict["t_60"], colors_dict["t_65"]]
    lock_list = [0,-1]
    
    shuffled_colors, ori_shuffled_colors = create_level(canvas, 100, 40, 400, 80, original_colors, lock_list)

    create_easy_dots(canvas)

    # Palauttaa tuplessa lukossa olevat ja väri-listat
    return ([1, 11, 12, 13], original_colors, shuffled_colors, ori_shuffled_colors)
# -------------------------------------------------------------------

