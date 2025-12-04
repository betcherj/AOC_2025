import os 


with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
    data = f.read().splitlines() 
    bank = []
    for line in data: 
        row = []
        for digit in line: 
            row.append(int(digit))
        bank.append(row)


def get_row_voltage(row):
    reversed_row = row[::-1]
    leading_digit = reversed_row[1]
    trailing_digit = reversed_row[0]
    leading_digit_idx = 1
    for idx, digit in enumerate(reversed_row[2:]):
        if digit >= leading_digit:
            leading_digit = digit 
            leading_digit_idx = idx + 2
            trailing_digit = max(reversed_row[:idx+2])
        
    trailing_digit = max(reversed_row[:leading_digit_idx])
    return int(str(leading_digit) + str(trailing_digit))        

def get_bank_voltage(bank): 
    total_voltage = 0
    for row in bank: 
        row_voltage = get_row_voltage(row)
        total_voltage += row_voltage
    return total_voltage


if __name__ == "__main__":
    print(get_bank_voltage(bank))
