#!/usr/bin/env python
import sys

def has_addends(num, last_x):
    found_addends = False

    # @note I wish I didn't have to do this everytime
    search_table = sorted(last_x)
    x = 0
    y = len(last_x) - 1
    while x < y:
        sum = search_table[x] + search_table[y]
        if sum < num:
            x += 1
        elif sum > num:
            y -= 1
        else:
            found_addends = True
            break

    return found_addends

def main(argv):
    file = argv[1]
    preamble_size = int(argv[2])

    last_x = []
    with open(file, 'r') as f:
        for line in f:
            num = int(line.strip())
            if len(last_x) < preamble_size:
                last_x.append(num)
            else:
                if not has_addends(num, last_x):
                    print("%d does not have addends..." % (num))
                    break

                last_x.append(num)
                last_x.pop(0)

if __name__ == '__main__':
    main(sys.argv)
