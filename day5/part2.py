import os 


with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
    data = f.read().split('\n\n')
    ranges = data[0].split('\n')
    ranges = [range.split('-') for range in ranges]
    ranges = [[int(start), int(end)] for start, end in ranges]
    ingredient_ids = data[1].split('\n')
    ingredient_ids = [int(id) for id in ingredient_ids]


def combine_ranges(ranges): 
    ranges = sorted(ranges, key = lambda x: x[0])
    combined_ranges = [ranges[0]]
    for range in ranges[1:]: 
        if range[0] <= combined_ranges[-1][1]:
            combined_ranges[-1][1] = max(combined_ranges[-1][1], range[1])
        else: 
            combined_ranges.append(range)
    return combined_ranges

def count_fresh_range(ranges): 
    total_valid_ids = 0 
    for range in ranges: 
        total_valid_ids += range[1] - range[0] + 1
    return total_valid_ids



if __name__ == "__main__":
    ranges = combine_ranges(ranges)
    print(count_fresh_range(ranges))