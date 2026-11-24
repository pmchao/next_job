def main():
    str1 = "aabbccc"

    def letter_count(str1):
        if not str1:
            return ""

        str2 = ""
        counter = 1
        endpoint = len(str1)
    result = letter_count(str1)

    print("Original string:", str1)
    print("Compressed string:", result)
    print("Compressed length:", len(result))


if __name__ == "__main__":
    main()