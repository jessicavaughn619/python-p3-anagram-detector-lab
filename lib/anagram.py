class Anagram:
    def __init__(self, word):
        self.word_letters = sorted([letter for letter in word])

    def match(self, word_list):
        match_word_list = []

        for word in word_list:
            if sorted([letter for letter in word]) == self.word_letters:
                match_word_list.append(word)

        return match_word_list

# Take word argument, break into individual letters

# Take list argument, for each word break into individual letters and sort

# Compare sorted word letters to each sorted word in list

# If sorted word matches sorted list, return matching word
