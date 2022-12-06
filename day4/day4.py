with open('day4/day4.txt', mode='r') as file:
    data = file.read()
    data = data.split('\n')

total1 = 0
total2 = 0

for pair in data:
    # Splits two pairs into two lists
    pair = pair.split(',')

    # Splits a single pair into two numbers
    for i in range(len(pair)):
        pair[i] = list(map(int, pair[i].split('-')))

    # Checks if second pair fully contains first pair
    if (pair[0][0] <= pair[1][0]) and (pair[0][1] >= pair[1][1]):
        total1 += 1
        total2 += 1
    # Checks if first pair fully contains second pair
    elif (pair[1][0] <= pair[0][0]) and (pair[1][1] >= pair[0][1]):
        total1 += 1
        total2 += 1
    # Checks if first pair intersects with second pair from left
    elif (pair[1][1] >= pair[0][0]) and (pair[1][0] <= pair[0][1]):
        total2 += 1
    # Checks if first pair intersects with second pair from right 
    elif (pair[1][0] <= pair[0][1]) and (pair[0][0] <= pair[1][1]):
        total2 += 1


print(f"Number of assignment pairs where one range fully contain the other: {total1}")
print(f"Number of assignment pairs where ranges overlap: {total2}")
