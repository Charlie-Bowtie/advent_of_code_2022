

wins = {'A': 'Z', 'B': 'X', 'C': 'Y', 'X': 'C', 'Y': 'A', 'Z': 'B'}
score = {'X': 1, 'Y': 2, 'Z': 3, 'A': 1, 'B': 2, 'C': 3}


def rps_scoring(they_move, me_move):

    they_points = 0
    me_points = 0

    they_points += score[they_move]
    me_points += score[me_move]

    if they_move == wins[me_move]:
        me_points += 6
    elif me_move == wins[they_move]:
        they_points += 6
    else:
        they_points += 3
        me_points += 3

    return [they_points, me_points]


def check_stratguide(path):

    my_score = 0
    their_score = 0

    with open(path) as infile:
        contents = infile.readlines()

        for line in contents:
            game = line.rstrip().split(" ")
            they = game[0]
            me = game[1]
            points = rps_scoring(they, me)
            their_score += points[0]
            my_score += points[1]

    print(f"My score be {my_score} and they score be {their_score}")


if __name__ == "__main__":
    check_stratguide('rps.txt')
