#!/usr/bin/python3
import re

def get_num(line):
    first_digit_pattern = re.compile(r'\d')
    last_digit_pattern = re.compile(r'\d(?=\D*$)')
    first_digit = first_digit_pattern.findall(line)
    last_digit = last_digit_pattern.findall(line)
    return int(first_digit[0]+last_digit[0])


def main():
    f = open("input.txt", "r")
    lines = f.readlines()
    sum = 0
    for line in lines:
        sum+=get_num(line)
    print(sum)

if __name__ == "__main__":
    main()