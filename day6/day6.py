with open('day6/day6.txt', mode='r') as file:
    data = file.read()

buffer = list(data[:4])
count = 4

for letter in data[4:]:
    # Checking if no. of unique characters is 4
    if len(set(buffer)) == 4:
        print(f"No. of characters that need to be processed before the first start-of-packet marker: {count}")
        break
    # Otherwise moving one character right 
    else:
        count += 1
        buffer.pop(0)
        buffer.append(letter)

buffer = list(data[:14])
count = 14

for letter in data[14:]:
    # Checking if no. of unique characters is 14
    if len(set(buffer)) == 14:
        print(f"No. of characters that need to be processed before the first start-of-message marker: {count}")
        break
    # Otherwise moving one character right 
    else:
        count += 1
        buffer.pop(0)
        buffer.append(letter)