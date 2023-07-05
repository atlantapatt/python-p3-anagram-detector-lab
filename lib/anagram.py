# your code goes here!

class Anagram:

    def __init__(self, word):
        self.word = word

    def match(self, anagrams):
        word = self.word
        match = []
        for anagram in anagrams:
            if(sorted(word) == sorted(anagram)):
                match.append(anagram)
        return match