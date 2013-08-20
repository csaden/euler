# In the card game poker, a hand consists of five cards
# and are ranked, from lowest to highest, in the following way:
# 
# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
# The cards are valued in the order:
# 
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
# 
# If two players have the same ranked hands then the rank made
# up of the highest value wins; for example, a pair of eights beats
# a pair of fives (see example 1 below). But if two ranks tie,
# for example, both players have a pair of queens,
# then highest cards in each hand are compared
# (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.
# 
# Consider the following five hands dealt to two players:
# 
# The file, poker.txt, contains one-thousand random hands dealt to two players.
# Each line of the file contains ten cards (separated by a single space):
# 		the first five are Player 1's cards and
#		the last five are Player 2's cards.
#
# You can assume that all hands are valid (no invalid characters or repeated cards),
# each player's hand is in no specific order, and in each hand there is a clear winner.
# 
# How many hands does Player 1 win?

def poker(hands):
	"Returns the index of the winning poker hand from [hands...]"
	return max(hands, key=hand_rank)

def hand_rank(hand):
	"Return a value indicating the ranking of the hand"
	ranks = card_ranks(hand)
	if straight(ranks) and flush(hand):
		return (8, max(ranks))
	elif kind(4, ranks):
		return (7, kind(4, ranks), kind(1, ranks))
	elif kind(3, ranks) and kind(2, ranks):
		return (6, kind(3, ranks), kind(2, ranks))
	elif flush(hand):
		return (5, ranks)
	elif straight(ranks):
		return (4, max(ranks))
	elif kind(3, ranks):
		return (3, kind(3, ranks), ranks)
	elif two_pair(ranks):
		return (2, two_pair(ranks), kind(1, ranks))
	elif kind(2, ranks):
		return (1, kind(2, ranks), ranks)
	else:
		return (0, ranks)

def card_ranks(hand):
	"Returns a list of the ranks, sorted with higher first."
	ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
	ranks.sort(reverse=True)
	return [5,4,3,2,1] if (ranks == [14,5,4,3,2]) else ranks

def kind(n, ranks):
	"""Returns the first rank that the hand has exactly n of.
	Return None if there is no n-of-a-kind in the hand."""
	for r in ranks:
		if ranks.count(r) == n: return r
	return None

def straight(ranks):
	"Return True if the ordered ranks form a 5-card straight."
	return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def flush(hand):
	"Return True if the hand contains 5 cards of the same suit."
	suits = [s for r,s in hand]
	return len(set(suits)) == 1

def two_pair(ranks):
	"Returns the ranks of the two pairs in the hand (highest, lowest); otherwise, return None."
	pair = kind(2, ranks)
	low_pair = kind(2, list(reversed(ranks)))
	if pair and low_pair != pair:
		return (pair, low_pair)
	else:
		return None

Player1 = 0
Player2 = 0

def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99*[fh]) == sf
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    return 'tests pass'

test()

with open("0054euler_poker.txt", "r") as f:
	for line in f:
		line = line.strip()
		cards = line.split()
		player_hands = [cards[0:5], cards[5:10]]
		print player_hands, poker(player_hands)
		if player_hands.index(poker(player_hands)) == 0:
			Player1 += 1
		else:
			Player2 += 1

print "Player1 won", Player1, "games."
print "Player2 won", Player2, "games."


