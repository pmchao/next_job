import re


def flatten_list(data):
    # Step 1: Convert list to string
    data_str = str(data)

    # Step 2: Split using regex
    parts = re.split(r'[\[\],]', data_str)

    # Step 3: Remove empty strings and whitespace
    parts = [p.strip() for p in parts if p.strip()]

    return parts


def main():
    data = [[1, 2, 3, [4, 5]], 6]

    result = flatten_list(data)

    print("Original list:", data)
    print("Flattened list:", result)


if __name__ == "__main__":
    main()