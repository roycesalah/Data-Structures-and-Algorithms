from sys import stdin


def maximum_gold(capacity, weights):
    memo = []
    # Initialize empty array (add 1 to each length to account for 0 value)
    for j in range(len(weights)+1):
        memo.append([0]*(capacity+1))
    # Iterate through different numbers of weights
    for w in range(1,len(weights)+1):
        # Iterate 1 to maximum capacity
        for c in range(1,capacity+1):
            memo[w][c] = memo[w-1][c]
            if weights[w-1] <= c:
                val = memo[w-1][c-weights[w-1]] + weights[w-1]
                if val > memo[w][c]:
                    memo[w][c] = val

    return memo[len(weights)][c]



if __name__ == '__main__':
    # DELETE NEW INPUTS BEFORE SUBMIT
    input_capacity, n = list(map(int, input().split()))
    input_weights = list(map(int, input().split()))
    
    #input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
