from random import randint


def random_numbers():
    p = randint(100, 200)
    q = randint(100, 200)
    e = randint(100, 200)
    return p, q, e


def extended_gcd(a, b):
    s1, s2 = 1, 0
    t1, t2 = 0, 1
    while b != 0:
        r1, r2 = divmod(a, b)
        a, b = b, r2
        s1, s2, t1, t2 = t1, t2, s1 - r1 * t1, s2 - r2 * t2
    """ s1 - greatest common divisor"""
    return s1


def miller_rabin_test(number):
    d, s = number - 1, 0
    while d % 2:
        d, s = d >> 1, s + 1
    for i in range(10):
        a = randint(2, number - 2)
        x = pow(a, d, number)
        if x == 1 or x == number - 1:
            continue
        for j in range(s - 1):
            x = pow(x, 2, number)
            if x == 1:
                return False
            elif x == number - 1:
                a = 0
                break
        if a:
            return False
    return True


def generate_keys():
    while 1:
        p, q, e = random_numbers()
        if miller_rabin_test(p) and miller_rabin_test(q) and miller_rabin_test(e):
            n = p * q
            func_euler = (p - 1) * (q - 1)
            d = extended_gcd(e, func_euler)
            if d < 0:
                continue
            print(p, q)
            return n, e, d
        else:
            continue
