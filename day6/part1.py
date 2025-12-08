import os 
import re 


with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
    data = f.read().splitlines()
    # Read each line veritcally 
    equations = []
    for i, line in enumerate(data[:-1]): 
        split_line = re.split(r'\s+', line.strip())
        for j, num in enumerate(split_line): 
            if i == 0: 
                equations.append([int(num)])
            else: 
                equations[j].append(int(num))
    operations = re.split(r'\s+', data[-1].strip())


def solve_equation(equation, operation):
    if operation == "+": 
        total = 0 
        for num in equation: 
            total += num 
    if operation == "*": 
        total = 1 
        for num in equation: 
            total *= num 
    return total

def solve_equations(equations, operations):
    solutions = [] 
    for equation, operation in zip(equations, operations):
        solutions.append(solve_equation(equation, operation))
    return sum(solutions)


if __name__ == "__main__": 
    print(solve_equations(equations, operations))