# python3


def lcm_naive(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    multiple = max(a, b)
    while multiple % a != 0 or multiple % b != 0:
        multiple += 1

    return multiple

def gcd(a, b):
    assert 0 <= a <= 2 * 10 ** 9 and 0 <= b <= 2 * 10 ** 9

    if b == 0:
        return a
    ap = a % b
    return gcd(b,ap)

def lcm(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9
    lcm = a*b/gcd(a,b)
    return int(lcm)


if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(lcm(input_a, input_b))
