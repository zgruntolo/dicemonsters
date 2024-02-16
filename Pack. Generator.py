import json
import random
from enum import Enum
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

class Rarity(Enum):
    COMMON = "COMMON"
    UNCOMMON = "UNCOMMON"
    RARE = "RARE"

class Card:
    def __init__(self, name, rarity):
        self.name = name
        self.rarity = Rarity(rarity)

def generate_rarity_weights():
    return [
        [3, 2, 1],
        [3, 2, 1],
        [2, 3, 1],
        [2, 2, 2]
    ]

def create_card_pool(data):
    card_pool = defaultdict(list)
    for entry in data:
        rarity = Rarity(entry['rarity'])
        card_pool[rarity].append(Card(entry['name'], rarity))
    return card_pool

def create_pack(cards, rarity_weights):
    pack = []
    with ThreadPoolExecutor() as executor:
        futures = []
        for i, weights in enumerate(rarity_weights):
            chosen_rarity = random.choices(list(Rarity), weights=weights)[0]
            if cards[chosen_rarity]:
                future = executor.submit(random.choice, cards[chosen_rarity])
                futures.append(future)
        for future in futures:
            chosen_card = future.result()
            pack.append(chosen_card)
    return pack

def open_pack(cards):
    rarity_weights = generate_rarity_weights()
    pack = create_pack(cards, rarity_weights)
    for card in pack:
        print(f"{card.name} - Rarity: {card.rarity.value}")

if __name__ == "__main__":
    with open("cards.json") as json_file:
        data = json.load(json_file)
    card_pool = create_card_pool(data)
    open_pack(card_pool)
