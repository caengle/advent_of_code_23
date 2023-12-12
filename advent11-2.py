#!/usr/bin/python3
import re

def find_distance(galaxyA, galaxyB, universe):
    x0 = int(galaxyA[0])
    y0 = int(galaxyA[1])
    x1 = int(galaxyB[0])
    y1 = int(galaxyB[1])
    startx = x0
    endx = x1
    starty = y0
    endy = y1
    if x1 < x0:
        startx = x1
        endx = x0
    if y1 < y0:
        starty = y1
        endy = y0
    distance = 0
    #print(galaxyA, galaxyB, (startx, starty), (endx, endy))
    
    for y in range(starty+1, endy+1):
        if universe[y][startx] == 'x':
            distance+=1000000
        else:
            distance+=1
        #print(universe[y][startx])

    for x in range(startx+1, endx+1):
        if universe[starty][x] == 'x':
            distance+=1000000
        else:
            distance+=1
        #print(universe[starty][x])

    #print("distance",distance)
    return distance

def main():
    sum = 0
    f = open("test.txt", "r")
    lines = f.readlines()
    lines[0] = lines[0][3:]

    i = 0
    while i < len(lines):
        lines[i] = lines[i].strip()
        if re.search(r'#', lines[i]):
            i+=1
        else:
            lines[i] = 'x'*len(lines[0])
            i+=2

    i = 0
    while i < len(lines[0]):
        curr = ''
        for line in lines:
            curr += (line[i])
        if re.search(r'#', curr):
            i+=1
        else:
            for j in range(0, len(lines)):
                lines[j] = lines[j][:i] + 'x' + lines[j][i+1:]
            i+=2
    #print(lines)
    i = 0
    j = 0
    galaxies = []
    for i in range(0, len(lines)):
        for j in range(0, len(lines[0])):
            if lines[i][j]=='#':
                galaxies.append((j, i))
    #print("galaxies", galaxies)
    i = 0
    j = 0
    for i in range(0, len(galaxies)):
        for j in range(i+1, len(galaxies)):
            sum += find_distance(galaxies[i], galaxies[j], lines)

   
    print(sum)

if __name__ == "__main__":
    main()
