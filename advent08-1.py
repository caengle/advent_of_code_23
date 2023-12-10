#!/usr/bin/python3

import re

def main():
    f = open("test.txt", "r")
    input = f.readlines()
    pattern = input[0].strip()
    pattern = pattern.replace("L", "0")
    pattern = pattern.replace("R", "1")
    instructions = {}
    for i in range(2, len(input)):
        letters = re.findall(r'[A-Z]+',input[i])
        instructions.update({letters[0] : letters[1:]})
    curr = 'AAA'
    length = 0
    i=0
    while curr != 'ZZZ':
        length+=1
        curr = instructions[curr][int(pattern[i])]
        i+=1
        if i > len(pattern) - 1:
            i=0
    print(length)

if __name__ == "__main__":
    main()
