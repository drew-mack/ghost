#!/usr/bin/env python3

import time

class TreeNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = dict()
        self.word_terminator = False

    def __repr__(self):
        return self.letter


class Player:
    def __init__(self, number):
        self.number = number
        self.strikes = 0

    def __repr__(self):
        return f'player {self.number}'


class Ghoster:
    def __init__(self):
        self.word_tree = TreeNode('$')

    def add_word(self, word):
        current_node = self.word_tree
        for letter in word:
            if letter in current_node.children.keys():
                current_node = current_node.children[letter]
                continue
            else:
                new_node = TreeNode(letter)
                current_node.children[letter] = new_node
                current_node = new_node
        current_node.word_terminator = True

    def string_valid(self, string, player):
        current_node = self.word_tree
        buffer = 0
        for letter in string:
            buffer += 1
            if letter in current_node.children.keys():
                current_node = current_node.children[letter]
                print(current_node)
            else:
                print(f'{string} does not begin a real word.')
                return False
            if current_node.word_terminator and buffer > 3:
                print(f'{string} is a word. {player} loses.')
                return False
        print('keep playing')
        return True

    def word_prep(self, file_path):
        with open(file_path, 'r') as f:
            for line in f:
                self.add_word(line.strip())

if __name__ == '__main__':
    p1 = Player(1)
    p2 = Player(2)
    g = Ghoster()
    g.word_prep('wordlist_kevin_atkinson.txt')
    print(g.string_valid('anything', p1))
