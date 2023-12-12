from dataclasses import dataclass
from collections import Counter

@dataclass
class Card:
    card_number: int
    first_half: list
    second_half: list

    def __post_init__(self):
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


def get_card_number(line):
    line = line.split(":")[0]
    line = line.split(" ")[-1]
    return line


def get_games(line):
    games = line.split(":")[-1]
    first_game, second_game = games.split("|")
    return [score.strip() for score in first_game.split(" ") if score != ''], [
        score.strip() for score in second_game.split(" ") if score != ''
    ]


def listify_input(f, cards):
    scratchcards = f.read().split("\n")
    for scratchcard in scratchcards:
        cardnumber = get_card_number(scratchcard)
        first_game, second_game = get_games(scratchcard)
        cards.add_card_to_collection(cardnumber, first_game, second_game)
    return scratchcards


def main():
    filepath = "./day_4/input.txt"
    cards = Cards()
    with open(filepath, "r", encoding="utf-8") as f:
        listify_input(f, cards)
    res = 0 
    for card in cards.collection:
        res += card.shared_values
    return res


if __name__ == "__main__":
    print(main())