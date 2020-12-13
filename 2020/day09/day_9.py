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

def find_addends(num, nums):
    x = 0
    y = 1

    addends = None
    while y < len(nums) and x < len(nums):
        slice_sum = sum(nums[x:y])

        if slice_sum < num:
            y += 1
        elif slice_sum > num:
            x += 1
        else:
            addends = nums[x:y]
            break

    return addends

def main(argv):
    file = argv[1]
    preamble_size = int(argv[2])

    nums = []
    last_x = []
    invalid_number = None
    with open(file, 'r') as f:
        for line in f:
            num = int(line.strip())
            nums.append(num)
            if len(last_x) < preamble_size:
                last_x.append(num)
            else:
                if not has_addends(num, last_x):
                    print("%d does not have addends..." % (num))
                    invalid_number = num
                    break

                last_x.append(num)
                last_x.pop(0)

    # Part 2 requires we search the whole set, not just a preamble
    addends = find_addends(invalid_number, nums)
    print("Found addends: ", addends)
    min_addend = min(addends)
    max_addend = max(addends)
    addend_sum = min_addend + max_addend
    print("Min: %d ; Max: %d ; Sum: %d" % (min_addend, max_addend, addend_sum))

if __name__ == '__main__':
    main(sys.argv)
