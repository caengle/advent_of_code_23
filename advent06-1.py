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
    product = 1
    f = open("test.txt", "r")
    input = f.readlines()
    times = input[0].split()[1:]
    distances = input[1].split()[1:]
    times_distances = list(zip(times, distances))
    
    for time, distance in times_distances:
        product *= get_limits(int(time), int(distance))

    print(product)

if __name__ == "__main__":
    main()
