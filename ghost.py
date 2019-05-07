#!/usr/bin/env python3

class TreeNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = dict()
        self.word_terminator = False


class Player:
    def __init__(self, number):
        self.number = number
        self.strikes = 0


class Ghoster:
    def __init__(self):
        self.word_tree = TreeNode('$')

    def add_word(self, word):
        current_node = self.word_tree
        for letter in word:
            has_child = False
            for child in current_node.children.keys():
                if child = letter:
                    current_node = current_node.children[child]
                    has_child = True
                    break
            if not has_child:
                new_node = TreeNode(letter)
                current_node.children[letter] = new_node
                current_node = new_node
        current_node.word_terminator = True

    def string_valid(self, string):
        current_node = self.word_tree # womb
        for letter in string:
            if current_node.word_terminator and len(string) > 3:
                return False
            if letter in current_node.children.keys():
                current_node = current_node.children[letter]
                continue
            else:
                return False
        return True


    def word_prep(self, file_path):
        with open(filepath, 'r') as f:


if __name__ == '__main__':
