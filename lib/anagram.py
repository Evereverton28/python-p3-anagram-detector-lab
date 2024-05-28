class Anagram:
    def __init__(self, base_word):
        self.base_word = base_word.lower()
        
    def is_anagram(self, other_word):
        return sorted(self.base_word) == sorted(other_word.lower())

    def match(self, words):
        return [word for word in words if self.is_anagram(word) and word.lower() != self.base_word]
