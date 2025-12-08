import os 


with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
    data = f.read().splitlines()
    grid = [[char for char in line] for line in data]

def run_split(grid): 
    beam_columns = {}
    for i, line in enumerate(grid):
        for j, item in enumerate(line):
            if item == "S": 
                beam_columns[j] = 1
            elif item == "^" and j in beam_columns: 
                if j>0: 
                    if j-1 not in beam_columns: 
                        beam_columns[j-1] = 0 
                    beam_columns[j-1] +=  beam_columns[j]
                if j<len(line)-1: 
                    if j+1 not in beam_columns: 
                        beam_columns[j+1] = 0 
                    beam_columns[j+1] += beam_columns[j]
                del beam_columns[j]
    return sum(beam_columns.values())


if __name__ == "__main__": 
    print(run_split(grid))
