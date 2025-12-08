import os 


with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
    data = f.read().splitlines()
    grid = [[char for char in line] for line in data]
    # for i, row in enumerate(grid): 
    #     for j, item in enumerate(row):
    #         if item == 'S': 
    #             beam_column = j
    #         elif item == "^": 
    #             splits.append((i, j))


def run_split(grid): 
    num_splits = 0 
    beam_columns = {}
    for i, line in enumerate(grid):
        for j, item in enumerate(line):
            if item == "S": 
                beam_columns[j] = True
            elif item == "^": 
                if j in beam_columns: 
                    del beam_columns[j]
                    num_splits += 1
                    if j>0 and j-1 not in beam_columns: 
                        beam_columns[j-1] = True
                    if j<len(line)-1 and j+1 not in beam_columns: 
                        beam_columns[j+1] = True 

                    
        print(f"Level {i}, num splits: {num_splits}")
    return num_splits


if __name__ == "__main__": 
    for row in grid: 
        print(row)
    print("here")
    print(run_split(grid))
