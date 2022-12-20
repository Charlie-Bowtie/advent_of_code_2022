def find_start_of_packet(path):

    with open(path) as infile:
        content = infile.read()

        st = []  # signal tracker
        letters_processed = 0

        for letter in content:
            st.append(letter)
            letters_processed += 1
            if len(st) > 4:
                del st[0]
                if st[0] not in st[1:4] and st[1] not in st[2:4] and st[2] not in st[0::3]:
                    break

    print(letters_processed, st)


def find_start_of_message(path):

    with open(path) as infile:
        content = infile.read()

        st = set()  # signal tracker
        sp = []
        letters_processed = 13
        index = 0
        index2 = 14
        keep_runnning = True

        while keep_runnning:
            packet = content[index:index2]
            letters_processed += 1

            for letter in packet:
                st.add(letter)
                sp.append(letter)

            if len(st) == 14:
                keep_runnning = False
            else:
                st.clear()
                sp.clear()

            index += 1
            index2 += 1

    print(letters_processed, st, sp[:-1])


if __name__ == "__main__":
    # find_start_of_packet("signal.txt")
    find_start_of_message("signal.txt")
