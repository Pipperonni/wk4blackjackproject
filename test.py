
import random

class Card:
    
    def __init__(self):
        self.cards = {"ace of clubs" : 11, "ace of dimonds" : 11, "ace of hearts" : 11, "ace of spades" : 11,
"eight of clubs" : 8, "eight of dimonds" : 8, "eight of hearts" : 8, "eight of spades" : 8, 
"five of clubs" : 5, "five of dimonds" : 5,"five of hearts" : 5, "five of spades" : 5,
"four of clubs" : 4, "four of dimonds" : 4,"four of hearts" : 4, "four of spades" : 4,
"jack of clubs" : 10, "jack of dimonds" : 10,"jack of hearts" : 10, "jack of spades" : 10,
"king of clubs" : 10, "king of dimonds" : 10,"king of hearts" : 10, "king of spades" : 10,
"nine of clubs" : 9, "nine of dimonds" : 9,"nine of hearts" : 9, "nine of spades" : 9,
"queen of clubs" : 10, "queen of dimonds" : 10,"queen of hearts" : 10, "queen of spades" : 10,
"seven of clubs" : 7, "seven of dimonds" : 7,"seven of hearts" : 7, "seven of spades" : 7,
"six of clubs" : 6, "six of dimonds" : 6,"six of hearts" : 6, "six of spades" : 6,
"ten of clubs" : 10, "ten of dimonds" : 10,"ten of hearts" : 10, "ten of spades" : 10,
"three of clubs" : 3, "three of dimonds" : 3,"three of hearts" : 3, "three of spades" : 3,
"two of clubs" : 2, "two of dimonds" : 2,"two of hearts" : 2, "two of spades" : 2}


class Hand:
    def __init__(self):
        self.player_value = 0
        self.dealer_value = 0
        self.player_cards_in_hand = []
        self.dealer_cards_in_hand = []
        self.played_deck = Card()
        self.new_deck = self.played_deck.cards.copy()
        self.list_hits = 1
        self.d_list_hits = 1
        self.player_ply = False
        self.dealer_ply = False
    def main(self):
        while True:
            user_input = input("\nPlay BlackJack: (y/n): ")
            if user_input == "y":
                self.player_ply = True
                self.dealer_ply = True
                cards = list(self.new_deck.keys())
                random.shuffle(cards)
                self.deal_cards()
                while self.player_ply or self.dealer_ply:
                    
                    print(f"\nYou have {self.player_cards_in_hand}, a total of {self.player_value} ")
                    print(f"\nDealer has {self.dealer_cards_in_hand[0][0]} : X")
                    player_input = input("\nHit or Stand: (h/s) ").lower()
                    if player_input == "h":
                        self.player_hits()
                    elif player_input == "s":
                        self.staying()
                    else:
                        print("\nInvald Input")
            elif user_input == "n":
                break
    
    def deal_cards(self):
        # Player cards
        player_card = random.sample(self.new_deck.keys(), k=2)
        self.player_cards_in_hand.append(player_card)
        del self.new_deck[self.player_cards_in_hand[0][0]]
        del self.new_deck[self.player_cards_in_hand[0][1]]
        self.player_value += self.played_deck.cards[self.player_cards_in_hand[0][0]]
        self.player_value += self.played_deck.cards[self.player_cards_in_hand[0][1]]
        # Dealer cards
        dealer_card = random.sample(self.new_deck.keys(), k=2)
        self.dealer_cards_in_hand.append(dealer_card)
        del self.new_deck[self.dealer_cards_in_hand[0][0]]
        del self.new_deck[self.dealer_cards_in_hand[0][1]]
        self.dealer_value += self.played_deck.cards[self.dealer_cards_in_hand[0][0]]
        self.dealer_value += self.played_deck.cards[self.dealer_cards_in_hand[0][1]]
        self.current_points()
        return 

    def current_points(self):
        aces = "ace of clubs ace of dimonds ace of hearts ace of spades"
        if self.player_value > 21:
            for alist in self.player_cards_in_hand:
                for card in alist:
                    if card in aces:
                        if self.player_value > 21:
                            self.player_value -= 10
                    else:
                        print("\nBUST, You Lose.")
                        self.player_ply = False
                        self.dealer_ply = False
                        self.remove_cards()
                        return

    
    def player_hits(self):
        player_card = random.sample(self.new_deck.keys(), k=1)
        self.player_cards_in_hand.append(player_card)
        del self.new_deck[self.player_cards_in_hand[self.list_hits][0]]
        self.player_value += self.played_deck.cards[self.player_cards_in_hand[self.list_hits][0]]
        print(f"\nYou have {self.player_cards_in_hand}, total of {self.player_value}")
        self.list_hits += 1
        self.current_points()
        return 

    def dealer_hits(self):
        dealer_card = random.sample(self.new_deck.keys(), k=1)
        self.dealer_cards_in_hand.append(dealer_card)
        del self.new_deck[self.dealer_cards_in_hand[self.d_list_hits][0]]
        self.dealer_value += self.played_deck.cards[self.dealer_cards_in_hand[self.d_list_hits][0]]
        self.d_list_hits += 1
        self.staying()
        return 
    
    def staying(self):
        print(f"\nDealer has {self.dealer_cards_in_hand}, total of {self.dealer_value}")
        aces = "ace of clubs ace of dimonds ace of hearts ace of spades"
        if self.dealer_value > 21:
            for alist in self.dealer_cards_in_hand:
                for card in alist:
                    if card in aces:
                        if self.dealer_value > 21:
                            self.dealer_value -= 10
                        elif self.dealer_value < 21:
                            self.staying()
                    else:
                        print("\nDealer BUSTS\n!!!! You Win !!!!")
                        print(f"\nYour hand {self.player_cards_in_hand}, total {self.player_value}")
                        self.player_ply = False
                        self.dealer_ply = False
                        self.remove_cards()
                        return
        
        elif self.dealer_value < 17:
            print("\nDealer Hits")
            self.dealer_hits()
        
        elif self.dealer_value >= 17:
            if self.dealer_value > self.player_value:
                print("\nYou Lose")
                print(f"\nYour hand {self.player_cards_in_hand}, total {self.player_value}")
                self.player_ply = False
                self.dealer_ply = False
                self.remove_cards()
            elif self.dealer_value < self.player_value:
                print("\n!!!! You Win !!!!")
                print(f"\nYour hand {self.player_cards_in_hand}, total {self.player_value}")
                self.player_ply = False
                self.dealer_ply = False
                self.remove_cards()
            else:
                print("\nIt's a Draw")
                print(f"\nYour hand {self.player_cards_in_hand}, total {self.player_value}")
                self.player_ply = False
                self.dealer_ply = False
                self.remove_cards()


    def remove_cards(self):
        self.player_value = 0
        self.dealer_value = 0
        self.list_hits = 1
        self.d_list_hits = 1
        self.player_cards_in_hand.clear()
        self.dealer_cards_in_hand.clear() 
        self.new_deck.clear()
        self.new_deck = self.played_deck.cards.copy()


c = Hand()
c.main()