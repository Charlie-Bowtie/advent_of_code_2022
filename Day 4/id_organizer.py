import re


def find_me_the_answer_1(path):

    total = 0

    with open(path) as infile:
        content = infile.readlines()

        for line in content:
            pair = list(map(int, re.split('-|,', line)))

            if pair[0] == pair[1] or pair[2] == pair[3]:
                if pair[0] in range(pair[2], pair[3] + 1) or\
                        pair[2] in range(pair[0], pair[1] + 1):
                    total += 1
            elif pair[0] <= pair[2] and pair[1] >= pair[3]:
                total += 1
            elif pair[2] <= pair[0] and pair[3] >= pair[1]:
                total += 1

    print(f"Someone f*ed up {total} assignments")


def find_me_thepart2_answer(path):

    total = 0

    with open(path) as infile:
        content = infile.readlines()

        for line in content:
            pair = list(map(int, re.split('-|,', line)))

            if pair[0] in list(range(pair[2], pair[3] + 1)) or\
               pair[2] in list(range(pair[0], pair[1] + 1)):
                total += 1

    print(f"Someone f*ed up {total} assignments")


if __name__ == "__main__":
    find_me_the_answer_1("ids.txt")
    find_me_thepart2_answer("ids.txt")
