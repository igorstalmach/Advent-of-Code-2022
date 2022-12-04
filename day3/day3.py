# Get item priority
def get_priority(num):
    if ord(num) > 96:
        return ord(num) - 96
    else:
        return ord(num) - 38


# Get priority of item that appears in both compartments of a rucksack
def get_rucksack_total(rucksack):
    first_compartment = set([*rucksack[:(len(rucksack)//2)]])
    second_compartment = set(*[rucksack[(len(rucksack)//2):]])

    for i in first_compartment:
        for j in second_compartment:
            if i == j:
                return get_priority(i)


# Get priority of item that appears in all three rucksacks
def check_rucksack(rucksack1, rucksack2, rucksack3):
    for badge in rucksack1:
        if badge in rucksack2:
            if badge in rucksack3:
                return get_priority(badge)
    

# Read and parse data
with open('day3/day3.txt', mode='r') as file:
    data = file.read()
    data = data.split('\n')

total1 = 0
total2 = 0

# Calculations for Part One
for rucksack in data:
    total1 += get_rucksack_total(rucksack)

# Calculations for Part Two
for i in range(0, len(data), 3):
    elf1, elf2, elf3 = data[i], data[i+1], data[i+2]
    total2 += check_rucksack(elf1, elf2, elf3)

print(f"Sum of the priorities for Part One: {total1}")
print(f"Sum of the priorities for Part Two: {total2}")