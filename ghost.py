#!/usr/bin/env python3

import random
import sys

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
    def __init__(self, filepath):
        self.word_tree = TreeNode('$')
        self.word_prep(filepath)

    @staticmethod
    def switch_players(players):
        p = players.pop(0)
        players.append(p)
        return players

    def game_loop(self, p1, p2):
        game_over = False
        current_str = ''
        if random.random() > 0.5:
            players = [p1, p2]
        else:
            players = [p2, p1]
        print('Welcome to ghost! To see the rules, open the readme.md included in this repository.\n' \
              f'{current_player.capitalize()} will begin this round.')
        while not game_over:
            new_letter = get_input(players[0], current_str)
            print(f'trying {current_str}{new_letter})
            response_code = self.string_valid(f'{current_str}{new_letter}')
            if response_code == 0:
                players = self.switch_players(players)
                current_str = f'{current_str}{new_letter}'
            elif response_code == 1:
                players[0].strikes += 1
                print(f'{current_str}{new_letter} is not a valid beginning to a word.')
                if players[0].strikes = 3:
                    print(f'Oh no, {players[0]}! That was your 3rd strike!\n' \
                          f'That means {players[0]} is the loser, and {players[1]} is the victor!')
                    game_over = True
                else:
                    strike_string = f'{players[0].capitalize()}, you now have {players[0].strikes} strike'
                    if players[0].strikes == 1:
                        print(f'{strike_string}.')
                    else:
                        print(f'{strike_string}s.')
            elif response_code == 2:
                print(f'Uh oh, {players[0]}! Since {current_str}{new_letter} is a real word, you lose!\n' \
                      f'Congratulations on the win, {players[1]}.')
                game_over = True
        return 0


    def get_input(self, player, current_str):
        while 1:
            if len(current_str) > 0:
                print(f'The current string is {current_str}.')
            string = input(f'Type your letter and press [enter].\n[{player}]> ')
            if len(string) > 1:
                print('Please type only 1 character, and try again.')
            elif not string.isalpha():
                print('Please only use a character from the English alphabet, and try again.')
            else:
                return string.lower()

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

    def string_valid(self, string):
        current_node = self.word_tree
        buffer = 0
        for letter in string:
            buffer += 1
            if letter in current_node.children.keys():
                current_node = current_node.children[letter]
            else:
                print(f'{string} does not begin a real word.')
                return 1
            if current_node.word_terminator and buffer > 3:
                print(f'{string} is a real, full word.')
                return 2
        print('keep playing')
        return 0

    def word_prep(self, file_path):
        with open(file_path, 'r') as f:
            for line in f:
                self.add_word(line.strip())

if __name__ == '__main__':
    p1 = Player(1)
    p2 = Player(2)
    g = Ghoster('wordlist_kevin_atkinson.txt')
    while 1:
        g.game_loop()
        response = input('Play again? [y/n]\n(All answers not \'y\' or \'Y\' will be counted as no).')
        if response in 'yY':
            continue
        else:
            print('Thank you for playing!')
            sys.exit(0)
