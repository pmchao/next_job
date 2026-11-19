"""
Reorganize a list such that:
- All 0s are moved to the beginning (left)
- All 1s are moved to the end (right)
- All other numbers stay in the middle, preserving their original order

Example:
Input : [1, 2, 3, 1, 0, 4, 5, 0]
Output: [0, 0, 2, 3, 4, 5, 1, 1]
"""

def reorganize_list(numbers):
    processed_list = (
        [x for x in numbers if x == 0] +
        [x for x in numbers if x not in (0, 1)] +
        [x for x in numbers if x == 1]
    )

    return processed_list


def main():
    my_list = [1, 2, 3, 1, 0, 4, 5, 0]
    processed_list = reorganize_list(my_list)
    print("Original list:", my_list)
    print("Processed list:", processed_list)


if __name__ == "__main__":
    main()