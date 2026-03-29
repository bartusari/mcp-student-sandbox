def average_ratios(numbers):
    if not isinstance(numbers, list):
        raise TypeError("numbers must be a list")
    if len(numbers) == 0:
        raise ValueError("numbers must not be empty")
    if any(n == 0 for n in numbers):
        raise ValueError("numbers must not contain zero")

    total = 0.0
    for number in numbers:
        total += 100.0 / number

    return total / len(numbers)


if __name__ == "__main__":
    print(average_ratios([10, 5, 2]))
