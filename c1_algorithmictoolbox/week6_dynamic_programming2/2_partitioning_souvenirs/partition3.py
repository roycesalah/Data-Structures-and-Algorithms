from sys import stdin


def partition3(values):
    div3 = sum(values)/3
    # If the largest value is larger than a third of the 
    # sum, then it's not possible to divide into equal parts
    # OR if the modulo of the sum by 3 is not 0
    if any(max(values) > div3,div3 % 3 != 0,len(values) < 3):
        return 0
    


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))

