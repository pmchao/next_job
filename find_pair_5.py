def find_pairs_with_sum(numbers, target):
    seen = set()
    pairs = []
    unique_pairs = set()

    for number in numbers:
        complement = target - number

        if complement in seen:
            pair = (min(number, complement),
                    max(number, complement))

            if pair not in unique_pairs:
                pairs.append(pair)
                unique_pairs.add(pair)

            seen.remove(complement)
        else:
            seen.add(number)

    return pairs


def main():
    numbers = [2, 5, 5, 5, 4, 3, 7, 8]
    target = 10

    result = find_pairs_with_sum(numbers, target)

    print("Original list:", numbers)
    print("Target sum:", target)
    print("Pairs found:", result)


if __name__ == "__main__":
    main()