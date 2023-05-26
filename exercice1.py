import sys

class Calculator:
    def __init__(self):
        self.memory = 0

    def add(self, a, b):
        result = a + b
        self.memory = result
        return result

    def subtract(self, a, b):
        result = a - b
        self.memory = result
        return result

    def multiply(self, a, b):
        result = a * b
        self.memory = result
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.memory = result
        return result

    def power(self, a, b):
        result = a ** b
        self.memory = result
        return result

    def sqrt(self, a):
        if a < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        result = a ** 0.5
        self.memory = result
        return result

    def clear_memory(self):
        self.memory = 0

    def get_memory(self):
        return self.memory

def main():
    if len(sys.argv) != 4:
        print("Erreur")
        return 1
    try:
        nb1 = float(sys.argv[1])
        nb2 = float(sys.argv[2])
        mode = sys.argv[3]
        calculator = Calculator()
        if (mode == "add"):
            print(calculator.add(nb1, nb2))
        elif (mode == "subtract"):
            print(calculator.subtract(nb1, nb2))
        elif (mode == "multiply"):
            print(calculator.multiply(nb1, nb2))
        elif (mode == "divide"):
            print(calculator.divide(nb1, nb2))
        elif (mode == "power"):
            print(calculator.power(nb1, nb2))
        elif (mode == "sqrt"):
            print(calculator.sqrt(nb1))
        else:
            print("Erreur")
            return 1
        return 0
    except ValueError:
        print("Erreur")
        return 1

if __name__ == "__main__":
    main()