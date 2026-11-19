
def find_second_smallest(numbers):
    if len(numbers) < 2:
        raise ValueError("At least two numbers are required.")

    # Check if all numbers are identical
    if len(set(numbers)) == 1:
        raise ValueError("All numbers are the same. No second smallest.")

    min1 = float('inf')
    min2 = float('inf')

    for num in numbers:
        if num < min1:
            min2 = min1
            min1 = num
        elif min1 < num < min2:
            min2 = num

    if min2 == float('inf'):
        return None

    return min2


def main():
    nums = [7,-1, 3, 1, 2, 4, 1, 9, 3]
    #nums = [3]
    #nums = [3,3,3]
    nums = [7, -1, 3]

    try:
        second_smallest = find_second_smallest(nums)

        if second_smallest is not None:
            print(f"The second smallest number is: {second_smallest}")
        else:
            print("No second smallest number found.")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
