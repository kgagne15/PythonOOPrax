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

#used solution for help, but not entirely
#helpful link: https://www.w3schools.com/python/ref_random_randint.asp

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
        file.close()
        return word_lst
    
    def random(self):
        """selects random index and returns the word from words at that index"""
        rand_word_idx = random.randint(1, self.num_words)
        return self.words[rand_word_idx]


class SpecialWordFinder(WordFinder):
    def parse(self):
        """opens file and returns all words not commented out 
        and removes all spaces between words"""
        file = open(f'{self.path}.txt', 'r')
        word_lst = []
        for line in file:
            if line[0] != '#' and line.rstrip():
                line = line.rstrip()
                word_lst.append(line)
        file.close()
        return word_lst
                
        