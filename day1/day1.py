with open('day1/day1.txt', mode='r') as file:
    data = file.read()

# Divide calories into lists representing elves
data = data.split('\n\n')
elves = []

# Parse and sum values for a single elf
for line in data:
    # Divide values into list elements (numbers are divided with '\n')
    line = line.split('\n')
    # Map string to int and sum
    elves.append(sum(map(int, line)))
        

elves = sorted(elves)
print(f"Total calories of the Elf carrying the most: {elves[-1]}")
print(f"Total calories of three of the Elves carrying the most: {sum(elves[-3:])}")