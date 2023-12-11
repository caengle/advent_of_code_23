#!/usr/bin/python3

def main():
    sum = 0
    f = open("input.txt", "r")
    reports = f.readlines()
    for i in range(0, len(reports)):
        reports[i] = reports[i].split()
    for report in reports:
        print("report:",report)
        sequences = [report]
        not_all_zeroes = True
        while not_all_zeroes:
            diffs = []
            not_all_zeroes = False
            curr = sequences[len(sequences) - 1]
            #print("curr:",curr)
            for i in range(0, len(curr) - 1):
                diff = abs(int(curr[i]) - int(curr[i+1]))
                diffs.append(diff)
                if diff != 0:
                    not_all_zeroes = True
            curr = diffs
            sequences.append(diffs)
            print(diffs)
        prediction = 0
        i = len(sequences) - 1
        #print(sequences)
        sequences[i].append(0)
        print(sequences[i - 1])
        while i > 0:
            sequences[i - 1].append(int(sequences[i - 1][len(sequences[i - 1]) - 1]) + int(sequences[i][len(sequences[i]) - 1]))
            i -= 1
        sum += sequences[0][len(sequences[0]) - 1]
        for line in sequences:
            print(line)
    print(sum)

if __name__ == "__main__":
    main()
