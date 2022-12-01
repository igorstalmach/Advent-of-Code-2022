with open('day1/day1.txt', mode='r') as file:
    data = file.read()

# Divide calories into lists representing elves
data = data.split('\n\n')

# Storing max values of calories
max_val = [0, 0, 0]

# Parse and sum values for a single elf
for line in data:
    # Divide values into list elements (numbers are divided with '\n')
    line = line.split('\n')

    # Map string to int and sum
    temp_max = sum(map(int, line))

    # Compare with previous max values
    for i in range(3):
        if temp_max > max_val[i]:
            max_val.insert(i, temp_max)
            break
 
print(f"Total calories of the Elf carrying the most: {max_val[0]}")
print(f"Total calories of three of the Elves carrying the most: {sum(max_val[:3])}")
