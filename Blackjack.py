

# poker_queue = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

spade = "\u2660"
heart = "\u2665"
diamond = "\u2666"
club = "\u2663"


class Dealer(object):
    def __init__(self, arg):
        self.arg = arg

class Player(object):
    def __init__(self, arg):
        self.arg = arg
    def hit():
        pass
    def stand():
        pass

class Card(object):
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __str__(self):
        number_str = ''
        if self.number == 1:
            number_str = 'A'
        elif self.number == 11:
            number_str = 'J'
        elif self.number == 12:
            number_str = 'Q'
        elif self.number == 13:
            number_str = 'K'
        else:
            number_str = str(self.number)
        return number_str + self.suit

    def possible_values(self):
        if self.number == 1:
            return [1, 11]
        elif self.number >= 2 and self.number <=10:
            return [self.number]
        else:
            return [10]
class Deck(object):
    def __init__(self):
        self.cards_array = []
        for each_card in range(num_cards):
            each_card = Card(spade, each_card)
            cards_array.append(each_card)
            each_card = Card(heart, each_card)
            cards_array.append(each_card)
            each_card = Card(diamond, each_card)
            cards_array.append(each_card)
            each_card = Card(club, each_card)
            cards_array.append(each_card)
        print(cards_array)

deck1 = Deck()
print(deck1)



# makes 52 cards (13 four times)
# put them in an array
# pop card from the top



# card1 = Card(spade, 3)
# card2 = Card(heart, 5)
# card3 = Card(club, 11)
# card4 = Card(diamond, 1)
# cards_array = [card1, card2, card3, card4]
#
# for card in cards_array:
#     print(card)
