# ---------------------------------------------------------------------------------------------
color_codes = {255 : "FF", 250 : "FA", 245 : "F5", 240 : "F0", 235 : "EB", 230 : "E6", \
               225 : "E1", 220 : "DC", 215 : "D7", 210 : "D2", 205 : "CD", 200 : "C8", \
                195 : "C3", 190 : "BE", 185 : "B9", 180 : "B4", 175 : "AF", 170 : "AA", \
                165 : "A5", 160 : "A0", 155 : "9B", 150 : "96", 145 : "91", 140 : "8C", \
                135 : "87", 130 : "82", 125 : "7D", 120 : "78", 115 : "73", 110 : "6E", \
                105 : "69", 100 : "64", 95 : "5F", 90 : "5A", 85 : "55", 80 : "50", \
                75 : "4B", 70 : "46", 65 : "41", 60 : "3C", 55 : "37", 50 : "32", \
                45 : "2D", 40 : "28", 35 : "23", 30 : "1E", 25 : "19", 20 : "14", \
                15 : "0F", 10 : "0A", 5 : "05", 0 : "00"}
# ---------------------------------------------------------------------------------------------
colors = ["r", "b", "g", "y", "p", "t", "r_y", "g_y", "g_t", "b_t", "b_p", "r_p"]
# ---------------------------------------------------------------------------------------------
def create_color_names_n_codes():
    """Creates and returns a dictionary with all needed color names and rgb color codes"""

    temp_dict = {}
    for i in colors:
        count = 251
        count2 = 240
        a = 1
        temp_dict["color_names_%s" % i] = []
        temp_dict["rgb_codes_%s" % i] = []

        
        while count > 5:
            temp_dict["color_names_%s" % i].append(f"{i}_{a}")

            if len(i) < 2:
                temp_dict["color_names_%s" % i].append(f"{i}_{a+50}")

            if i == "r":
                # Creates 50 colors from light to medium and 50 colors from medium to dark
                create_light_and_dark_color(temp_dict, i, 255, count-1, count-1, count+4, 0, 0)
            elif i == "b":
                create_light_and_dark_color(temp_dict, i, count-1, count-1, 255, 0, 0, count+4)
            elif i == "g":
                create_light_and_dark_color(temp_dict, i, count-1, 255, count-1, 0, count+4, 0)
            elif i == "y":
                create_light_and_dark_color(temp_dict, i, 255, 255, count-1, count+4, count+4, 0)
            elif i == "p":
                create_light_and_dark_color(temp_dict, i, 255, count-1, 255, count+4, 0, count+4)
            elif i == "t":
                create_light_and_dark_color(temp_dict, i, count-1, 255, 255, 0, count+4, count+4)

            elif i == "r_y":
                # Creates 25 colors from light to medium and 25 colors from medium to dark
                create_light_or_dark_color(temp_dict, a, i, 255, count-1, count2, count2+255, count-1, 0)
            elif i == "g_y":
                create_light_or_dark_color(temp_dict, a, i, count-1, 255, count2, count-1, count2+255, 0)
            elif i == "g_t":
                create_light_or_dark_color(temp_dict, a, i, count2, 255, count-1, 0, count2+255, count-1)
            elif i == "b_t":
                create_light_or_dark_color(temp_dict, a, i, count2, count-1, 255, 0, count-1, count2+255)
            elif i == "b_p":
                create_light_or_dark_color(temp_dict, a, i, count-1, count2, 255, count-1, 0, count2+255)
            elif i == "r_p":
                create_light_or_dark_color(temp_dict, a, i, 255, count-1, count2, count2+255, 0, count-1)
                
            count -= 5
            count2 -= 10
            a += 1

    return temp_dict
# ---------------------------------------------------------------------------------------------
def create_color(temp_dict, i, r, g, b):
    """Creates a color code and appends it to a list"""
    temp_dict["rgb_codes_%s" % i].append(f"#{color_codes[r]}{color_codes[g]}{color_codes[b]}")
# ---------------------------------------------------------------------------------------------
def create_light_and_dark_color(temp_dict, i, r1, g1, b1, r2, g2, b2):
    """Creates one light and one dark color"""
    create_color(temp_dict, i, r1, g1, b1)
    create_color(temp_dict, i, r2, g2, b2)
# ---------------------------------------------------------------------------------------------
def create_light_or_dark_color(temp_dict, a, i, r1, g1, b1, r2, g2, b2):
    """Creates one light color when a < 26, and otherwise one dark color"""
    if a < 26:
        create_color(temp_dict, i, r1, g1, b1)
    else:
        create_color(temp_dict, i, r2, g2, b2)
# ---------------------------------------------------------------------------------------------
def create_colors_dict():
    """Creates a dictionary of color name dictionaries that have color codes and lock-status"""
    temp_dict = create_color_names_n_codes()
    # print(temp_dict)

    colors_dict = {}

    for i in colors:
        for a in range(len(temp_dict["color_names_%s" % i])):

            colors_dict[temp_dict["color_names_%s" % i][a]] = temp_dict["rgb_codes_%s" % i][a]

    return colors_dict
# ---------------------------------------------------------------------------------------------
colors_dict = create_colors_dict()
print(colors_dict)
# ---------------------------------------------------------------------------------------------

