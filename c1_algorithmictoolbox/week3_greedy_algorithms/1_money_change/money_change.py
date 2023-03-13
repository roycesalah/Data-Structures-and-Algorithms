# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3

    coins = 0
    while money > 0:
        if money >= 10:
            money -= 10
        elif 5 <= money < 10:
            money -= 5
        else:
            money -= 1
        coins += 1
    return coins


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
