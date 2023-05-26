import pytest
import os.path
# os.chdir('../')

def test_add_positive_res():
    output = os.popen("python3 exercice1.py 2 2 add").read()
    assert output.strip() == "4.0"

def test_add_negative_res():
    output = os.popen("python3 exercice1.py -22 2 add").read()
    assert output.strip() == "-20.0"

def test_subtract_positive_res():
    output = os.popen("python3 exercice1.py 233 9 subtract").read()
    assert output.strip() == "224.0"

def test_subtract_negative_res():
    output = os.popen("python3 exercice1.py 17 26 subtract").read()
    assert output.strip() == "-9.0"

def test_multiply_positive_res():
    output = os.popen("python3 exercice1.py 16 3 multiply").read()
    assert output.strip() == "48.0"

def test_multiply_negative_res1():
    output = os.popen("python3 exercice1.py -27 8 multiply").read()
    assert output.strip() == "-216.0"

def test_multiply_negative_res2():
    output = os.popen("python3 exercice1.py -27 -8 multiply").read()
    assert output.strip() == "216.0"

def test_divide_positive_res():
    output = os.popen("python3 exercice1.py 30 2 divide").read()
    assert output.strip() == "15.0"

def test_divide_negative_res():
    output = os.popen("python3 exercice1.py -9 2 divide").read()
    assert output.strip() == "-4.5"

def test_divide_by_zero():
    output = os.popen("python3 exercice1.py 147 0 divide").read()
    assert output.strip() == "Erreur"

def test_power_positive_res():
    output = os.popen("python3 exercice1.py 10 3 power").read()
    assert output.strip() == "1000.0"

def test_power_positive_res2():
    output = os.popen("python3 exercice1.py -9 4 power").read()
    assert output.strip() == "6561.0"

def test_sqrt_positive_res():
    output = os.popen("python3 exercice1.py 11 2 sqrt").read()
    assert output.strip() == "3.3166247903554"

def test_sqrt_positive_res2():
    output = os.popen("python3 exercice1.py 78 -678 sqrt").read()
    assert output.strip() == "8.831760866327848"
