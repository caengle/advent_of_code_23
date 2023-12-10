#!/usr/bin/python3

import re

def main():
    f = open("test.txt", "r")
    seed_list = []
    map_list = []
    mapped_list = []
    input = f.readlines()
    seed_list = input[0][7:].split()
    length = len(input)
    k = 0

    for i in range(1, length):
        if re.findall(r'[a-z]', input[i]):
            j = i + 1
            map_list.append([])
            while j < length and input[j][0].isdigit():
                map_list[k].append(input[j].split())
                j+=1
            k+=1
            
    for seed in seed_list:
        mapped = int(seed)
        print("\nstart:",seed)
        for maps in map_list:
            for map in maps:
                print(map)
                if mapped >= int(map[1]) and mapped <= int(map[1]) + int(map[2]) - 1:
                    print(mapped,int(map[1]),int(map[1]) + int(map[2]) - 1)
                    print(mapped,"has been")
                    mapped += (int(map[0]) - int(map[1]))
                    print("mapped to",mapped)
                    break
            #print(map)
            #print("mapped:",mapped)
        mapped_list.append(mapped)

    print(min(mapped_list))

if __name__ == "__main__":
    main()
