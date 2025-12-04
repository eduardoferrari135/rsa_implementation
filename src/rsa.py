from encoding import decode, encode
from utils import gcd, generate_prime
import random


class RSAEncryption:
    def __init__(self) -> None:
        self.p = generate_prime()
        q = generate_prime()
        while q == self.p:
            q = generate_prime()
        self.q = q
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)

        e = random.randint(2, self.phi)
        while gcd(e, self.phi) != 1:
            e = random.randint(2, self.phi)
        self.e = e
        self.d = pow(self.e, -1, self.phi)

    def encrypt(self, m: int):
        return pow(m, self.e, self.n)

    def decrypt(self, c: int):
        return pow(c, self.d, self.n)


if __name__ == "__main__":
    o = RSAEncryption()
    message = "Hello world!"
    m = encode(message)
    c = o.encrypt(m)
    print(f"{c=}")
    m_new = o.decrypt(c)
    m_new = decode(m_new)
    print(f"{m_new=}")
