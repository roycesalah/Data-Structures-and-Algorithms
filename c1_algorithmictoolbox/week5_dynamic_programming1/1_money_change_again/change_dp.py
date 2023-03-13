def change(money):
    # Money denominations are 1,3,4
    arr = [0] * (money+1)
    for i in range(1,money+1):
        arr[i] = min([(arr[i-denom]+1) for denom in [1,3,4] if i-denom >= 0])

    return arr[money]


if __name__ == '__main__':
    m = int(input())
    print(change(m))
