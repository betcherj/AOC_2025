import os 


with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
    data = f.read().splitlines() 
    bank = []
    for line in data: 
        row = []
        for digit in line: 
            row.append(int(digit))
        bank.append(row)


def get_row_voltage(row, left, right):
    highest_digit = 0 

    for idx, digit in enumerate(row):
        if idx < left or idx > right:
            continue
        if digit > highest_digit:
            highest_digit = digit
            left = idx
    right += 1
    left += 1
    if right == len(row): 
        return str(highest_digit)
    else:
        return str(highest_digit) + get_row_voltage(row, left, right)

def get_bank_voltage(bank): 
    total_voltage = 0
    for row in bank: 
        row_voltage = get_row_voltage(row, 0, len(row)-12)
        total_voltage += int(row_voltage)
    return total_voltage


if __name__ == "__main__":
    print(get_bank_voltage(bank))
