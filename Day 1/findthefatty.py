def findthefatty(path):

    elfs = []
    elf_inv = []

    with open (path) as infile:
        contents = infile.read()
        chonks = contents.split("\n\n")
        for chonk in chonks:
            elf = chonk.replace("\n", ",")
            elfs.append(elf)
        for e in elfs:
            snacks = map(int, e.split(","))
            snack_count = sum(snacks)
            elf_inv.append(snack_count)
        

    #part 1 answer
    #print (max(elf_inv))
    return elf_inv

def findthefatty_2(elf_inv):

    sorted_elfs = sorted(elf_inv, reverse = True)
    print(sum(sorted_elfs[0:3]))

if __name__ == "__main__":
    elf_inv = findthefatty("elfeat.txt")
    findthefatty_2(elf_inv)
