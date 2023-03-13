# python3
def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45
    memo = [0] * (n+1)
    # Establish value 1 at 1 position
    if n == 0:
        return memo[0]
    memo[1] = 1
    for i in range(n-1):
        memo[i+2] = memo[i+1] + memo[i]
    return memo[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
    # print(fibonacci_number_naive(input_n))
