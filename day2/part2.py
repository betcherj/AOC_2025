import os 

import math 

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
    data = f.read().split(',')
    ranges = [range.split('-') for range in data]


def id_matches_pattern(id: str, pattern: str):
    for i in range(0, len(id), len(pattern)): 
        if id[i:i+len(pattern)] != pattern:
            return False
    return True


def is_valid_id(id: str):
    for i in range(math.ceil(len(id)/2)):
        if id_matches_pattern(id, id[:i+1]):
            return True
    return False
    

def get_invalid_id_sum_range(start, end): 
    invalid_id_sum = 0
    for i in range(int(start), int(end)+1): 
        if not is_valid_id((str(i))): 
            invalid_id_sum += i
    return invalid_id_sum

def get_invalid_id_sum(ranges): 
    invalid_id_sum = 0 
    for start, end in ranges:
        invalid_id_sum += get_invalid_id_sum_range(start, end)

    return invalid_id_sum

if __name__ == "__main__":
    print(get_invalid_id_sum(ranges))
