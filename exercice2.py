class StringAnalyzer:
    def __init__(self, input_string):
        self.input_string = input_string

    def count_vowels(self):
        vowels = "aeiou"
        count = 0
        for char in self.input_string.lower():
            if char in vowels:
                count += 1
        return count

    def count_consonants(self):
        consonants = "bcdfghjklmnpqrstvwxyz"
        count = 0
        for char in self.input_string.lower():
            if char in consonants:
                count += 1
        return count

    def count_digits(self):
        digits = "0123456789"
        count = 0
        for char in self.input_string:
            if char in digits:
                count += 1
        return count

    def count_words(self):
        words = self.input_string.split()
        return len(words)

    def count_lines(self):
        lines = self.input_string.split("\n")
        return len(lines)
