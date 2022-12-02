with open('day2/day2.txt', mode='r') as file:
    data = file.read()
    data = data.split('\n')

# Calculate game results
validate = {
    'A X': 3 + 1,
    'A Y': 6 + 2,
    'A Z': 0 + 3,
    'B X': 0 + 1,
    'B Y': 3 + 2,
    'B Z': 6 + 3,
    'C X': 6 + 1,
    'C Y': 0 + 2,
    'C Z': 3 + 3
}

# Convert according to the elf's secret strategy
strategy = {
    'A X': 'A Z',
    'A Y': 'A X',
    'A Z': 'A Y',
    'B X': 'B X',
    'B Y': 'B Y',
    'B Z': 'B Z',
    'C X': 'C Y',
    'C Y': 'C Z',
    'C Z': 'C X'
}

total_1 = 0
total_2 = 0

for i in range(0, len(data)):
    total_1 += validate[data[i]]
    total_2 += validate[strategy[data[i]]]

print(f"Total score if everything goes exactly according to the strategy guide: {total_1}")
print(f"Total score if everything goes exactly according to the secret strategy guide: {total_2}")
