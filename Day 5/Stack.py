

def get_stacking(path):

    with open(path) as infile:
        content = infile.read()

        stacks, movements = content.split('\n\n')
        stacks = stacks.splitlines()
        movements = movements.splitlines()

        num_of_stacks = int(max(stacks[-1].split()))

        horizontal_stacks = []
        crates = [[]]
        instructions = []

        for line in stacks:
            l = []
            for i in range(2, num_of_stacks * 4, 4):
                 l.append(line[i - 1])
            horizontal_stacks.append(l)

        
        for i in range(len(horizontal_stacks[0])):
             l = []
             for j in range(len(horizontal_stacks) - 1):
                if horizontal_stacks[j][i] != ' ':
                    l.append(horizontal_stacks[j][i])
             crates.append(l)

        for line in movements:
            l = line.split(" ")
            instruction = []
            for item in l:
                try: 
                    instruction.append(int(item))
                except:
                    pass
            instructions.append(instruction)

    return crates, instructions

def CrateMover_9000(stacks, instructions):
    crates_on_top = []

    for i in instructions:
        s = stacks [i[1]][0:i[0]]
        for cargo in s:
            stacks[i[2]].insert(0, cargo)
        del stacks [i[1]][0:i[0]]

    for stack in stacks:
        try:
            crates_on_top.append(stack[0])
        except:
            pass
            
    print(''.join(crates_on_top))

def CrateMover_9001(stacks, instructions):
     crates_on_top = []

     for i in instructions:
        index = 0
        s = stacks [i[1]][0:i[0]]
        for cargo in s:
            stacks[i[2]].insert(index, cargo)
            index += 1
        del stacks [i[1]][0:i[0]]

     for stack in stacks:
        try:
            crates_on_top.append(stack[0])
        except:
            pass
            
     print(''.join(crates_on_top))


if __name__ == "__main__":
    c, i = get_stacking("stacks.txt")
    #CrateMover_9000(c,i)
    #CrateMover_9001(c,i)
