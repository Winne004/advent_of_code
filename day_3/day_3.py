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
        first_half = sliding_window(
            row, col, engine_schematic, engine_schematic_width, True
        )
        second_half = sliding_window(
            row, col, engine_schematic, engine_schematic_width, False
        )
        return int(first_half + second_half)
    else:
        return 0


def sliding_window(row, col, engine_schematic, engine_schematic_width, reverse=True):
    res = ""
    if reverse:
        col -= 1
        while col >= 0 and engine_schematic[row][col].isdigit() :
            res += engine_schematic[row][col]
            engine_schematic[row][col] = '.'
            col -= 1
        return res[::-1]

    else:
        while col <= engine_schematic_width and engine_schematic[row][col].isdigit():
            res += engine_schematic[row][col]
            engine_schematic[row][col] = '.'
            col += 1 

        return res


def main():
    filepath = "./day_3/input.txt"

    with open(filepath, "r", encoding="utf-8") as f:
        engine_schematic = f.read().split()
        engine_schematic = [[str(char) for char in line] for line in engine_schematic]
                
        engine_schematic_length = len(engine_schematic)
        engine_schematic_width = len(engine_schematic[0])-1

        res = 0 

        for row_index, row in enumerate(engine_schematic):
            for col_index, char in enumerate(row):
                if not char.isalnum() and char != ".":
                    if char == '*':
                        tmp = []
                        for x, y in search_around_symbol():
                            t = (get_adjacent_number(
                            row_index + x,
                            col_index + y,
                            engine_schematic,
                            engine_schematic_length,
                            engine_schematic_width,
                        ))
                            if t != 0:
                                tmp.append(t)
                        if len(tmp)> 1:
                            res += math.prod(tmp)
                    # else:
                    #     for x, y in search_around_symbol():
                    #         res += (get_adjacent_number(
                    #             row_index + x,
                    #             col_index + y,
                    #             engine_schematic,
                    #             engine_schematic_length,
                    #             engine_schematic_width,
                    #         ))
        print(res)




if __name__ == "__main__":
    print(main())
