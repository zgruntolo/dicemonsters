import csv
import random
from enum import Enum

class Rarity(Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"

class Card:
    def __init__(self, name, rarity):
        self.name = name
        self.rarity = rarity

def generate_rarity_weights():
    return [
        [3, 2, 1],
        [3, 2, 1],
        [2, 3, 1],
        [2, 2, 2]
    ]

def create_card_pool(filename):
    card_pool = {Rarity.COMMON: [], Rarity.UNCOMMON: [], Rarity.RARE: []}
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rarity = Rarity[row['rarity']]
            card = Card(row['name'], rarity)
            card_pool[rarity].append(card)
    return card_pool

def create_pack(cards, rarity_weights):
    chosen_rarity = random.choices(list(Rarity), weights=rarity_weights)[0]
    chosen_card = random.choice(cards[chosen_rarity])
    return chosen_card

def open_pack(cards):
    rarity_weights = generate_rarity_weights()
    pack = [create_pack(cards, rarity_weights) for rarity_weights in rarity_weights]
    for card in pack:
        print(f"{card.name} - Rarity: {card.rarity.value}")

if __name__ == "__main__":
    card_pool = create_card_pool("cards.csv")
    open_pack(card_pool)
