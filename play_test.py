from color_dict import create_colors_dict

def play_tester(original_list, shuffled_list, locked):

    shuffled_names = ["r_1", "r_4", "r_5", "r_8", "r_9", "r_2", "r_3", "r_10", "r_7", "r_6", "r_11"]

    locked_places = []
    for i in locked:
        locked_places.append(i+1)

    while True:

        print("Level is:")
        print(shuffled_names)
        print("Locked places:", locked_places)
        place_from = int(input(f"Which place moves: (1-{len(shuffled_list)})"))
        place_to = int(input(f"Where is it moved: (1-{len(shuffled_list)})"))

        temp = shuffled_list[place_to-1]
        temp_name = shuffled_names[place_to-1]

        shuffled_list[place_to-1] = shuffled_list[place_from-1]
        shuffled_names[place_to-1] = shuffled_names[place_from-1]

        shuffled_list[place_from-1] = temp
        shuffled_names[place_from-1] = temp_name

        if shuffled_list == original_list:
            print("Congratulations! Level complete!")
            break

colors_dict = create_colors_dict()

original_list = [colors_dict["r_1"], colors_dict["r_2"], colors_dict["r_3"], colors_dict["r_4"], \
                 colors_dict["r_5"], colors_dict["r_6"], colors_dict["r_7"], colors_dict["r_8"], \
                    colors_dict["r_9"], colors_dict["r_10"], colors_dict["r_11"]]

shuffled_list = [colors_dict["r_1"], colors_dict["r_4"], colors_dict["r_5"], colors_dict["r_8"], \
                 colors_dict["r_9"], colors_dict["r_2"], colors_dict["r_3"], colors_dict["r_10"], \
                    colors_dict["r_7"], colors_dict["r_6"], colors_dict["r_11"]]

locked = [0, 10]

play_tester(original_list, shuffled_list, locked)



