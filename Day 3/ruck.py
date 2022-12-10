import string


letters = list(string.ascii_lowercase + string.ascii_uppercase)
priorities = {}
number = 0

for letter in letters:
    number += 1
    priorities[letter] = number


def get_total(half1, half2):
    both = []

    for item in half1:
        if item in half2:
            both.append(priorities.get(item))
            break

    return sum(both)


def get_badge(ruck1, ruck2, ruck3):
    badges = []

    for item in ruck1:
        if item in ruck2 and item in ruck3:
            if item not in badges:
                badges.append(item)
            else:
                pass

    badge_priorty = [priorities.get(badge) for badge in badges]

    return sum(badge_priorty)


def group_elfs(rucks, group_size):

    for i in range(0, len(rucks), group_size):
        yield rucks[i:i + group_size]


def get_me_the_first_answer(path):

    total = 0

    with open(path) as infile:
        content = infile.readlines()

        for line in content:
            slice1 = slice(0, len(line) // 2)
            slice2 = slice(len(line) // 2, len(line))

            string1 = line[slice1]
            string2 = line[slice2]

            total += get_total(string1, string2)

    print(total)


def get_me_the_second_answer(path):

    total = 0

    with open(path) as infile:
        content = infile.readlines()
        groups = list(group_elfs(content, 3))

        for group in groups:
            score = get_badge(
                group[0].rstrip(),
                group[1].rstrip(),
                group[2].rstrip())
            total += score

    print(total)


if __name__ == "__main__":
    get_me_the_first_answer("items.txt")
    get_me_the_second_answer("items.txt")
