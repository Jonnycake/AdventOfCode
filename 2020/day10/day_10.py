#!/usr/bin/env python
import sys

def main(argv):
    file = argv[1]

    gaps = {}
    nums = []
    with open(file, 'r') as f:
        nums = list(map(lambda num: int(num), [num for num in f.read().split("\n") if num]))
        nums.sort()

    prev_num = 0
    for num in nums:
        difference = num - prev_num
        gaps[difference] = gaps.get(difference, 0) + 1
        prev_num = num

    gaps[3] = gaps.get(3, 0) + 1

    print(gaps)
    print("Answer: %d" % (gaps.get(1, 0) * gaps.get(3, 0)))
if __name__ == '__main__':
    main(sys.argv)
