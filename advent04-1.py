#!/usr/bin/python3

import re

def main():
    total_winnings = 0
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
        #print("pass ",i+1, match_map)

    for card in match_map:
        #print(card[0])
        winnings = 0
        for number in card[2]:
            for winning_number in card[1]:
                if number == winning_number:
                    if winnings == 0:
                        winnings = 1
                    else:
                        winnings = winnings * 2
                    #print("winnings:", winnings, "total:", total_winnings)
        total_winnings += winnings#(winnings * card[0])

    print(total_winnings)

if __name__ == "__main__":
    main()
