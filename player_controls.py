import csv
import os

#loading player data
def player_data_loader():
    """compiles players into a list from the csv file"""
    with open("player_data.csv", mode="r",newline="",encoding='utf-8-sig', errors='replace') as player_file:
            csv_reader = csv.DictReader(player_file)
            player_list = []
            for row in csv_reader:
                player_list.append(row)
    
    reconstructed_player_list = []
    for dict in player_list:
        incomplete_player_levels = dict["incomplete_levels"]
        complete_levels_best = dict["complete_levels_best"]

        #reconstructs the incomplete levels as a list
        incomplete_player_levels = incomplete_player_levels[1:-1]
        ipl_temporary = ""
        for letter in incomplete_player_levels:
            if letter != "," and letter != "'":
                ipl_temporary += letter
        incomplete_player_levels = ipl_temporary.split()
        #print(incomplete_player_levels)

        #reconstructs complete levels best as a list
        complete_levels_best = complete_levels_best[1:-1]
        clb_temporary = ""
        for letter in complete_levels_best:
            if letter != " " and letter != "'":
                clb_temporary += letter
        complete_levels_best = clb_temporary.split(",")

        #puts the list items into a dictionary
        if '' in complete_levels_best:
            complete_levels_best = {}
        else:
            levels_best_dict = {}
            for level in complete_levels_best:
                y = level.split(":")
                levels_best_dict[y[0]] = int(y[1])
            complete_levels_best = levels_best_dict
            #print(complete_levels_best)

        dict["incomplete_levels"] = incomplete_player_levels
        dict["complete_levels_best"] = complete_levels_best
        reconstructed_player_list.append(dict)

    return reconstructed_player_list

#writing player data
def player_data_writer(player_list):
    """writes the player list down into the csv file"""
    fields = ["username","incomplete_levels","complete_levels_best"]
    with open(f"player_data.csv","w",newline="",encoding='utf-8-sig', errors='replace') as player_file:
        writer = csv.DictWriter(player_file,fieldnames=fields)
        writer.writeheader()
        writer.writerows(player_list)
    return

#in the beginning...
def game_start():
    """First portion of hue-peli, lets you select/delete your player or create a new one"""
    print("Welcome to working title hue-peli\nChoose an option from below\n\n(1) I've played these games before\n(2) Create user\n(3) Delete user\n")
    
    valid_options = ["1","2","3"]
    while True:
        option = input("Enter the number of the option you choose: ")
        if option in valid_options:
            if option == "1":
                print()
                player_selection()
            elif option == "2":
                print()
                player_creation()
            else:
                print()
                player_deletion()
        else:
            print("\nWhat you entered was not very zen\n")
    
#selects your user tag to begin the game
def player_selection():
    """Helps you select your username and begin the game with your data"""
    player_list = player_data_loader()
    while True:
        found = False
        tag = input("Enter your username: ")
        tag = tag.upper()
        if tag == "BACK":
            print()
            return
        for data in player_list:
            if data["username"] == tag:
                user = data
                found = True
                break
        if found == True:
            break
        else:
            print("\nNo match was found\n")
    print()
    to_hue(user)

#creates a user for yourself
def player_creation():
    """Helps create a three letter username for yourself, all other data is predefined"""
    player_list = player_data_loader()
    alphabet = "ABCDEFGHIJKLMNOPQRSTYVWXYZÅÄÖ"
    print("Create your username, three letters from AAA-ÖÖÖ\n")
    
    while True:
        name = input("Name: ")
        name = name.upper()
        if name == "BACK":
            print()
            return
        #length check
        if len(name) != 3:
            print("\nYour username isn't three characters long\n")
            continue
        name = name.upper()
        #wrong character check
        invalid_characters = False
        for letter in name:
            if letter not in alphabet:
                invalid_characters = True
        if invalid_characters == True:
            print("\nYour username contains something it shouldn't\n")
            continue
        #pre-existing check:
        duplicate_name = False
        for dictionary in player_list:
            if dictionary["username"] == name:
                duplicate_name = True
                break
        if duplicate_name == True:
            print("\nThat username already exists\n")
            continue
        #confirmation
        print(f"\nIs {name} the username you want to go with?\n\n(1) Yes\n(2) No\n")
        done = True
        while True:
            confirmation = input("Is this you?: ")
            if confirmation == "1":
                break
            elif confirmation == "2":
                print()
                done = False
                break
            else:
                print("\nWhat you entered was not very zen\n")
        if done == False:
            continue
        #new player dict creation
        new_player = {}
        new_player["username"] = name
        new_player["incomplete_levels"] = ['1.1', '1.2', '1.3', '2.1', '2.2', '2.3', '3.1', '3.2', '3.3']
        new_player["complete_levels_best"] = {}
        player_list.append(new_player)
        player_data_writer(player_list)
        break
    print()
    to_hue(new_player)

#deletes a user
def player_deletion():
    """Helps you delete a player and then goes back to game_start"""
    player_list = player_data_loader()
    
    while True:
        tag = input("Enter the username for deletion: ")
        tag = tag.upper()
        if tag == "BACK":
            print()
            return
        copy_list = []
        deleted = False
        for data in player_list:
            if data["username"] != tag:
                copy_list.append(data)
            else:
                print(f"\nDeleted {tag}\n")
                deleted = True
        if deleted == True:
            player_data_writer(copy_list)
            game_start()
        else:
            print("\nNo match was found\n")
            
#test function
def to_hue(player_data):
    print(player_data)

#some code should be integrated in player data loading
def score_comparison(player_tag: str, level_number: str, move_count):
    """logic for player moveset comparison"""
    #chooses player data based on tag and makes calculations based on scores
    #player data
    player_list = player_data_loader()

    #separate the player from the rest
    new_player_list = []
    for dict in player_list:
        if dict["username"] == player_tag:
            player_data = dict
        else:
            new_player_list.append(dict)

    #puts in the data straight away if the level wasn't complete before
    if level_number in player_data["incomplete_levels"]:
        player_data["incomplete_levels"].remove(level_number)
        player_data["complete_levels_best"][level_number] = move_count
        old_move_count = 0
    
    #if the particular level data exists it compares and then inputs
    else:
        old_move_count = player_data["complete_levels_best"][level_number]
        if move_count < player_data["complete_levels_best"][level_number]:
            player_data["complete_levels_best"][level_number] = move_count

    #global rank counter
    new_player_list.append(player_data)
    global_level_score = {}
    for dict in new_player_list:
        try:
            global_level_score[dict["username"]] = dict["complete_levels_best"][level_number]
        except IndexError:
            pass
    global_score_list = sorted(global_level_score.items(), key=lambda item: item[1])

    #The rank is also based on shared positions. All same scores are put in the same rank, and the following rank is increased by x-1 where x is the amount of entries in a shared rank
    rank_counter = 0
    next_rank_change = 0
    old_entry = -1
    for entry in global_score_list:
        if entry[1] != old_entry:
            rank_counter += 1
            rank_counter += next_rank_change
            next_rank_change = 0
        elif entry[1] == old_entry:
            next_rank_change += 1
        if entry[0] == player_tag:
            break
        old_entry = entry[1]

    #score countings
    print()
    if old_move_count == 0:
        print("Your first score is your best score")
        print(f"Score: {move_count}\n")
    elif move_count > old_move_count:
        print("This isn't your best score")
        print(f"Current score: {move_count}")
        print(f"Best score: {old_move_count}\n")
    elif move_count < old_move_count:
        print("This is your best score")
        print(f"New best score: {move_count}")
        print(f"Old best score: {old_move_count}\n")
    elif move_count == old_move_count:
        print("This score is tied with a previous best score")
        print(f"Score: {move_count}\n")
    print(f"Globally you are ranked: {rank_counter}")

    #IMPORTANT: below is the file writer, disabled for testings
    #player_data_writer(new_player_list)
    
        

os.system("cls")
#game_start()
#test
player_list = player_data_loader()
player_data_writer(player_list)

score_comparison("SAM","1.1",21)
