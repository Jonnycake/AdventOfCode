#!/usr/bin/env python
import pprint

def tokenize_string(string):
    tokens = []
    delimiters = ' \n'
    ignore = ' \t,.'

    current_token = ""
    for char in string:
        if char in delimiters and len(current_token):
            tokens.append(current_token)
            current_token = ""
            continue

        if char not in ignore:
            current_token += char

    if len(current_token):
        tokens.append(current_token)

    return tokens

def get_container(tokens):
    i = 0

    container = []
    for token in tokens:
        i += 1
        if token == 'contain':
            break

        container.append(token)

    return " ".join(container), tokens[i:]

def get_contents(tokens):
    numbers = '1234567890'
    contents = []

    mode = 'number'
    current_number = 0
    current_content = []
    for token in tokens:
        next = False

        if not current_number and token.isnumeric():
            current_number = int(token)
            continue

        if token in ['bag', 'bags']:
            current_content.append('bags')
            next = True
        else:
            current_content.append(token)

        if next:
            contents += [" ".join(current_content)] * current_number
            current_number = 0
            current_content = []

    if len(current_content):
        contents.append(" ".join(current_content))

    return contents

def parse_tokens(tokens):
    mode = 'container'
    container, remaining = get_container(tokens)
    contents = get_contents(remaining)

    return container, contents


def find_containers(bag):
    containers = set()
    for container in bag.keys():
        containers.add(container)
        containers |= find_containers(bag[container])

    return containers

def find_container_counts(bag, containers, container_counts):
    count = 0
    for content in containers[bag].keys():
        count += container_counts[bag][content]
        count += find_container_counts(content, containers, container_counts) * container_counts[bag][content]

    return count

container_counts = {}
contained = {}
containers = {}
with open('input', 'r') as f:
    for line in f:
        tokens = tokenize_string(line)
        container, contents = parse_tokens(tokens)

        if container not in containers:
            containers[container] = {}

        for content in contents:
            # Find the count of bags in each container...
            if container not in container_counts:
                container_counts[container] = {}
            if content not in container_counts[container]:
                container_counts[container][content] = 1
            else:
                container_counts[container][content] += 1


            # Find what bags contain
            if content not in containers:
                containers[content] = {}
            containers[container][content] = containers[content]

            # Find what contains bag
            if content not in contained:
                contained[content] = {}
            if container not in contained:
                contained[container] = {}
            contained[content][container] = contained[container]

print(find_container_counts('shiny gold bags', containers, container_counts))
