

lost = {'C': 'A', 'A': 'B', 'B': 'C'}
wins = {'A': 'C', 'B': 'A', 'C': 'B'}
score = {'A': 1, 'B': 2, 'C': 3}


def rps_scoring(they_move, signal):

    they_points = 0
    me_points = 0

    they_points += score[they_move]

    if signal == 'Z':
        me_move = lost[they_move]
        me_points += 6
    elif signal == 'X':
        me_move = wins[they_move]
        they_points += 6
    else:
        me_move = they_move
        they_points += 3
        me_points += 3

    me_points += score[me_move]

    return [they_points, me_points]


def check_stratguide(path):

    my_score = 0
    their_score = 0

    with open(path) as infile:
        contents = infile.readlines()

        for line in contents:
            game = line.rstrip().split(" ")
            they_move = game[0]
            signal = game[1]
            points = rps_scoring(they_move, signal)
            their_score += points[0]
            my_score += points[1]

    print(f"My score be {my_score} and they score be {their_score}")


if __name__ == "__main__":
    check_stratguide('rps.txt')