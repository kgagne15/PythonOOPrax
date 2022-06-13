"""Word Finder: finds random words from a dictionary."""

#1. instantiate with a path to a file that contains words
#2. reads that file and makes an attribute that is a list of
#those words (probably a separate method that is called in __init__)
#3. prints out a str that says "[number of words read] words read"
#4. method random is made to return random word from list of words
#5. the random method should not re-read the entire list but rather
#work from the list of words that have already been read
#6. this will need to strip the /n from each word (like the python function
#further study 5 problem)

import random

class WordFinder:
    ...
    def __init__(self, path):
        """Initialize the WordFinder class. Prints number of words to find

        Attributes
        ---------
        path: name of file to be read
        words: list of words from that file
        num_words: number of words in list words
        """
        self.path = path
        self.words = self.read()
        self.num_words = len(self.words)
        print(f'{self.num_words} words read')

    def read(self):
        """Opens file based on path name provided and creates a list 
        with each word from that file"""
        word_lst = []
        file = open(f'{self.path}.txt', 'r')
        for line in file:
            line = line.rstrip()
            word = (line)
            word_lst.append(word)
        return word_lst
    
    def random(self):
        """selects random index and returns the word from words at that index"""
        rand_word_idx = random.randint(1, self.num_words)
        return self.words[rand_word_idx]
