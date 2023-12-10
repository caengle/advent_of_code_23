#!/usr/bin/python3

import re

def main():
    total_cards = 0
    f = open("test.txt", "r")
    card_table = f.readlines()
    match_map = []
    for card in card_table:
        card = card.split('|')
        card[0] = card[0][card[0].find(':')+1:].split()
        card[1] = card[1].split()
        match_map.append((1, card[0], card[1]))
    #print(match_map)

    for i in range(0, len(match_map)):
        matches = 0
        for number in match_map[i][2]:
            for winning_number in match_map[i][1]:
                if number == winning_number:
                    matches += 1
        j=i+1
        while j < len(match_map) and j < i + matches + 1:
            #print(match_map)
            match_map[j] = (match_map[j][0]+match_map[i][0], match_map[j][1], match_map[j][2])
            j+=1
        total_cards+=match_map[i][0]

    print(total_cards)

if __name__ == "__main__":
    main()
