with open('items_game.txt', 'r') as f:
    for line in f:
        if 'item_logname' in line:
            print(line)