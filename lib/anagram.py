# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, candidates):
        matches = []
        sorted_word = sorted(self.word)
        
        for candidate in candidates:
            if len(candidate) == len(self.word) and candidate.lower() != self.word:
                if sorted(candidate.lower()) == sorted_word:
                    matches.append(candidate)

        return matches
