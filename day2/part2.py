import os 



with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
    data = f.read().split(',')
    ranges = [range.split('-') for range in data]

# What makes a range
# repearted sequences of numebrs 
# Brute force: if id[:len(id/2)] == id[len(id/2):] then it is invalid

def build_invalid_id_pattern(id, range_start, range_end): 
    min_digits = len(str(range_start))
    max_digits = len(str(range_end))
    
    return None

def is_valid_id(id): 
    # 2121212121
    
    

    return True

def get_invalid_id_sum_range(start, end): 
    invalid_id_sum = 0
    for i in range(int(start), int(end)+1): 
        if not is_valid_id(i): 
            invalid_id_sum += i
    return invalid_id_sum

def get_invalid_id_sum(ranges): 
    invalid_id_sum = 0 
    for start, end in ranges:
        invalid_id_sum += get_invalid_id_sum_range(start, end)

    return invalid_id_sum

if __name__ == "__main__":
    print(get_invalid_id_sum(ranges))
