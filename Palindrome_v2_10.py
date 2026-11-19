def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(filter(str.isalnum, s)).lower()

    # Initialize two pointers
    left = 0
    right = len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False

        left += 1
        right -= 1

    return True


def main():
    # Get user input
    input_string = input("Enter a string: ")

    if is_palindrome(input_string):
        print(f'"{input_string}" is a palindrome.')
    else:
        print(f'"{input_string}" is NOT a palindrome.')

if __name__ == "__main__":
    main()
