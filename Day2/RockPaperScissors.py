def RPS():
    print('initializing...')

    combinations = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}
    sum = 0
    with open('data.txt') as file:
        for line in file:
            key = line.strip()
            sum = sum + combinations[key]
    print(sum)
    

RPS()