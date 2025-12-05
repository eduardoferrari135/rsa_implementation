from encoding import decode, encode
from utils import gcd, generate_prime
import random
import json
import base64


class RSAKey:
    def __init__(self, n: int, e: int, d: int | None = None) -> None:
        self.n = n
        self.e = e
        self.d = d

    @property
    def is_private(self):
        return self.d is not None

    def export_key(self) -> str:
        """Exports the key as a base64 encoded JSON string."""
        key_data = {"n": self.n, "e": self.e}
        if self.d:
            key_data["d"] = self.d

        json_bytes = json.dumps(key_data).encode("utf-8")
        return base64.b64encode(json_bytes).decode("utf-8")

    @classmethod
    def import_key(cls, key_str: str):
        """Creates an RSAKey instance from a base64 encoded string."""
        try:
            json_bytes = base64.b64decode(key_str)
            data = json.loads(json_bytes)
            return cls(n=data["n"], e=data["e"], d=data.get("d"))
        except Exception as e:
            raise ValueError("Invalid key format") from e

    def __str__(self):
        base = f"MODULUS n: {self.n}\nPUBLIC RSA KEY: {self.e}"
        if self.d:
            return base + f"\nPRIVATE RSA KEY: {self.d}"
        return base


class RSA:
    @staticmethod
    def generate_keys() -> RSAKey:
        p = generate_prime()
        q = generate_prime()
        while q == p:
            q = generate_prime()

        n = p * q
        phi = (p - 1) * (q - 1)

        e = 65537
        if gcd(e, phi) != 1:
            e = random.randint(3, phi - 1)
            while gcd(e, phi) != 1:
                e = random.randint(3, phi - 1)

        d = pow(e, -1, phi)
        return RSAKey(n, e, d)

    @staticmethod
    def encrypt(m: int | str, key: RSAKey) -> int:
        if isinstance(m, str):
            m = encode(m)
        return pow(m, key.e, key.n)

    @staticmethod
    def decrypt(c: int, key: RSAKey) -> str:
        if not key.is_private:
            raise ValueError("Private key required for decryption.")
        return pow(c, key.d, key.n)

    @staticmethod
    def decrypt_and_decode(c: int, key: RSAKey) -> str:
        return decode(RSA.decrypt(c, key))


if __name__ == "__main__":
    key_pair = RSA.generate_keys()
    message = "Here's my secret message"
    ciphered = RSA.encrypt(message, key_pair)
    deciphered = RSA.decrypt_and_decode(ciphered, key_pair)
    breakpoint()
