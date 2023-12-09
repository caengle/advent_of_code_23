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

def get_gear_ratio(num_coor, x, y, width):
    ratio = 0
    nums = []

    for i in range(0, len(num_coor[y])):
        if (y > 0 and x >= num_coor[y-1][1][i][0] - 1 and x <= num_coor[y-1][1][i][1] + 1):
            nums.append(num_coor[y-1][0][i])
        if (y < len(num_coor) - 1 and x >= num_coor[y+1][1][i][0] - 1 and x <= num_coor[y+1][1][i][1] + 1):
            nums.append(num_coor[y+1][0][i])
        if (x > 0 and y == i and x == num_coor[y][1][i][0] - 1) or (x < width - 1 and x > 0 and y == i and x == num_coor[y][1][i][0] + 1):
            nums.append(num_coor[y+1][0][i])
    if len(nums) == 2:
        ratio = int(nums[0]) * int(nums[1])
    return ratio

def main():
    sum = 0
    f = open("test.txt", "r")
    engine = f.readlines()
    num_coor = []
    #[([10, 20, 30], [(1, 2), (3, 4)]), ([10, 20, 30], [(1, 2), (3, 4)])]
    for i in range(0, len(engine)):
        engine[i] = engine[i].strip()
    for i in range(0, len(engine)):
        num_coor.append(get_coordinates(engine[i]))
    print(num_coor)
    for y in range(0, len(engine)):
        for x in range(0, len(engine[y])):
            #print(x,y)
            if re.search(r'\*', engine[y][x]) != None:
                sum += get_gear_ratio(num_coor, x, y, len(engine[0]))

    print(sum)

if __name__ == "__main__":
    main()
