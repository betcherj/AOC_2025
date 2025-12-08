import os 
import math 

NUM_JUNCTIONS = 1000

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
    data = f.read().splitlines()
    locations = [[int(num) for num in line.split(',')] for line in data]
    locations = [(x[0], x[1], x[2]) for x in locations]


def distance(x,y):
    return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2 + (x[2]- y[2])**2) 


def sort_by_distance(locations):
    distances = []
    for idx, location in enumerate(locations):
        for idx2, location2 in enumerate(locations[idx+1:]):
            if location == location2:
                continue
            distances.append((distance(location, location2), location, location2))
    return sorted(distances, key= lambda x: x[0])
    

def get_junctions(locations): 
    distances = sort_by_distance(locations)

    # Now we need to assocate the closest pairs to eachother 
    graph = {k: set() for k in locations}
    for i in range(NUM_JUNCTIONS): 
        dist, loc1, loc2 = distances[i]
        # Make location 2 a neighbor of location 1 
            # add location 2 to neighbors of location 1 
        for node in graph[loc1]:
            if node != loc2:
                graph[node].add((loc2))
                graph[loc2].add((node))
        graph[loc1].add((loc2))
        # Make location 1 a neighbor of location 2 
        for node in graph[loc2]:
            if node != loc1:
                graph[node].add((loc1))
                graph[loc1].add((node))
        graph[loc2].add((loc1))
    return graph

def multiply_largest(graph, num=3):
    # We need to take out all the junction boxes in the clique 
    # then find the next largest clique
    res = 1 
    # for key, val in graph.items():
        # print(f"key: {key}, val: {val}")
    for i in range(num): 
        largest_group = 0 
        largest_key = None 
        largest_val = None 
        for key, val in graph.items(): 
            if len(val) + 1 > largest_group: 
                largest_group = len(val) + 1 # Since the node is in the group 
                largest_val = val 
                largest_key = key
        del graph[largest_key]
        for item in largest_val: 
            if item in graph:
                del graph[item]
        res *= largest_group 
        print(f"Largest group: {largest_group}, Largest key: {largest_key}")
    return res

if __name__ == "__main__": 
    # print(list(get_junctions(locations).values())[0])
    # print(get_junctions(locations))
    # distances = sort_by_distance(locations)
    # for i in range(len(distances)):
    #     for j in range(i+i, len(distances)):
    #         if distances[i] == distances[j]:
    #             print(f"Distance {distances[i]} is repeated")
    
    graph = get_junctions(locations)
    print(multiply_largest(graph))
