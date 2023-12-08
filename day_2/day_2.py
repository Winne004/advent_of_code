import numpy


class GemsPossible:
    gem_maximum_possible_values = {"red": 12, "green": 13, "blue": 14}

    @staticmethod
    def do_number_of_gems_exceed_allowed_values(subset_to_check):
        for (
            k,
            v,
        ) in subset_to_check.items():
            if v > GemsPossible.gem_maximum_possible_values[k]:
                return False
        return True


def get_game(game_record):
    id_, game = [game.strip() for game in game_record.split(":")]
    return int(id_.split(" ")[-1]), game


def get_subsets_from_game(game):
    subset = [subset.strip() for subset in game.split(";")]
    return subset


def get_stones_from_subset(subset):
    stones = [stone.strip() for stone in subset.split(",")]
    return stones


def sort_stones_into_color_dictionary(stones):
    colour_count_dict = {"red": 0, "blue": 0, "green": 0}
    for stone in stones:
        v, k = [stone.strip() for stone in stone.split(" ")]
        colour_count_dict[k] = int(v)
    return colour_count_dict


def get_stones_in_game(game_record):
    id_, game = get_game(game_record)
    subsets = get_subsets_from_game(game)
    stones_in_game = []
    for subset in subsets:
        stones = get_stones_from_subset(subset)
        colour_count_dict = sort_stones_into_color_dictionary(stones)
        stones_in_game.append(colour_count_dict)
    return stones_in_game, id_


def is_game_valid(id_, stones_in_game):
    return (
        id_
        if all(
            GemsPossible.do_number_of_gems_exceed_allowed_values(color_counts)
            for color_counts in stones_in_game
        )
        else 0
    )


def get_min_values(stones_in_game):
    dict = {}
    for key in GemsPossible.gem_maximum_possible_values.keys():
        dict[key] = 0
    for colour_count_dict in stones_in_game:
        for k, v in colour_count_dict.items():
            dict[k] = max(dict[k], v)
    return numpy.prod(list(dict.values()))


def main():
    filepath = "./day_2/input.txt"

    res, sum_of_power = 0, 0
    with open(filepath, "r", encoding="utf-8") as game_records:
        for game_record in game_records:
            stones_in_game, id_ = get_stones_in_game(game_record)

            res += is_game_valid(id_, stones_in_game)
            sum_of_power += get_min_values(stones_in_game)
    return res, sum_of_power


if __name__ == "__main__":
    print(main())
