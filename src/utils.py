import random
import secrets


def generate_prime(bits=1024):
    while True:
        candidate = secrets.randbits(bits)

        # Transforma o bit mais significativo e menos significativo em 1,
        # garantindo números grandes e ímpares
        candidate |= (1 << bits - 1) | 1

        if is_prime(candidate):
            return candidate


def is_prime(n: int, rounds=40):
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(rounds):
        a = random.randint(2, n - 2)

        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    print(gcd(9, 6))
