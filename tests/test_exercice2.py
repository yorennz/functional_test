import pytest
import os.path
# os.chdir('../')

def test_count_vowels1():
    output = os.popen("python3 exercice2.py abeille count_vowels").read()
    assert output.strip() == "4"

def test_count_vowels2():
    output = os.popen("python3 exercice2.py pwn count_vowels").read()
    assert output.strip() == "0"

def test_count_consonants1():
    output = os.popen("python3 exercice2.py yoyo count_consonants").read()
    assert output.strip() == "0"

def test_count_consonants2():
    output = os.popen("python3 exercice2.py pwn count_consonants").read()
    assert output.strip() == "3"

def test_count_digits1():
    output = os.popen("python3 exercice2.py 2d379DDHOI9 count_digits").read()
    assert output.strip() == "5"

def test_count_digits2():
    output = os.popen("python3 exercice2.py 1456789765 count_digits").read()
    assert output.strip() == "10"

def test_count_words1():
    output = os.popen("python3 exercice2.py \"Hello world\" count_words").read()
    assert output.strip() == "2"

def test_count_words2():
    output = os.popen("python3 exercice2.py \"How are you mate .\" count_words").read()
    assert output.strip() == "5"

def test_count_lines1():
    output = os.popen("python3 exercice2.py \"Hello\nw\nor\nld\" count_lines").read()
    assert output.strip() == "4"

def test_count_lines2():
    output = os.popen("python3 exercice2.py \"How are \nyou\n\n\n\n mate .\" count_lines").read()
    assert output.strip() == "6"
