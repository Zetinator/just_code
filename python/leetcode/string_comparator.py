"""https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=sorting&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

Comparators are used to compare two objects. In this challenge, you'll create a comparator and use it to sort an array. The Player class is provided in the editor below. It has two fields:
"""
from collections import namedtuple

Player = namedtuple('Player', ['name', 'score'])

def sort_data(players):
    players = [Player(*e) for e in players]
    players = sorted(players, key=lambda x: (x.score, [-ord(e) for e in x.name]))
    players.reverse()
    return players


# test
players = [('amy', 100),
        ('david', 100),
        ('heraldo', 50),
        ('aakansha', 75),
        ('aleksa', 150)]
print(f'testing with: test: {players}')
print(f'ans: {sort_data(players)}')
