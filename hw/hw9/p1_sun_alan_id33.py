import random
import os


def final_floor(directions):
    """
    First part of problem 1
    :param directions: str that contains '[' and ']' to denote going up and going down floors respectively.
    :return: int that denotes the final floor that Mary ends up on based on the given directions.
    """
    return directions.count('[') - directions.count(']')  # total floor increase  - total floor decrease


def first_basement(directions):
    """
    Second part of problem 1
    Where the number of the first direction that brings Mary into the basement is returned
    :param directions: str that contains '[' and ']' to denote going up and going down floors respectively.
    :return: int position of the character that brings Mary into the basement
    """
    floor_count = 0  # starting floor
    for position, step_direction in enumerate(directions):
        if step_direction == '[':
            floor_count += 1
        else:
            floor_count -= 1
        if floor_count < 0:  # Mary is in the basement
            return position + 1  # Since the first position counts as 1 not 0


def visited_three_times(directions):
    """
    Third part of problem 1
    :param directions: str that contains '[' and ']' to denote going up and going down floors respectively.
    :return: int first floor that Mary visits three times
    """
    floor_count = 0  # starting floor
    floor_dict = {0: 1}  # dictionary whose key is floor number and value is number of times visited
    for step_direction in directions:
        floor_count += 1 if step_direction == '[' else -1  # adding floors accoriding to the given: [ -> +1; ] -> -1
        if floor_count not in floor_dict.keys():  # add new floor to dictionary
            floor_dict[floor_count] = 1
        else:  # increment number of visits to a floor already visited
            floor_dict[floor_count] += 1
        if 3 in floor_dict.values():  # search if any floor value has been visited three times
            for floor in floor_dict:
                if floor_dict[floor] == 3:  # test for floor that has been visited three times
                    return floor


def kudos():
    """
    Creates a 10,000 character puzzle and solves it using the three functions above
    :return: tuple index 0 contains the directions, index 1 contains a list of solutions
    """
    direct = ""  # string of directions for generated problem
    solutions = [0, 0, 0]  # three solutions for three parts of the problem
    for i in range(10000):
        direct += '[' if random.randint(1, 2) == 1 else ']'  # generate random character to add to directions
    solutions[0] = final_floor(direct)  # using solution functions above
    solutions[1] = first_basement(direct)
    solutions[2] = visited_three_times(direct)
    return direct, solutions


if __name__ == '__main__':
    f_in = open('p1_id33_input.txt').readline().strip()  # opened input file
    print(final_floor(f_in))
    print(first_basement(f_in))
    print(visited_three_times(f_in))

    # Kudos
    directions, solutions = kudos()
    f_out_directions = open('kudos/kudos_directions.txt', 'w')
    f_out_directions.write(directions)
    f_out_directions.close()

    f_out_solutions = kudos()  # *
    f_out_solutions = open('kudos/kudos_solutions.txt', 'w')
    f_out_solutions.write('\n'.join(map(str, solutions)))  # convert list values to strings for concatenation


