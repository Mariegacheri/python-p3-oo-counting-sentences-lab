#!/usr/bin/env python3# test_count_sentences.py
# count_sentences.py
import re  # Import the 're' module for regular expressions

class MyString:
    def __init__(self, value=""):
        if not isinstance(value, str):
            raise ValueError("The value must be a string.")
        self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        sentences = [s.strip() for s in re.split('[.!?]', self.value) if s.strip()]
        return len(sentences)

# count_sentences_test.py
import io
import sys
import unittest

class TestMyString(unittest.TestCase):
    def test_is_class(self):
        '''is a class with the name "MyString".'''
        string = MyString()
        string.value = "This is a string! It has three sentences. Right?"
        self.assertIsInstance(string, MyString)

    def test_value_string(self):
        '''raises ValueError if not string.'''
        with self.assertRaises(ValueError):
            string = MyString(123)

    def test_is_sentence(self):
        '''returns True if value ends with a period and False otherwise.'''
        string = MyString("Hello World.")
        self.assertTrue(string.is_sentence())

    def test_is_question(self):
        '''returns True if value ends with a question mark and False otherwise.'''
        string = MyString("Is anybody there?")
        self.assertTrue(string.is_question())

    def test_is_exclamation(self):
        '''returns True if value ends with an exclamation mark and False otherwise.'''
        string = MyString("It's me!")
        self.assertTrue(string.is_exclamation())

    def test_count_sentences(self):
        '''returns the number of sentences in the value.'''
        simple_string = MyString("one. two. three?")
        self.assertEqual(simple_string.count_sentences(), 3)

    def test_value_string(self):
         '''prints "The value must be a string." if not string.''' 
         captured_out = io.StringIO()
         string = MyString()
         string.value = 123
    
if __name__ == '__main__':
    unittest.main()
