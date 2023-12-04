#!/usr/bin/python3

import re

def get_maximums(game):
    red_max = 0
    blue_max = 0
    green_max = 0  
    red_curr = 0
    blue_curr = 0 
    green_curr = 0
    
    number_pattern=re.compile(r'\d+')
    color_pattern=re.compile(r'red|green|blue')
    start_index = game.find(":")
    colors = color_pattern.findall(game[start_index:])
    numbers = number_pattern.findall(game[start_index:])
    pairs = zip(colors, numbers)

    for pair in pairs:
        if pair[0] == "red":
            red_curr = int(pair[1])
            if red_curr > red_max:
                red_max = red_curr
        elif pair[0] == "green":
            green_curr = int(pair[1])
            if green_curr > green_max:
                green_max = green_curr
        elif pair[0] == "blue":
            blue_curr = int(pair[1])
            if blue_curr > blue_max:
                blue_max = blue_curr
    
    return (red_max, green_max, blue_max)

def get_id(game):
    pattern = re.compile(r'\d+')
    id = int(pattern.findall(game)[0])
    return id

def main():
    sum = 0
    f = open("input02.txt", "r")
    games = f.readlines()
    for game in games:
        maximums = get_maximums(game)
        sum+=maximums[0]*maximums[1]*maximums[2]
    print(sum)
if __name__ == "__main__":
    main()
