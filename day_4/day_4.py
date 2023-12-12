from dataclasses import dataclass
from collections import Counter


@dataclass
class Card:
    card_number: int
    first_half: Counter
    second_half: Counter

    def __post_init__(self):
        self.card_number = int(self.card_number)
        self.first_half = Counter(self.first_half)
        self.second_half = Counter(self.second_half)
        self.number_of_keys = self.get_shared_keys()
        self.shared_values = self.get_shared_values()

    def get_shared_values(self):
        res = 0
        for _ in range(self.number_of_keys):
            if res == 0:
                res = 1
            else:
                res *= 2
        return res

    def get_shared_keys(self):
        return len([key for key in self.first_half.keys() & self.second_half.keys()])


class Cards:
    def __init__(self) -> None:
        self.collection = []

    def add_card_to_collection(self, card_number, first_half, second_half):
        self.collection.append(Card(card_number, first_half, second_half))


class WinningCardsCounter:
    def __init__(self) -> None:
        self.number_of_winning_card = Counter()
        self.res = 0

    def increment_winning_card_count(self, card_number, number_of_matches):
        while self.number_of_winning_card[card_number] >= 0:
            for x in range(card_number + 1, card_number + number_of_matches + 1, 1):
                self.number_of_winning_card[x] += 1
            self.res += 1
            self.number_of_winning_card[card_number] -= 1


def parse_card_number_from_input(line):
    line = line.split(":")[0]
    line = line.split(" ")[-1]
    return line


def parse_games_from_input(line):
    games = line.split(":")[-1]
    first_game, second_game = games.split("|")
    return [score.strip() for score in first_game.split(" ") if score != ""], [
        score.strip() for score in second_game.split(" ") if score != ""
    ]


def process_input(f, cards):
    scratchcards = f.read().split("\n")
    for scratchcard in scratchcards:
        cardnumber = parse_card_number_from_input(scratchcard)
        first_game, second_game = parse_games_from_input(scratchcard)
        cards.add_card_to_collection(cardnumber, first_game, second_game)
    return scratchcards


def main():
    filepath = "./day_4/input.txt"
    cards = Cards()
    winning_card_counter = WinningCardsCounter()

    with open(filepath, "r", encoding="utf-8") as f:
        process_input(f, cards)

    res = 0
    for card in cards.collection:
        res += card.shared_values
        winning_card_counter.increment_winning_card_count(
            card.card_number, card.number_of_keys
        )

    return res, winning_card_counter.res


if __name__ == "__main__":
    print(main())
