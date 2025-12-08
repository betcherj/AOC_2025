import os 
import re 


with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
    data = f.read().splitlines()
    # Read each line veritcally 
    grid = []
    for idx, line in enumerate(data[:-1]): 
        grid.append([])
        for char in line:
            grid[idx].append(char)

    operations = re.split(r'\s+', data[-1].strip())

def process_grid(grid):
    equations = []
    current_equation = []
    for j in range(len(grid[0])): 
        vertical = ''
        for i in range(len(grid)): 
            vertical += grid[i][j]
        if vertical.strip() == "": 
            equations.append(current_equation)
            current_equation = []
        else: 
            current_equation.append(int(vertical.strip()))
    equations.append(current_equation)
    return equations

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
        print(equation, operation)
        solutions.append(solve_equation(equation, operation))
    return sum(solutions)


if __name__ == "__main__": 
    # for row in grid:
    #     print(row)
    equations = process_grid(grid)
    print(solve_equations(equations, operations))