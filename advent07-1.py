#!/usr/bin/python3
import re

class HandValPos:
    def __init__(self, val, pos):
        self.val = val
        self.pos = pos
    def __repr__(self):
        return repr((self.val, self.pos))

def get_hand_type_value(hand):
    pair1 = ''
    pair2 = ''
    three_kind = ''
    four_kind = ''
    five_kind = ''
    
    for i in range(0, len(hand)):
        curr_card = hand[i]
        repeat = False
        if i != 0:
            for card in hand[:i]:
                if card == curr_card:
                    repeat = True
        if repeat != True:
            for card in hand[i+1:]:
                if card == curr_card:
                    if card == pair1:
                        pair1 = ''
                        three_kind = card
                    elif card == pair2:
                        pair2 = ''
                        three_kind = card
                    elif card == three_kind:
                        three_kind = ''
                        four_kind= card
                    elif card == four_kind:
                        four_kind == ''
                        five_kind = card
                    elif pair1 == '':
                        pair1 = card
                    elif pair2 == '':
                        pair2 = card
    if five_kind != '':
        return '7'
    elif four_kind != '':
        return '6'
    elif three_kind != ''  and pair1 != '':
        return '5'
    elif three_kind != '':
        return '4'
    elif pair2 != '':
        return '3'
    elif pair1 != '':
        return '2'
    return '1'

def get_hand_value(hand):
    value = []
    value.append(get_hand_type_value(hand))
    for i in range (0, 5):
        if hand[i] == 'A':
            value.append('E')
        elif hand[i] == 'K':
            value.append('D')
        elif hand[i] == 'Q':
            value.append('C')
        elif hand[i] == 'J':
            value.append('B')
        elif hand[i] == 'T':
            value.append('A')
        else:
            value.append(hand[i])
    return value




def main():
    sum = 0
    f = open("input07.txt", "r")
    hands_bets = f.readlines()
    hand_values = []

    for i in range(0, len(hands_bets)):
        hands_bets[i] = hands_bets[i].split()
        hand_values.append(HandValPos((int(''.join(get_hand_value(hands_bets[i][0])), 16)), i))

    hand_values = sorted((hand_values), key = lambda hand: hand.val)
    for i in range(0, len(hand_values)):
        sum += (i + 1) * int(hands_bets[hand_values[i].pos][1])
    print(sum)

if __name__ == "__main__":
    main()
