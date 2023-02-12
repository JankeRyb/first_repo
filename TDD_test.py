# # #import functions
from functions import *
import pytest
# # print(multiply(5,6))
#
#
# def test_multiply():
#     assert multiply(5,10) == 50
#     assert multiply(100, 1.1) == 110
#     assert multiply(1.5, 1.5) == 2.25
#     assert multiply(0.0000001,100)==0.00001
#     assert multiply('mama',3) =='mamamamamama'
#     #assert multiply(None,5) == None
#
# def test_no_of_letters():
#     assert no_of_letters("xdddxd") == 6
#     assert no_of_letters('mama.tata') == 8 #mozna ten warunek poprawic

# @pytest.mark.parametrize('number, result', [(1,1),(3,'fizz'),(5,'buzz'),(15,'fizzbuzz')])
# def test_fizzbuzz_param(number,result):
#     assert fizzbuzz(number)==result
# def test_fizzbuzz_basic():
#     assert fizzbuzz(1)==1
#     assert fizzbuzz(2)==2
#     assert fizzbuzz(3)=='fizz'
#     assert fizzbuzz(4) == 4
#     assert fizzbuzz(5) == 'buzz'
#     assert fizzbuzz(6)=='fizz'
#     assert fizzbuzz(10) == 'buzz'
#     assert fizzbuzz(15) == 'fizzbuzz'
#
# def test_fizzbuzz_adv():
#     assert fizzbuzz(1.3) ==1
#     assert fizzbuzz(1.9) == 1
#     assert fizzbuzz('1') == 1
#     assert fizzbuzz('1.3') == 1
#     assert fizzbuzz(5.9) == 'buzz'
#     assert fizzbuzz('5.99') == 'buzz'
#     assert fizzbuzz(0) == None
#     assert fizzbuzz(0.999) == None
#     assert fizzbuzz('mama') == None
#     assert fizzbuzz(-5) == None
#     assert fizzbuzz('-15.8') == None
