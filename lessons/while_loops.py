"""Demonstrates while loops by finding low value in a string"""

cards: str = "5235"

card_index: int = 0
low_card: int = int(cards[0])

#look at each number in the string
while card_index < 4:
    current_card: int = int(cards[card_index])
    if (current_card<low_card):
        low_card = current_card
    card_index +=1

print(low_card)