#!/usr/bin/env python

def validate_passport(passport_string):
    passport_dict = {field[0]: field[1] for field in [field.split(":") for field in passport_string.split()]}
    hex_set = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    required_fields = {
        'byr': lambda v: v.isnumeric() and int(v) >= 1920 and int(v) <= 2002,
        'iyr': lambda v: v.isnumeric() and int(v) >= 2010 and int(v) <= 2020,
        'eyr': lambda v: v.isnumeric() and int(v) >= 2020 and int(v) <= 2030,
        'hgt': lambda v: (
                len(v) == 5 and v.endswith('cm') and v[:3].isnumeric() and int(v[:3]) >= 150 and int(v[:3]) <= 193
            ) or (
                len(v) == 4 and v.endswith('in') and v[:2].isnumeric() and int(v[:2]) >= 59 and int(v[:2]) <= 76
            ),
        'hcl': lambda v: (
            len(v) == 7 and v.startswith('#') and len(set(list(v[1:].upper()) + hex_set)) == 16
        ),
        'ecl': lambda v: v in eye_colors,
        'pid': lambda v: len(v) == 9 and v.isnumeric(),
    }

    valid = True
    for field in required_fields:
        if field not in passport_dict:
            valid = False
            break

        if not required_fields[field](passport_dict[field]):
            valid = False
            break

    return valid

with open("input", "r") as f:

    line = f.readline()
    passport_string = ""
    valid_passports = 0

    while line:
        line = line.strip()

        if line:
            passport_string += " %s" % (line)

        line = f.readline()

        if (line == '\n' or not line):
            if validate_passport(passport_string):
                valid_passports += 1
            passport_string = ""

print(valid_passports)
