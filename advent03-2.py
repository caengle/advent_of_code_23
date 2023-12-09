#!/usr/bin/python3

import re

def get_num(engine, x, y):
    num = engine[y][x]
    i = x
    while i > 0:
        i-=1
        curr = engine[y][i]
        if curr.isdigit():
            num = curr+num
        else:
            break
    i = x
    while i < len(engine[0])-1:
        i+=1
        curr = engine[y][i]
        if curr.isdigit():
            num = num + curr
        else:
            break
    return int(num)

def check_adjacent_numbers(engine, x, y):
    adjacent_numbers = []
    x0 = x
    x1 = x
    y0 = y
    y1 = y
    if x > 0:
        x0 = x - 1
    if y > 0:
        y0 = y - 1
    if x < len(engine[0]) - 1:
        x1 = x + 1
    if y < len(engine) - 1:
        y1 = y + 1

    prev_num = False
    if y != 0:
        for i in range(x0, x1+1):
            print(x,y,engine[y0][i])
            if engine[y0][i].isdigit():
                if prev_num == False:
                    adjacent_numbers.append((i,y0))
                    prev_num = True
            else:
                prev_num = False

    prev_num = False                
    if y != len(engine) - 1:
        for i in range(x0, x1+1):
            if engine[y1][i].isdigit():
                if prev_num == False:
                    adjacent_numbers.append((i,y1))
                    prev_num = True
            else:
                prev_num = False
                
    if x != 0:
        if engine[y][x0].isdigit():
            adjacent_numbers.append((x0,y))
    if x != len(engine[0]) - 1:
        if engine[y][x1].isdigit():
            adjacent_numbers.append((x1,y))
    return(adjacent_numbers)    

def main():
    sum = 0
    f = open("test.txt", "r")
    engine = f.readlines()
    for i in range(len(engine)):
        engine[i] = engine[i].strip()
        for j in range(len(engine[i])):
            if engine[i][j] == '*':
                #print(j,i)
                adjacent_numbers = check_adjacent_numbers(engine, j, i)
                if len(adjacent_numbers) == 2:
                    print(adjacent_numbers)
                    sum += get_num(engine, adjacent_numbers[0][0], adjacent_numbers[0][1]) * get_num(engine, adjacent_numbers[1][0], adjacent_numbers[1][1])
    print(sum)

if __name__ == "__main__":
    main()
