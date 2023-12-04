#!/usr/bin/python3
import re
from word2number import w2n

def get_num(line):
    first_digit_pattern = re.compile(r'(?=(\d|zero|one|two|three|four|five|six|seven|eight|nine))')
    digits = first_digit_pattern.findall(line)
    if len(digits) > 0:
        return int(str(w2n.word_to_num(digits[0])) + str(w2n.word_to_num(digits[len(digits)-1])))
    else: 
        return 0


def main():
    f = open("input.txt", "r")
    lines = f.readlines()
    sum = 0
    for line in lines:
        sum+=get_num(line)
    print(sum)

if __name__ == "__main__":
    main()
