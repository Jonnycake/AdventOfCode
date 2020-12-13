#!/usr/bin/env python
import pprint
from sys import argv

def tokenize_string(string):
    instruction = {}

    string = string.split()
    instruction['op'] = string[0]
    instruction['sign'] = string[1][0]
    instruction['arg'] = string[1][1:]

    return instruction

def run_code(instructions, output=True, acc=0, ip=0):
    visited = set()
    trace = []
    fault = False
    while ip >= 0 and ip < len(instructions):
        instruction = instructions[ip]
        if ip in visited:
            if output:
                print("Infinite loop detected...acc: %d - ip: %d" % (acc, ip))
                pprint.pprint(trace[::-1])
            fault = True
            break

        visited.add(ip)
        trace.append({
            # Including acc and ip as that allows us to run right
            #  from the changed instruction instead of the whole
            #  program
            'ip': ip,
            'acc': acc,
            'op': instruction['op'],
            'sign': instruction['sign'],
            'arg': instruction['arg'],
        })

        # Avoiding nested ifs with some clever math :P
        is_negative = instruction['sign'] == '-'
        multiplier = 1 - (is_negative * 2)

        if instruction['op'] == 'acc':
            acc += int(instruction['arg']) * multiplier
        elif instruction['op'] == 'jmp':
            ip += int(instruction['arg']) * multiplier
            continue

        ip += 1

    return acc, fault, trace[::-1]

def read_and_tokenize_file(file):
    instructions = []
    with open(file, "r") as f:
        for line in f:
            instructions.append(tokenize_string(line.strip()))

    return instructions

def fix_program(instructions, trace):
    instruction_switch = {
        'nop': 'jmp',
        'jmp': 'nop',
    }
    for instruction in trace:
        if instruction['op'] not in instruction_switch:
            continue

        ip = instruction['ip']
        acc = instruction['acc']
        instruction_original_op = instruction['op']
        instructions[ip]['op'] = instruction_switch[instruction['op']]
        res_acc, fault, trace = run_code(instructions, output=False, ip=ip, acc=acc)
        if not fault:
            print("Found a fix...%d change from %s to %s..Returns: %d" % (ip, instruction_original_op, instructions[ip]['op'], res_acc))

        # Reset for the next loop
        instructions[ip]['op'] = instruction_original_op

def main(file):
    instructions = read_and_tokenize_file(file)
    acc, fault, trace = run_code(instructions)

    if fault:
        fix_program(instructions, trace)

if __name__ == '__main__':
    main(argv[1])
