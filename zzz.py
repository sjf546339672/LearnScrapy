# coding: utf-8


def trailingZeroes(n):
    res = 0

    while n / 5 > 0:
        res += int(n / 5)
        n = n / 5
    return res


print(trailingZeroes(15))