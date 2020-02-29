from typing import Tuple
from findrootword import *
import string

class Trie(object):
    """
    Trie node implementation
    """
    def __init__(self, char):
        self.char = char
        self.children = []
        self.word_finished = False
        self.counter = 0

def add(root, word):
    """
    Adding a word into the Trie
    """
    curr_node = root
    # Looping through all characters in the word
    for char in word:
        found_in_child = False
        # Searching the children of the node to find whether the character exists
        for child in curr_node.children:
            if child.char == char:
                # If found, point to current node to the child that matches the character
                curr_node = child
                found_in_child = True
                break
        # If not found, add a new child that contains this character
        if not found_in_child:
            new_node = Trie(char)
            curr_node.children.append(new_node)

            # as above, point the current node to the new child node
            curr_node = new_node
    # Mark the end of the word, and increase the counter of the last node to count the frequency of the word
    curr_node.word_finished = True
    curr_node.counter += 1


def find_count(root, word) -> Tuple[str, int]:
    """
    Check if the word exists, return its frequency count
    """
    curr_node = root
    if not root.children:
        return False, 0
    for char in word:
        char_found = False
        # Search through all the children of the present `node`
        for child in curr_node.children:
            if child.char == char:
                # We found the char existing in the child.
                char_found = True
                # Assign node as the child containing the char and break
                curr_node = child
                break
        # Return False anyway when we did not find a char.
        if not char_found:
            return False, 0
    # Well, we are here means we have found the prefix. Return true to indicate that
    # And also the counter of the last node. This indicates how many words have this
    # prefix
    return word, curr_node.counter

    # if __name__ == "__main__":
def find_file_count(inputFilePath):
    wordList = []
    filePath = inputFilePath
    file = open(filePath, 'r')
    for line in file:
        for word in line.split():
            word = findRootWord(word)
            if word != None:
                word = word.translate(str.maketrans('', '', string.punctuation))
                word = word.lower()
                wordList.append(word)
            # print(wordList)
    root = Trie('*')
    for words in wordList:
        add(root, words)

        return find_count(root,words)

#print(find_file_count('testing.txt'))
# def process_file(user_input):
#
#     wordList = []
#     # filePath = 'testing.txt'
#     file = open(user_input, 'r')
#     for line in file:
#         for word in line.split():
#             word = findRootWord(word)
#             if word != None:
#                 word = word.translate(str.maketrans('', '', string.punctuation))
#                 word = word.lower()
#                 wordList.append(word)
#     # print(wordList)
#
#     root = Trie('*')
#     for words in wordList:
#         add(root, words)
#         # print(find_count(root, words))
#
#     return find_count(root,words)
