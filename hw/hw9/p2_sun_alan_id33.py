def unique_squares_one_player(directions):
    """
    "w" moves the player north
    "a" moves the player west
    "s" moves the player south
    "d" moves the player east
    After following all of the directions in the input snippet, how many unique
    squares were visited by the player?
    :param directions: a string of characters consisted of 'w', 'a', 's', 'd' that denotes the direction of movement
    of the player.
    :return: int that represents how many unique squares that the player has gone to.
    """
    coordinates = []  # a list of coordinates of where the player has stepped
    starting_coordinate = [0, 0]  # a list that keeps track of the current position of the player starting at 0, 0
    nunique = 0
    for step in directions:
        if step == 'w':  # direction testing
            starting_coordinate[1] += 1  # increment y coordinate
        elif step == 's':
            starting_coordinate[1] -= 1  # decrement y coordinate
        elif step == 'd':
            starting_coordinate[0] += 1  # increment x coordinate
        elif step == 'a':
            starting_coordinate[0] -= 1  # decrement x coordinate
        coordinates.append(starting_coordinate.copy())
    print(coordinates)
    for coordinate in coordinates:
        if coordinates.count(coordinate) == 1:
            nunique += 1
    return nunique


def unique_squares_two_players(directions):
