
def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(filter(str.isalnum, s)).lower()

    # Check if the string equals its reverse
    return cleaned == cleaned[::-1]


def main():
    # Test string
    input_string = "abba"

    if is_palindrome(input_string):
        print(f'"{input_string}" is a palindrome.')
    else:
        print(f'"{input_string}" is NOT a palindrome.')


if __name__ == "__main__":
    main()
