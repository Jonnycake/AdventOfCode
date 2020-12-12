#!/usr/bin/env python


def tokenize_string(string):
    instruction = {}

    string = string.split()
    instruction['op'] = string[0]
    instruction['sign'] = string[1][0]
    instruction['arg'] = string[1][1:]

    return instruction

instructions = []
with open("input", "r") as f:
    for line in f:
        instructions.append(tokenize_string(line.strip()))

ip = 0
acc = 0

while ip >= 0 and ip < len(instructions):
    instruction = instructions[ip]
    if 'visited' in instructions[ip]:
        print("Infinite loop detected...acc: %d - ip: %d" % (acc, ip))
        break
    instruction['visited'] = True

    # Avoiding nested ifs with some clever math :P
    is_negative = instruction['sign'] == '-'
    multiplier = 1 - (is_negative * 2)

    if instruction['op'] == 'acc':
        acc += int(instruction['arg']) * multiplier
    elif instruction['op'] == 'jmp':
        ip += int(instruction['arg']) * multiplier
        continue

    ip += 1
