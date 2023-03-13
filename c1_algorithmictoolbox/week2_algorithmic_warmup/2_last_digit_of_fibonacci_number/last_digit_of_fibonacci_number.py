# python3


def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7
    # Establish initial set
    memo = [0,1,1]
    if n == 0:
        return memo[0]
    for _ in range(n - 2):
        # Shift memory over ( Eliminates need to save all 10 ** 7 numbers)
        # Further optimize by only saving last digit
        memo[0] = memo[1]
        memo[1] = memo[2]
        memo[2] = int(str(memo[1] + memo[0])[-1])

    return int(str(memo[2])[-1])


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
