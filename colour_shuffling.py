from random import shuffle

def temporary_clr_list():
    """Temporary list for hue_peli"""
    colour_list = []
    for i in range(1,21):
        colour_list.append(f"r_{i}")
    return colour_list

def shuffle_list(colour_list = list,lock_list = list):    
    """shuffles the list according to locks and checks it, lock_list isn't checked for accuracy"""
    
    #goes through the locked indexes and assigns them their colour into a dictionary
    locked_colours = {}
    for lock_index in lock_list:
        locked_colours[lock_index] = colour_list[lock_index]
    #print(locked_colours)

    #creates a blank list called new_colours the length of the colour_list
    new_colours = []
    for i in range(len(colour_list)):
        new_colours.append("")
    #assigns the locked colours to the formerly blank list new_colours
    for lock_index in locked_colours:
        new_colours[lock_index] = locked_colours[lock_index]
    #print(new_colours)

    #compares the new_colours list with all the colours and creates a shufflable list with non-locked colours
    shufflables_original_order = []
    for colour in colour_list:
        if colour not in new_colours:
            shufflables_original_order.append(colour)
    #print(shufflables_original_order)

    #creates shuffle match threshold for how many shuffled colours may match the original list (one fifth of non-locked numbers rounded)
    threshold = (len(colour_list) - len(lock_list)) / 5
    threshold = round(threshold)
    #print(threshold)

    #shuffles the shufflables list so that no matches go over the threshold
    while True:
        threshold_counter = 0
        shufflables_new_order = shufflables_original_order.copy()
        shuffle(shufflables_new_order)
        for i in range(len(shufflables_original_order)):
            if shufflables_new_order[i] == shufflables_original_order[i]:
                threshold_counter += 1
        if threshold_counter <= threshold:
            break

    #puts the locked and shuffled numbers together in order
    for i in range(len(new_colours)):
        if new_colours[i] == "":
            new_colours[i] = shufflables_new_order[0]
            shufflables_new_order.pop(0)
    
    return new_colours




def run():
    """runs"""
    #temporary makes a list from r_1 to r_20
    colour_list = temporary_clr_list()
    #lock_list accepts negative index numbers, doesn't check for incorrect indexes
    lock_list = [0,-1]
    shuffled_colours = shuffle_list(colour_list,lock_list)
    print(shuffled_colours)

#run()
