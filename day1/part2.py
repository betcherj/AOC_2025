import os 


dial_start = 50 # Starting position of the dial 
dial_max = 99 
dial_min = 0

# 1, 2, 3, 4, 5 
with open(os.path.join(os.path.dirname(__file__), 'day1.txt'), 'r') as f:
    data = f.read().splitlines()
    amounts = [int(line[1:]) for line in data]
    directions = [line[0] for line in data]

def move_dial(direction, dial, move):
    rotations_step = 0 
    while move > dial_max:
        move -= dial_max + 1
        rotations_step += 1
    if direction == 'L':
        dial = dial - move 
        if dial == 0: 
            rotations_step += 1
        while dial < dial_min:
            rotations_step += 1
            dial += dial_max + 1
    elif direction == 'R':
        dial = dial + move
        if dial == 0: 
            rotations_step += 1
        while dial > dial_max:
            rotations_step += 1
            dial -= dial_max + 1 
    return dial, rotations_step

def count_rotations(amounts, directions):
    rotations = 0
    dial = dial_start
    for amount, direction in zip(amounts, directions):
        dial, rotations_step= move_dial(direction, dial, amount)
        rotations += rotations_step
    return rotations

if __name__ == "__main__":
    print(count_rotations(amounts, directions)) 