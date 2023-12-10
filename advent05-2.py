#!/usr/bin/python3

import re
import numpy
import multiprocessing
import time
import os

f = open("test.txt", "r")
input = f.readlines()

def get_map(input):
    map_list = []
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
    return map_list

map_list = get_map(input)

def map_seed(seed):
    mapped = int(seed)
    for maps in map_list:
        for m in maps:
            #print(map)
            if mapped >= int(m[1]) and mapped <= int(m[1]) + int(m[2]) - 1:
                #print(mapped,int(map[1]),int(map[1]) + int(map[2]) - 1)
                #print(mapped,"has been")
                mapped += (int(m[0]) - int(m[1]))
                #print("mapped to",mapped)
                break
        #print(map)
        #print("mapped:",mapped)
    return mapped

def main():
    f = open("test.txt", "r")
    seed_list = numpy.empty(0,dtype=int)
    mapped_list = []
    input = f.readlines()
    seed_ranges = input[0][7:].split()
    i = 0
    while i < len(seed_ranges):
        print(i)
        seed_list = numpy.concatenate((seed_list, numpy.arange(int(seed_ranges[i]), int(seed_ranges[i]) + int(seed_ranges[i+1]))))
        i+=2

    # length = len(input)
    # k = 0
    # for i in range(1, length):
    #     if re.findall(r'[a-z]', input[i]):
    #         j = i + 1
    #         map_list.append([])
    #         while j < length and input[j][0].isdigit():
    #             map_list[k].append(input[j].split())
    #             j+=1
    #         k+=1  

    # for seed in seed_list:
    #     mapped = int(seed)
    #     #print("\nstart:",seed)
    #     for maps in map_list:
    #         for map in maps:
    #             #print(map)
    #             if mapped >= int(map[1]) and mapped <= int(map[1]) + int(map[2]) - 1:
    #                 #print(mapped,int(map[1]),int(map[1]) + int(map[2]) - 1)
    #                 #print(mapped,"has been")
    #                 mapped += (int(map[0]) - int(map[1]))
    #                 #print("mapped to",mapped)
    #                 break
    #         #print(map)
    #         #print("mapped:",mapped)
    #     mapped_list.append(mapped) 
    seed_list_len = len(seed_list)
    start_time = time.time()
    print(seed_list_len)
    mapped_list = list(multiprocessing.Pool(24).map(map_seed, seed_list[:int(seed_list_len/4)]))
    print("25%:", min(mapped_list))
    mapped_list = list(multiprocessing.Pool(24).map(map_seed, seed_list[int(seed_list_len/4):int(seed_list_len/2)]))
    print("50%", min(mapped_list))
    mapped_list = list(multiprocessing.Pool(24).map(map_seed, seed_list[int(seed_list_len/2):int(seed_list_len/2+seed_list_len/4)]))
    print("75%", min(mapped_list))
    mapped_list = list(multiprocessing.Pool(24).map(map_seed, seed_list[int(seed_list_len/2+seed_list_len/4):]))
    print("100%", min(mapped_list))

    end_time = time.time()
    
    elapsed_time = end_time - start_time
    print(f"Time taken to iterate through the list: {elapsed_time} seconds")

    print(min(mapped_list))

if __name__ == "__main__":
    main()
