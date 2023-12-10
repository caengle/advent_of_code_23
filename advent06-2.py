#!/usr/bin/python3

import re

def get_limits(time, record):
    min = time
    max = 0
    for i in range (0, time):
        j = time - i
        lower = (time - i) * i
        upper = (time - j) * j
        if i < min and lower > record:
            min = i
        if j > max and upper > record:
            max = j
    #print("\ntime:",time, "\ndistance:", record, "\nmin:", min, "\nmax:", max, "\nrange:", max-min+1)
    return max - min + 1

def main():
    f = open("test.txt", "r")
    input = f.readlines()
    time = ''.join(input[0].split()[1:])
    distance = ''.join(input[1].split()[1:])
    print(time, distance)
    
    print(get_limits(int(time), int(distance)))

if __name__ == "__main__":
    main()
