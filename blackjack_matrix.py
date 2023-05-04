import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["Clubs", "Diamonds", "Hearts", "Spades"]:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

class Player:
    def __init__(self):
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        total_value = 0
        num_aces = 0
        for card in self.hand:
            if card.value == 1:
                num_aces += 1
                total_value += 11
            elif card.value >= 10:
                total_value += 10
            else:
                total_value += card.value
        while total_value > 21 and num_aces > 0:
            total_value -= 10
            num_aces -= 1
        return total_value
    
deck = Deck()
deck.shuffle()
player = Player()
dealer = Player()

player.add_card(deck.deal_card())
player.add_card(deck.deal_card())
dealer.add_card(deck.deal_card())
dealer.add_card(deck.deal_card())

print("Dealer's hand:")
print(dealer.hand[0])
print("<hidden card>")
print("\nPlayer's hand:")
for card in player.hand:
    print(card)

while True:
    print("\nPlayer's turn:")
    print(f"Current hand value: {player.get_value()}")
    if player.get_value() > 21:
        print("Bust! You lose.")
        break
    elif player.get_value() == 21 and len(player.hand) == 2:
        print("Blackjack! You win.")
        break
    else:
        choice = input("Do you want to hit or stand? ")
        if choice.lower() == "hit":
            player.add_card(deck.deal_card())
            print(f"You were dealt the {player.hand[-1]}")
        elif choice.lower() == "stand":
            break

if player.get_value() <= 21:
    print("\nDealer's turn:")
    print(f"Dealer's hand: {', '.join(str(card) for card in dealer.hand)}")
    while dealer.get_value() < 17:
        dealer.add_card(deck.deal_card())
        print(f"Dealer was dealt the {dealer.hand[-1]}")
    print(f"Dealer's final hand value: {dealer.get_value()}")
    if dealer.get_value() > 21:
        print("Dealer busts! You win.")
    elif dealer.get_value() > player.get_value():
        print("Dealer wins!")
    elif dealer.get_value() < player.get_value():
        print("You win!")
    else:
        print("Tie game!")