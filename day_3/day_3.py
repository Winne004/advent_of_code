import math


def search_around_symbol():
    for x in range(-1, 2, 1):
        for y in range(-1, 2, 1):
            if x == 0 and y == 0:
                continue
            else:
                yield x, y


def get_adjacent_number(
    row, col, engine_schematic, engine_schematic_length, engine_schematic_width
):
    if 0 > row > engine_schematic_length or 0 > col > engine_schematic_width:
        return False
    if engine_schematic[row][col].isdigit():
        number = sliding_window(row, col, engine_schematic, engine_schematic_width)
        return int(number)
    else:
        return 0


def sliding_window(row, col, engine_schematic, engine_schematic_width):
    number = ""

    left = col - 1
    while left >= 0 and engine_schematic[row][left].isdigit():
        number += engine_schematic[row][left]
        engine_schematic[row][left] = "."
        left -= 1
    number = number[::-1]

    while col <= engine_schematic_width and engine_schematic[row][col].isdigit():
        number += engine_schematic[row][col]
        engine_schematic[row][col] = "."
        col += 1

    return number


def get_symbol_locations(engine_schematic):
    for row_index, row in enumerate(engine_schematic):
        for col_index, char in enumerate(row):
            if not char.isalnum() and char != ".":
                yield row_index, row, col_index, char


def get_sum_of_part_numbers(
    engine_schematic,
    engine_schematic_length,
    engine_schematic_width,
    res,
    row_index,
    col_index,
    x,
    y,
):
    res += get_adjacent_number(
        row_index + x,
        col_index + y,
        engine_schematic,
        engine_schematic_length,
        engine_schematic_width,
    )
    return res


def get_gear_ratio(
    engine_schematic,
    engine_schematic_length,
    engine_schematic_width,
    total_gear_ratios,
    row_index,
    col_index,
):
    gear_ratios_near = []
    for x, y in search_around_symbol():
        t = get_adjacent_number(
            row_index + x,
            col_index + y,
            engine_schematic,
            engine_schematic_length,
            engine_schematic_width,
        )
        if t != 0:
            gear_ratios_near.append(t)
    if len(gear_ratios_near) > 1:
        total_gear_ratios += math.prod(gear_ratios_near)
    return total_gear_ratios


def listify_input(f):
    engine_schematic = f.read().split()
    engine_schematic = [[str(char) for char in line] for line in engine_schematic]
    return engine_schematic


def main():
    filepath = "./day_3/input.txt"
    gear = False
    with open(filepath, "r", encoding="utf-8") as f:
        engine_schematic = listify_input(f)

        engine_schematic_length = len(engine_schematic)
        engine_schematic_width = len(engine_schematic[0]) - 1

        res, total_gear_ratios = 0, 0

        for row_index, row, col_index, char in get_symbol_locations(engine_schematic):
            if gear:
                if char == "*":
                    total_gear_ratios = get_gear_ratio(
                        engine_schematic,
                        engine_schematic_length,
                        engine_schematic_width,
                        total_gear_ratios,
                        row_index,
                        col_index,
                    )

            else:
                for x, y in search_around_symbol():
                    res = get_sum_of_part_numbers(
                        engine_schematic,
                        engine_schematic_length,
                        engine_schematic_width,
                        res,
                        row_index,
                        col_index,
                        x,
                        y,
                    )
        print(res, total_gear_ratios)


if __name__ == "__main__":
    print(main())
