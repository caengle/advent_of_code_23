#!/usr/bin/python3

import re

def get_coordinates(line):
    coordinates = []
    pattern = re.compile(r'\d+')
    numbers = pattern.findall(line)
    x_start = 0
    num = ''
    curr = '.'
    prev = '.'

    for i in range(len(line)):
        curr = line[i]
        if not prev.isdigit() and curr.isdigit():
            x_start = i
            if i == len(line) - 1:
                coordinates.append((x_start, i))
        elif prev.isdigit() and curr.isdigit():
            num += curr
            if i == len(line) - 1:
                coordinates.append((x_start, i))
        elif prev.isdigit() and not curr.isdigit():
            coordinates.append((x_start, i - 1))
        prev = curr

    return(numbers, coordinates)
        
def is_part(y0, x0, x1, engine):
    x = x0 - 1
    y = y0 - 1
    is_part = False
    while y <= y0 + 1 and y < len(engine):
        if x == x1 + 2 or x == len(engine[y0]):
            y+=1
            x = x0 - 1
        elif re.search(r'[^.0-9\n]', engine[y][x]) != None:
            return True
        else:
            x+=1
    return False

def main():
    sum = 0
    f = open("input03.txt", "r")
    engine = f.readlines()
    
    for i in range(0, len(engine)):
        engine[i] = engine[i].strip()

    for y in range(0, len(engine)):
        num, coor = get_coordinates(engine[y])
        for n, c in zip(num, coor):
            if is_part(y, c[0], c[1], engine):
                sum += int(n)
            

    print(sum)
if __name__ == "__main__":
    main()
