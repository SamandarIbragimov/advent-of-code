part1 = { 'A X': 4, 'A X\n':4, 'A Y': 8, 'A Y\n': 8, 'A Z': 3, 'A Z\n':3, 'B X': 1, 'B X\n': 1, 'B Y': 5, 'B Y\n':5, 'B Z': 9, 'B Z\n': 9, 'C X': 7, 'C X\n':7, 'C Y': 2, 'C Y\n':2, 'C Z': 6, 'C Z\n':6, }
part2 = { 'A X': 3, 'A X\n':3, 'A Y': 4, 'A Y\n': 4, 'A Z': 8, 'A Z\n':8, 'B X': 1, 'B X\n': 1, 'B Y': 5, 'B Y\n':5, 'B Z': 9, 'B Z\n': 9, 'C X': 2, 'C X\n':2, 'C Y': 6, 'C Y\n':6, 'C Z': 7, 'C Z\n':7, }
with open('day_2_input.txt', 'r') as f:
    lines = f.readlines()
    print ("Part 1: ", sum([part1[play] for play in lines]))
    print ("Part 1: ", sum([part2[play] for play in lines]))
