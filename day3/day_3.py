#!/usr/bin/env python

with open("input", "r") as f:
    m_1 = 1
    t_1 = 0
    x_1 = 0

    m_2 = 3
    t_2 = 0
    x_2 = 0

    m_3 = 5
    t_3 = 0
    x_3 = 0

    m_4 = 7
    t_4 = 0
    x_4 = 0

    m_5 = 0.5
    t_5 = 0
    x_5 = 0

    trees = 0
    for line in f:
        # Get rid of newline...
        line = line.strip()
        length = len(line)

        # t_1
        if line[x_1 % length] == '#':
            t_1 += 1
        x_1 += m_1

        # t_2
        if line[x_2 % length] == '#':
            t_2 += 1
        x_2 += m_2

        # t_3
        if line[x_3 % length] == '#':
            t_3 += 1
        x_3 += m_3

        # t_4
        if line[x_4 % length] == '#':
            t_4 += 1
        x_4 += m_4

        # t_5
        if int(x_5) == x_5 and line[int(x_5) % length] == '#':
            t_5 += 1
        x_5 += m_5

    print("Part 1: %d " % (t_2))
    print("Part 2: %d\n\tt_1: %d\n\tt_2: %d\n\tt_3: %d\n\tt_4: %d\n\tt_5: %d" %(t_1*t_2*t_3*t_4*t_5, t_1, t_2, t_3, t_4, t_5))
