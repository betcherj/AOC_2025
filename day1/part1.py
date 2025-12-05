import os 


dial_start = 50 # Starting position of the dial 
dial_max = 99 
dial_min = 0


with open(os.path.join(os.path.dirname(__file__), 'day1.txt'), 'r') as f:
    data = f.read().splitlines()
    amounts = [int(line[1:]) for line in data]
    directions = [line[0] for line in data]

def move_dial(direction, dial, move):
    print(f"Moving {move} {direction} from {dial}")

    if direction == 'L':
        dial = dial - move
        while dial < dial_min: 
            dial += dial_max + 1 
    elif direction == 'R':
        dial = dial + move
        while dial > dial_max:
            dial -= dial_max + 1
    print(f"New dial position: {dial}")
    return dial

def count_rotations(amounts, directions):
    rotations = 0
    dial = dial_start
    for amount, direction in zip(amounts, directions):
        dial = move_dial(direction, dial, amount)
        if dial == 0: 
            rotations += 1
    return rotations

if __name__ == "__main__":
    print(count_rotations(amounts, directions))