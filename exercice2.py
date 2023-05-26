import sys

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

def main():
    if len(sys.argv) != 3:
        print("Erreur")
        return 1
    try:
        mode = sys.argv[1]
        mode = sys.argv[2]
        calculator = StringAnalyzer(sys.argv[1])
        if (mode == "count_vowels"):
            print(calculator.count_vowels())
        elif (mode == "count_consonants"):
            print(calculator.count_consonants())
        elif (mode == "count_digits"):
            print(calculator.count_digits())
        elif (mode == "count_words"):
            print(calculator.count_words())
        elif (mode == "count_lines"):
            print(calculator.count_lines())
        else:
            print("Erreur")
            return 1
        return 0
    except ValueError:
        print("Erreur")
        return 1

if __name__ == "__main__":
    main()