#!/usr/bin/python3

import re

def all_ending(keys):
    for key in keys:
        if key[2] != 'Z':
            return False
    return True

def main():
    f = open("test.txt", "r")
    input = f.readlines()
    pattern = input[0].strip()
    pattern = pattern.replace("L", "0")
    pattern = pattern.replace("R", "1")
    instructions = {}

    for i in range(2, len(input)):
        letters = re.findall(r'[A-Z\d]+',input[i])
        instructions.update({letters[0] : letters[1:]})

    curr_list = []
    for e in list(instructions.keys()):
        if e[2] == 'A':
            curr_list.append(e)
    print(curr_list)
    next = curr_list
    length = 0
    i=0
    endings = {}

    while all_ending(curr_list) != True:
        next = []
        length+=1
        for curr in curr_list:
            next.append(instructions[curr][int(pattern[i])])
        curr_list = next
        i+=1
        if i > len(pattern) - 1:
            i=0

    print(length)

if __name__ == "__main__":
    main()
