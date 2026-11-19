def decimal_to_binary(n):
    if n == 0:
        return "0"

    binary = ""

    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2

    return binary


def decimal_to_hex(n):
    if n == 0:
        return "0"

    hex_digits = "0123456789ABCDEF"
    hex_representation = ""

    while n > 0:
        hex_representation = hex_digits[n % 16] + hex_representation
        n = n // 16

    return hex_representation


def main():
    decimal_number = 5

    binary_representation = decimal_to_binary(decimal_number)
    hex_representation = decimal_to_hex(decimal_number)

    print(f"Decimal number: {decimal_number}")
    print(f"Binary representation: {binary_representation}")
    print(f"Hexadecimal representation: {hex_representation}")


if __name__ == "__main__":
    main()