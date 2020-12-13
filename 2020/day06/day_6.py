#!/usr/bin/env python

def part1():
    total_yes = 0
    with open('input', 'r') as f:
        group_set = set()
        line = f.readline()
        while line:
            line = line.strip()
            for char in line:
                group_set.add(char)

            line = f.readline()
            if line == '\n' or not line:
                total_yes += len(group_set)
                group_set = set()

    return total_yes

def part2():
    total_group_yes = 0
    with open('input', 'r') as f:
        group_yes = None

        line = f.readline()
        while line:
            line = line.strip()
            if not line:
                line = f.readline()
                continue

            person_yes = set(line)

            if group_yes is None:
                group_yes = person_yes
            elif person_yes:
                group_yes = group_yes.intersection(person_yes)

            line = f.readline()
            if line == '\n' or not line:
                total_group_yes += len(group_yes)
                group_yes = None

    return total_group_yes

print(part2())
