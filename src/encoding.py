def encode(text: str):
    final_message = 0
    for c in text:
        final_message = final_message * 256 + ord(c)
    return final_message


def decode(number: int):
    bytes_list = []

    while number > 0:
        bytes_list.append(number % 256)
        number = number // 256
    bytes_list.reverse()
    return bytes(bytes_list).decode()


if __name__ == "__main__":
    e = encode("Hello world")
    d = decode(e)

    print(f"{e=}")
    print(f"{d=}")
