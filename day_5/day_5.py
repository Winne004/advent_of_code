from collections import defaultdict
from typing import List


def parse_almanacs(almanac):
    tmp = []
    mapping = None
    almanac_collection = defaultdict(list)
    for x in range(2, len(almanac), 1):
        if "map" in almanac[x]:
            mapping = almanac[x][:-1]
        elif almanac[x] != "":
            tmp.append(almanac[x].split(" "))
        elif almanac[x] == "":
            almanac_collection[mapping].append([[int(x) for x in x] for x in tmp])
            tmp = []
    almanac_collection[mapping].append([[int(x) for x in x] for x in tmp])
    return almanac_collection


def get_seeds(almanac):
    seeds = {
        almanac[0].split(":")[0]: [
            numbers.strip()
            for numbers in almanac[0].split(":")[1].split(" ")
            if numbers != ""
        ]
    }
    return seeds


def process_input(f):
    almanac = f.read().split("\n")
    return almanac


def x_to_y(step, m) -> int:
    for destination_range_start, source_range_start, range_length in m:
        if step >= source_range_start and step < source_range_start + range_length:
            step = destination_range_start + (step - source_range_start)
            break

    return step


def main():
    filepath = "./day_5/input.txt"
    with open(filepath, "r", encoding="utf-8") as f:
        almanac = process_input(f)
    seeds = get_seeds(almanac)
    parsed_almnacs = parse_almanacs(almanac)
    r = float("inf")

    for seedss in seeds.values():
        for seed in seedss:
            for almnac in parsed_almnacs.values():
                for mappings in almnac:
                    seed = x_to_y(int(seed), mappings)
            r = min(r, seed)
    print(r)


if __name__ == "__main__":
    print(main())
