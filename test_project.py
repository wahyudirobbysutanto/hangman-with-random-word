from project import get_character_choice, get_difficulty_choice, get_valid_word
import pytest
import sys

datatest = [['gspbx']]
datatest2 = ['12341']
datatestError = []

def test_get_character_choice():
    assert get_character_choice("1") == ""
    assert get_character_choice("2") == ""
    assert get_character_choice("3") == ""
    assert get_character_choice("0") == f"\nPlease input only 1 or 2 or 3\n"
    assert get_character_choice("a") == f"\nPlease input only 1 or 2 or 3\n"

def test_get_difficulty_choice():
    assert get_difficulty_choice("1") == ""
    assert get_difficulty_choice("2") == ""
    assert get_difficulty_choice("3") == ""
    assert get_difficulty_choice("0") == f"\nPlease input only 1 or 2 or 3\n"
    assert get_difficulty_choice("a") == f"\nPlease input only 1 or 2 or 3\n"

def test_get_valid_word():
    assert get_valid_word(datatest) == ['gspbx']
    assert get_valid_word(datatest2) == '12341'
    assert  get_valid_word(datatestError) == []