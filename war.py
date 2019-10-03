import random

class Card:
  def __init__(self, suit, val):
    self.suit = suit
    self.val = val

  def __str__(self):
    if self.val>10:
      if self.val is 11:
        val = 'Jack'
      elif self.val is 12:
        val = 'Queen'
      elif self.val is 13:
        val = 'King'
      elif self.val is 14:
        val = 'Ace'
    else:
      val = self.val
    return str(val) + ' of ' + self.suit
    
## Taken from: https://codereview.stackexchange.com/questions/82103/ascii-fication-of-playing-cards
def ascii_version_of_card(*cards, return_string=True):
  #     """
  #     Instead of a boring text version of the card we render an ASCII image of the card.
  #     :param cards: One or more card objects
  #     :param return_string: By default we return the string version of the card, but the dealer hide the 1st card and we
  #     keep it as a list so that the dealer can add a hidden card in front of the list
  #     """
  #     # we will use this to prints the appropriate icons for each card
  #     suits_name = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
  #     suits_symbols = ['♠', '♦', '♥', '♣']

  #     # create an empty list of list, each sublist is a line
  #     lines = [[] for i in range(9)]

  #     for index, card in enumerate(cards):
  #         # "King" should be "K" and "10" should still be "10"
  #         if card.rank == '10':  # ten is the only one who's rank is 2 char long
  #             rank = card.rank
  #             space = ''  # if we write "10" on the card that line will be 1 char to long
  #         else:
  #             rank = card.rank[0]  # some have a rank of 'King' this changes that to a simple 'K' ("King" doesn't fit)
  #             space = ' '  # no "10", we use a blank space to will the void
  #         # get the cards suit in two steps
  #         suit = suits_name.index(card.suit)
  #         suit = suits_symbols[suit]

  #         # add the individual card on a line by line basis
  #         lines[0].append('┌─────────┐')
  #         lines[1].append('│{}{}       │'.format(rank, space))  # use two {} one for char, one for space or char
  #         lines[2].append('│         │')
  #         lines[3].append('│         │')
  #         lines[4].append('│    {}    │'.format(suit))
  #         lines[5].append('│         │')
  #         lines[6].append('│         │')
  #         lines[7].append('│       {}{}│'.format(space, rank))
  #         lines[8].append('└─────────┘')

  #     result = []
  #     for index, line in enumerate(lines):
  #         result.append(''.join(lines[index]))

  #     # hidden cards do not use string
  #     if return_string:
  #         return '\n'.join(result)
  #     else:
  #         return result
  pass

class Deck:
  def __init__(self):
    self.cards = []
    
    for suit in ['Hearts','Diamonds','Spades','Clubs']:
      for val in range(2,15):
        self.cards.append(Card(suit, val))

  def shuffle(self, all_cards=True):
    if all_cards:
      self.cards = []
      for suit in ['Hearts','Diamonds','Spades','Clubs']:
        for val in range(2,15):
          self.cards.append(Card(suit, val))
    random.shuffle(self.cards)

  def draw(self):
    return self.cards.pop()
    
def endless_war_for_points():
  d = Deck()
  d.shuffle()
  keep_playing = True

  print("Let's play War!\n\n")
  score = [0,0]

  while keep_playing and len(d.cards) > 1:
    input('Hit Enter to draw a card!')
    player_card = d.draw()
    comp_card = d.draw()
    print('You drew a ' + str(player_card) + ' and I drew the ' + str(comp_card) + ' which means...')

    # Who won?
    if player_card.val > comp_card.val: # The player!
      score[0] += 1
      print("You win!")
    elif player_card.val < comp_card.val: # The computer!
      score[1] += 1
      print("I win!!!! HAHAHAHHA :D")
    elif player_card.val == comp_card.val: # THE POSSIBLY ENDLESS DESTRUCTIVE CYCLE OF WAR BEGINS
      pot = 1
      while player_card.val == comp_card.val:
        print("IT'S WARRRRRRRRR")
        # Make sure there are enough cards to finish the war
        if len(d.cards) < 4:
          d.shuffle()
        d.draw() # Burn card
        d.draw() # Burn card

        input('Hit Enter to draw a card!')
        player_card = d.draw()
        comp_card = d.draw()
        pot += 2 # Increase pot for new cards

        print('You drew a ' + str(player_card) + ' and I drew the ' + str(comp_card) + ' which means...')

        # Who won? or will the while loop continue to run?
        if player_card.val > comp_card.val:
          score[0] += pot
          print("You win!")
        elif player_card.val < comp_card.val:
          score[1] += pot
          print("I win!!!! HAHAHAHHA :D")
        

    print("The score is\n\nPlayer: " + str(score[0]) + "\nComputer: " + str(score[1]) + "\n")  
    keep_playing = 'n' is not input("Would you like to keep playing? [y/n]")

  if len(d.cards) < 2:
    print("Sorry, I'm all outta cards :(")

  print("Thanks for playing!")

class Player():
  def __init__(self):
    self.hand = []
    self.pile = []

  def add_to_pile(self, card):
    self.pile.append(card)

def war_accumulating():
  d = Deck()
  d.shuffle()
  p1 = Player()
  cpu = Player()
  for i in range(26):
    p1.add_to_pile(d.draw())
  for i in range(26):
    cpu.add_to_pile(d.draw())

  print("Let's play War!\n\n")
  input('Hit Enter to draw a card!')

  while len(p1.hand) < 52 and len(cpu.hand) < 52:
    pot = []
    if len(p1.hand) == 0:
      random.shuffle(p1.pile)
      p1.hand = p1.pile
      p1.pile = []
    if len(cpu.hand) == 0:
      random.shuffle(cpu.pile)
      cpu.hand = cpu.pile
      cpu.pile = []
    player_card = p1.hand.pop()
    comp_card = cpu.hand.pop()
    pot = [player_card, comp_card]
    print('You drew a ' + str(player_card) + ' and I drew the ' + str(comp_card) + ' which means...')

    # Who won?
    if player_card.val > comp_card.val: # The player!
      print("You win!")
      for card in pot:
        p1.add_to_pile(card)
    
    elif player_card.val < comp_card.val: # The computer!
      print("I win!!!! HAHAHAHHA :D")
      for card in pot:
        cpu.add_to_pile(card)

    elif player_card.val == comp_card.val: # THE POSSIBLY ENDLESS DESTRUCTIVE CYCLE OF WAR BEGINS
      while player_card.val == comp_card.val:
        print("IT'S WARRRRRRRRR")
        # Make sure there are enough cards to finish the war
        if len(d.cards) < 4:
          d.shuffle()
        pot.append(d.draw()) # Burn card
        pot.append(d.draw()) # Burn card

        # input('Hit Enter to draw a card!')
        player_card = d.draw()
        comp_card = d.draw()
        pot.append(player_card) # Increase pot for new cards
        pot.append(comp_card)

        print('You drew a ' + str(player_card) + ' and I drew the ' + str(comp_card) + ' which means...')

        # Who won? or will the while loop continue to run?
        if player_card.val > comp_card.val:
          print("You win!")
          for card in pot:
            p1.add_to_pile(card)

        elif player_card.val < comp_card.val:
          print("I win!!!! HAHAHAHHA :D")
          for card in pot:
            cpu.add_to_pile(card)
  print(len(p1.hand))  
  print(len(cpu.hand))  
  if len(p1.hand) is 0:
    print('lol u lose')
  elif len(p1.hand) is 52:
    print('lol u win')        
war_accumulating()