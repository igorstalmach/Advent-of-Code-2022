import copy

with open('day5/day5.txt', mode='r') as file:
    data = file.read()
    data = data.split('\n')

# Filling list with n empty lists, where n is the amount of stacks
crates = []
for _ in range(9):
    crates.append([])

# Adding crates to stacks
for line in data[:8]:
    # Crate letters on a single line are positioned every 4 indices starting from index 2
    index = 1

    for i in range(len(crates)):
        # Add only when a crate exists
        if line[index] != ' ':
            crates[i].append(line[index])
        index += 4

# Reversing every stack to simplify later operations
for i in range(len(crates)):
    crates[i] = list(reversed(crates[i]))

# Copying crate list for Part Two
crates_2 = copy.deepcopy(crates)

for command in data[10:]:
    # Parsing commands
    command = command.split(' ')
    amount, start, dest = int(command[1]), int(command[3]) - 1, int(command[5]) - 1

    # Crane holds crates to move
    crane = crates[start][-amount:]
    crane_2 = crates_2[start][-amount:]

    # Moving crates with changing order
    for crate in crane:
        crates[dest].append(crates[start].pop())

    # Moving crates without changing order
    crates_2[start] = crates_2[start][:-amount]
    crates_2[dest].extend(crane_2)

# Adding stacks top elements to a result string
stack_top = ''
for stack in crates:
    stack_top = stack_top + stack[-1]

stack_top_2 = ''
for stack in crates_2:
    stack_top_2 = stack_top_2 + stack[-1]

print(f"Part One: {stack_top}")
print(f"Part Two: {stack_top_2}")
