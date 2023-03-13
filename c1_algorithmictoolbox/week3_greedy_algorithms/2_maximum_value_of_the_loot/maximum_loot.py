# python3
from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 0 <= len(weights) <= 10 ** 3
    assert all(0 <= w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    # Check if capacity is filled or if all weights are empty
    if capacity == 0 or weights == []:
        return 0
    # Adjust price to cost / weight ratio
    adjustedprice = []
    for i in range(len(prices)):
        adjustedprice.append(prices[i]/weights[i])
    maxindex = adjustedprice.index(max(adjustedprice))
    amount = min(capacity, weights[maxindex])
    value = (amount/weights[maxindex])*prices[maxindex]

    # Adjust for changes
    weights[maxindex] -= amount
    capacity -= amount
    if weights[maxindex] == 0:
        prices.pop(maxindex)
        weights.pop(maxindex)

    return value + maximum_loot_value(capacity, weights, prices)


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
