
# -------------------------------------------------------------------
def create_level(original_colors, lock_list):
    """Luodaan levelin palikat"""
    import colour_shuffling

    shuffled_colors = colour_shuffling.shuffle_list(original_colors, lock_list)

    ori_shuffled_colors = []
    for color in shuffled_colors:
        ori_shuffled_colors.append(color)



    return (shuffled_colors, ori_shuffled_colors)
# -------------------------------------------------------------------
def create_easy_rectangles(canvas, x1, y1, x2, y2, shuffled_colors):

    for i in range(len(shuffled_colors)):
        # x1, y1 = vasen yläkulma, x2, y2 = oikea alakulma, width on reunukset
        canvas.create_rectangle(x1, y1, x2, y2, fill = shuffled_colors[i], width = 0)
        y1 += 40
        y2 += 40
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
    
    shuffled_colors, ori_shuffled_colors= create_level(original_colors, [0,-1])
    create_easy_rectangles(canvas, 100, 40, 400, 80, shuffled_colors)

    create_easy_dots(canvas)

    # Palauttaa tuplessa lukossa olevat ja väri-listat
    return ([1, 11, 12, 13], original_colors, shuffled_colors, ori_shuffled_colors)
# -------------------------------------------------------------------
def create_level_easy_2(canvas, colors_dict):
    """Luodaan easy level 2"""
    
    original_colors = [colors_dict["b_15"], colors_dict["b_20"], colors_dict["b_25"], colors_dict["b_30"], \
              colors_dict["b_35"], colors_dict["b_40"], colors_dict["b_45"], colors_dict["b_50"], \
                colors_dict["b_55"], colors_dict["b_60"], colors_dict["b_65"]]
    
    shuffled_colors, ori_shuffled_colors= create_level(original_colors, [0,-1])
    create_easy_rectangles(canvas, 100, 40, 400, 80, shuffled_colors)

    create_easy_dots(canvas)

    # Palauttaa tuplessa lukossa olevat ja väri-listat
    return ([1, 11, 12, 13], original_colors, shuffled_colors, ori_shuffled_colors)
# -------------------------------------------------------------------
def create_level_easy_3(canvas, colors_dict):
    """Luodaan easy level 3"""
    
    original_colors = [colors_dict["g_15"], colors_dict["g_20"], colors_dict["g_25"], colors_dict["g_30"], \
              colors_dict["g_35"], colors_dict["g_40"], colors_dict["g_45"], colors_dict["g_50"], \
                colors_dict["g_55"], colors_dict["g_60"], colors_dict["g_65"]]
    
    shuffled_colors, ori_shuffled_colors= create_level(original_colors, [0,-1])
    create_easy_rectangles(canvas, 100, 40, 400, 80, shuffled_colors)

    create_easy_dots(canvas)

    # Palauttaa tuplessa lukossa olevat ja väri-listat
    return ([1, 11, 12, 13], original_colors, shuffled_colors, ori_shuffled_colors)
# -------------------------------------------------------------------
def create_level_easy_4(canvas, colors_dict):
    """Luodaan easy level 4"""
    
    original_colors = [colors_dict["p_15"], colors_dict["p_20"], colors_dict["p_25"], colors_dict["p_30"], \
              colors_dict["p_35"], colors_dict["p_40"], colors_dict["p_45"], colors_dict["p_50"], \
                colors_dict["p_55"], colors_dict["p_60"], colors_dict["p_65"]]
    
    shuffled_colors, ori_shuffled_colors= create_level(original_colors, [0,-1])
    create_easy_rectangles(canvas, 100, 40, 400, 80, shuffled_colors)

    create_easy_dots(canvas)

    # Palauttaa tuplessa lukossa olevat ja väri-listat
    return ([1, 11, 12, 13], original_colors, shuffled_colors, ori_shuffled_colors)
# -------------------------------------------------------------------
def create_level_easy_5(canvas, colors_dict):
    """Luodaan easy level 5"""
    
    original_colors = [colors_dict["y_15"], colors_dict["y_20"], colors_dict["y_25"], colors_dict["y_30"], \
              colors_dict["y_35"], colors_dict["y_40"], colors_dict["y_45"], colors_dict["y_50"], \
                colors_dict["y_55"], colors_dict["y_60"], colors_dict["y_65"]]
    
    shuffled_colors, ori_shuffled_colors= create_level(original_colors, [0,-1])
    create_easy_rectangles(canvas, 100, 40, 400, 80, shuffled_colors)

    create_easy_dots(canvas)

    # Palauttaa tuplessa lukossa olevat ja väri-listat
    return ([1, 11, 12, 13], original_colors, shuffled_colors, ori_shuffled_colors)
# -------------------------------------------------------------------
def create_level_easy_6(canvas, colors_dict):
    """Luodaan easy level 6"""
    
    original_colors = [colors_dict["t_15"], colors_dict["t_20"], colors_dict["t_25"], colors_dict["t_30"], \
              colors_dict["t_35"], colors_dict["t_40"], colors_dict["t_45"], colors_dict["t_50"], \
                colors_dict["t_55"], colors_dict["t_60"], colors_dict["t_65"]]
    
    shuffled_colors, ori_shuffled_colors= create_level(original_colors, [0,-1])
    create_easy_rectangles(canvas, 100, 40, 400, 80, shuffled_colors)

    create_easy_dots(canvas)

    # Palauttaa tuplessa lukossa olevat ja väri-listat
    return ([1, 11, 12, 13], original_colors, shuffled_colors, ori_shuffled_colors)
# -------------------------------------------------------------------
def create_medium_rectangles(canvas, x1, y1, x2, y2, shuffled_colors):
    count = 0
    y1_use = y1
    y2_use = y2

    for i in range(len(shuffled_colors)):
        # x1, y1 = vasen yläkulma, x2, y2 = oikea alakulma, width on reunukset
        canvas.create_rectangle(x1, y1_use, x2, y2_use, fill = shuffled_colors[i], width = 0)
        y1_use += 40
        y2_use += 40
        count += 1

        if count == 11:
            x1 += 100
            x2 += 100
            y1_use = y1
            y2_use = y2
            count = 0
# ------------------------------------------------------------------- 
def create_medium_dots(canvas):

    # Luodaan pisteet lukossa oleville palikoille
    dot1 = canvas.create_oval(148, 58, 152, 62, tags = "point", fill = "black")
    dot2 = canvas.create_oval(148, 458, 152, 462, tags = "point", fill = "black")
    dot3 = canvas.create_oval(248, 58, 252, 62, tags = "point", fill = "black")
    dot4 = canvas.create_oval(248, 458, 252, 462, tags = "point", fill = "black")
    dot5 = canvas.create_oval(348, 58, 352, 62, tags = "point", fill = "black")
    dot6 = canvas.create_oval(348, 458, 352, 462, tags = "point", fill = "black")
    # -------------------------------------------------------------------
def create_level_medium_1(canvas, colors_dict):
    """Luodaan medium level 1"""

    original_colors = [colors_dict["r_40"], colors_dict["r_45"], colors_dict["r_50"], colors_dict["r_55"], \
              colors_dict["r_60"], colors_dict["r_65"], colors_dict["r_70"], colors_dict["r_75"], \
                colors_dict["r_80"], colors_dict["r_85"], colors_dict["r_90"], \
                \
                    colors_dict["r_y_18"], colors_dict["r_y_21"], colors_dict["r_y_24"], colors_dict["r_y_27"], \
              colors_dict["r_y_30"], colors_dict["r_y_33"], colors_dict["r_y_36"], colors_dict["r_y_39"], \
                colors_dict["r_y_42"], colors_dict["r_y_45"], colors_dict["r_y_48"], \
                \
                    colors_dict["y_40"], colors_dict["y_45"], colors_dict["y_50"], colors_dict["y_55"], \
              colors_dict["y_60"], colors_dict["y_65"], colors_dict["y_70"], colors_dict["y_75"], \
                colors_dict["y_80"], colors_dict["y_85"], colors_dict["y_90"]]

    shuffled_colors, ori_shuffled_colors= create_level(original_colors, [0, 10, 11, 21, 22, -1])
    create_medium_rectangles(canvas, 100, 40, 200, 80, shuffled_colors)

    create_medium_dots(canvas)
    return ([1, 11, 12, 22, 23, 33, 34, 35, 36, 37, 38, 39], original_colors, shuffled_colors, ori_shuffled_colors)
# -------------------------------------------------------------------
def create_level_medium_2(canvas, colors_dict):
    """Luodaan medium level 2"""

    original_colors = [colors_dict["r_40"], colors_dict["r_45"], colors_dict["r_50"], colors_dict["r_55"], \
              colors_dict["r_60"], colors_dict["r_65"], colors_dict["r_70"], colors_dict["r_75"], \
                colors_dict["r_80"], colors_dict["r_85"], colors_dict["r_90"], \
                \
                    colors_dict["r_p_18"], colors_dict["r_p_21"], colors_dict["r_p_24"], colors_dict["r_p_27"], \
              colors_dict["r_p_30"], colors_dict["r_p_33"], colors_dict["r_p_36"], colors_dict["r_p_39"], \
                colors_dict["r_p_42"], colors_dict["r_p_45"], colors_dict["r_p_48"], \
                \
                    colors_dict["p_40"], colors_dict["p_45"], colors_dict["p_50"], colors_dict["p_55"], \
              colors_dict["p_60"], colors_dict["p_65"], colors_dict["p_70"], colors_dict["p_75"], \
                colors_dict["p_80"], colors_dict["p_85"], colors_dict["p_90"]]

    shuffled_colors, ori_shuffled_colors= create_level(original_colors, [0, 10, 11, 21, 22, -1])
    create_medium_rectangles(canvas, 100, 40, 200, 80, shuffled_colors)

    create_medium_dots(canvas)
    return ([1, 11, 12, 22, 23, 33, 34, 35, 36, 37, 38, 39], original_colors, shuffled_colors, ori_shuffled_colors)
# -------------------------------------------------------------------
def create_level_medium_3(canvas, colors_dict):
    """Luodaan medium level 3"""

    original_colors = [colors_dict["b_40"], colors_dict["b_45"], colors_dict["b_50"], colors_dict["b_55"], \
              colors_dict["b_60"], colors_dict["b_65"], colors_dict["b_70"], colors_dict["b_75"], \
                colors_dict["b_80"], colors_dict["b_85"], colors_dict["b_90"], \
                \
                    colors_dict["b_p_18"], colors_dict["b_p_21"], colors_dict["b_p_24"], colors_dict["b_p_27"], \
              colors_dict["b_p_30"], colors_dict["b_p_33"], colors_dict["b_p_36"], colors_dict["b_p_39"], \
                colors_dict["b_p_42"], colors_dict["b_p_45"], colors_dict["b_p_48"], \
                \
                    colors_dict["p_40"], colors_dict["p_45"], colors_dict["p_50"], colors_dict["p_55"], \
              colors_dict["p_60"], colors_dict["p_65"], colors_dict["p_70"], colors_dict["p_75"], \
                colors_dict["p_80"], colors_dict["p_85"], colors_dict["p_90"]]

    shuffled_colors, ori_shuffled_colors= create_level(original_colors, [0, 10, 11, 21, 22, -1])
    create_medium_rectangles(canvas, 100, 40, 200, 80, shuffled_colors)

    create_medium_dots(canvas)
    return ([1, 11, 12, 22, 23, 33, 34, 35, 36, 37, 38, 39], original_colors, shuffled_colors, ori_shuffled_colors)
# -------------------------------------------------------------------
def create_level_medium_4(canvas, colors_dict):
    """Luodaan medium level 4"""

    original_colors = [colors_dict["b_40"], colors_dict["b_45"], colors_dict["b_50"], colors_dict["b_55"], \
              colors_dict["b_60"], colors_dict["b_65"], colors_dict["b_70"], colors_dict["b_75"], \
                colors_dict["b_80"], colors_dict["b_85"], colors_dict["b_90"], \
                \
                    colors_dict["b_t_18"], colors_dict["b_t_21"], colors_dict["b_t_24"], colors_dict["b_t_27"], \
              colors_dict["b_t_30"], colors_dict["b_t_33"], colors_dict["b_t_36"], colors_dict["b_t_39"], \
                colors_dict["b_t_42"], colors_dict["b_t_45"], colors_dict["b_t_48"], \
                \
                    colors_dict["t_40"], colors_dict["t_45"], colors_dict["t_50"], colors_dict["t_55"], \
              colors_dict["t_60"], colors_dict["t_65"], colors_dict["t_70"], colors_dict["t_75"], \
                colors_dict["t_80"], colors_dict["t_85"], colors_dict["t_90"]]

    shuffled_colors, ori_shuffled_colors= create_level(original_colors, [0, 10, 11, 21, 22, -1])
    create_medium_rectangles(canvas, 100, 40, 200, 80, shuffled_colors)

    create_medium_dots(canvas)
    return ([1, 11, 12, 22, 23, 33, 34, 35, 36, 37, 38, 39], original_colors, shuffled_colors, ori_shuffled_colors)
# -------------------------------------------------------------------
def create_level_medium_5(canvas, colors_dict):
    """Luodaan medium level 5"""

    original_colors = [colors_dict["g_40"], colors_dict["g_45"], colors_dict["g_50"], colors_dict["g_55"], \
              colors_dict["g_60"], colors_dict["g_65"], colors_dict["g_70"], colors_dict["g_75"], \
                colors_dict["g_80"], colors_dict["g_85"], colors_dict["g_90"], \
                \
                    colors_dict["g_t_18"], colors_dict["g_t_21"], colors_dict["g_t_24"], colors_dict["g_t_27"], \
              colors_dict["g_t_30"], colors_dict["g_t_33"], colors_dict["g_t_36"], colors_dict["g_t_39"], \
                colors_dict["g_t_42"], colors_dict["g_t_45"], colors_dict["g_t_48"], \
                \
                    colors_dict["t_40"], colors_dict["t_45"], colors_dict["t_50"], colors_dict["t_55"], \
              colors_dict["t_60"], colors_dict["t_65"], colors_dict["t_70"], colors_dict["t_75"], \
                colors_dict["t_80"], colors_dict["t_85"], colors_dict["t_90"]]

    shuffled_colors, ori_shuffled_colors= create_level(original_colors, [0, 10, 11, 21, 22, -1])
    create_medium_rectangles(canvas, 100, 40, 200, 80, shuffled_colors)

    create_medium_dots(canvas)
    return ([1, 11, 12, 22, 23, 33, 34, 35, 36, 37, 38, 39], original_colors, shuffled_colors, ori_shuffled_colors)
# -------------------------------------------------------------------
def create_level_medium_6(canvas, colors_dict):
    """Luodaan medium level 6"""

    original_colors = [colors_dict["g_40"], colors_dict["g_45"], colors_dict["g_50"], colors_dict["g_55"], \
              colors_dict["g_60"], colors_dict["g_65"], colors_dict["g_70"], colors_dict["g_75"], \
                colors_dict["g_80"], colors_dict["g_85"], colors_dict["g_90"], \
                \
                    colors_dict["g_y_18"], colors_dict["g_y_21"], colors_dict["g_y_24"], colors_dict["g_y_27"], \
              colors_dict["g_y_30"], colors_dict["g_y_33"], colors_dict["g_y_36"], colors_dict["g_y_39"], \
                colors_dict["g_y_42"], colors_dict["g_y_45"], colors_dict["g_y_48"], \
                \
                    colors_dict["y_40"], colors_dict["y_45"], colors_dict["y_50"], colors_dict["y_55"], \
              colors_dict["y_60"], colors_dict["y_65"], colors_dict["y_70"], colors_dict["y_75"], \
                colors_dict["y_80"], colors_dict["y_85"], colors_dict["y_90"]]

    shuffled_colors, ori_shuffled_colors= create_level(original_colors, [0, 10, 11, 21, 22, -1])
    create_medium_rectangles(canvas, 100, 40, 200, 80, shuffled_colors)

    create_medium_dots(canvas)
    return ([1, 11, 12, 22, 23, 33, 34, 35, 36, 37, 38, 39], original_colors, shuffled_colors, ori_shuffled_colors)
# -------------------------------------------------------------------

