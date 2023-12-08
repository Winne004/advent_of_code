class FindNumbersAsStrings:
    numbers_as_words = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
def find_first_and_last_int(code: str) -> int:
    list_of_numbers = [char for char in code if char.isdigit()]
    return (
        False
        if not list_of_numbers
        else int("".join([list_of_numbers[0], list_of_numbers[-1]]))
    )


def main():
    filepath = "day_1/input.txt"
    calibration_document = open(filepath, "r")

    res = 0
    for line in calibration_document:
        res += find_first_and_last_int(line)

    return res


if __name__ == "__main__":
    main()
