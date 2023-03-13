import sys
def compute_operations(n):
    # Functions are +1, *2, *3
    operations = [0,(None,0)]
    ind = 2
    while ind < n+1:
        ops = [operations[ind-1][1]+1] + [operations[int(ind/x)][1]+1 if ind%x==0 else 99999 for x in [2,3]]
        min_op = ops.index(min(ops))
        operations.append((min_op+1,ops[min_op]))
        ind += 1
    

    # Backtrack through operations
    backtracked_operations = []
    number = n
    while True:
        if number == 1:
            backtracked_operations.append(1)
            break
        backtracked_operations.append(number)
        if operations[number][0] == 1:
            number -= 1
        else:
            number = int(number / operations[number][0])
    
    # Reverse order of backtracked operations
    backtracked_operations.reverse()

    return backtracked_operations


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
