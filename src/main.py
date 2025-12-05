from rsa import RSA, RSAKey


def main():
    option = input("Enter 1 to encrypt, 2 to decrypt: ")
    if option == "1":
        content = input("Enter the content you want to encrypt: ")
        key_pair = RSA.generate_keys()

        path = input("Enter the key.txt path (default: './key.txt'): ")
        if len(path) == 0:
            path = "./key.txt"

        with open(path, "w") as file:
            file.write(key_pair.export_key())
            print("Key saved at key.txt.")

        ciphered = RSA.encrypt(content, key_pair)
        print(f"Ciphered message: {ciphered}")
    elif option == "2":
        ciphered_content = int(input("Enter the content you want to decipher: "))
        path = input("Enter the key.txt path (default: './key.txt'): ")
        if len(path) == 0:
            path = "./key.txt"
        with open(path, "r") as file:
            key = file.read()

        key = RSAKey.import_key(key)
        deciphered = RSA.decrypt_and_decode(ciphered_content, key)
        print(f"Deciphered message: {deciphered}")


if __name__ == "__main__":
    main()
