with open('input.txt', 'r') as fp:
    lines = fp.readlines()

lines = [line.strip() for line in lines]

horizontal = 0
depth = 0

for line in lines:
    direction, value = line.split(' ')
    value = int(value)
    if direction == 'forward':
        horizontal += value
    elif direction == 'down':
        depth += value
    elif direction == 'up':
        depth -= value

print(horizontal * depth)

horizontal = 0
depth = 0
aim = 0

for line in lines:
    direction, value = line.split(' ')
    value = int(value)
    if direction == 'forward':
        horizontal += value
        depth += aim * value
    elif direction == 'down':
        aim += value
    elif direction == 'up':
        aim -= value

print(horizontal * depth)
