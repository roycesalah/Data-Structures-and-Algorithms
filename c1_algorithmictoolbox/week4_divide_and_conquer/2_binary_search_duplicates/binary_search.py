import math
import random
import sys

def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1

def binary_search(keys, query):
    low = 0
    high = len(keys)-1

    # Find an occurance of the query within the keys using binary search
    while True:
        mid = low + math.floor((high-low)/2)
        if high < low:
            return -1
        if query == keys[mid]:
            break
        elif query > keys[mid]:
            low = mid + 1
        elif query < keys[mid]:
            high = mid - 1

    # Iterate until the lowest indexed query is found
    while True:
        if keys[mid-1] != keys[mid]:
            return mid
        mid -= 1
        


if __name__ == '__main__':
    while True:
        x = random.sample(range(1000, 10000), 100) * random.choice([1,2,3,4,5])
        y = random.sample(range(1000, 10000), 100) * random.choice([1,2,3,4,5])
        z = random.sample(range(1000, 10000), 100) * random.choice([1,2,3,4,5])
        array = x + y + z
        array.sort()
        query = random.choice(array)
        if linear_search(array, query) != binary_search(array, query):
            sys.exit("dne")
        print(array)
        print(query)
        print("OK")

    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
