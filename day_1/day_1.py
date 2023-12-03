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
