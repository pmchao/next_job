def time_in_words(hour, minute):
    words = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
        "twenty"
    ]

    def number_to_words(n):
        if n <= 20:
            return words[n]
        return "twenty " + words[n - 20]

    if minute == 0:
        return f"{words[hour]} o'clock"

    if minute == 15:
        return f"quarter past {words[hour]}"

    if minute == 30:
        return f"half past {words[hour]}"

    next_hour = hour % 12  + 1

    if minute == 45:
        return f"quarter to {words[next_hour]}"

    if minute < 30:
        unit = "minute" if minute == 1 else "minutes"
        return f"{number_to_words(minute)} {unit} past {words[hour]}"

    remaining = 60 - minute
    unit = "minute" if remaining == 1 else "minutes"

    return f"{number_to_words(remaining)} {unit} to {words[next_hour]}"


def main():
    hour = 5
    minute = 0

    result = time_in_words(hour, minute)
    print("Input:", f"{hour}:{minute:02d}")
    print("Output:", result)

if __name__ == "__main__":
    main()