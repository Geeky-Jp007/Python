n = int(input())
d1 = int(input())
d2 = int(input())


def any_to_ten(n, d):
    p = 0
    res = 0

    while n:
        res += (n % 10) * pow(d, p)
        n //= 10
        p += 1

    return int(res)


def ten_to_any(n, d):
    p = 0
    res = 0

    while n:
        res += (n % d) * pow(10, p)
        n //= d
        p += 1

    return res


def AnyToAny(n, d1, d2):
    med = any_to_ten(n, d1)
    return ten_to_any(med, d2)
# Write your code here


if __name__ == "__main__":
    res = AnyToAny(n, d1, d2)
    print(res)