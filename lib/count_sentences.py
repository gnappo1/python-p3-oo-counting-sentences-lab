#!/usr/bin/env python3
import re
from functools import reduce

class MyString:
  def __init__(self, sentence = None):
    self._value = None
    self._sentence = sentence
  
  def get_value(self):
    self._value
  
  def set_value(self, string):
    self._value = string if type(string) == type('x') else print("The value must be a string.")
  
  def is_sentence(self):
    return True if self._sentence[-1] == "." else False
  
  def is_question(self):
    return True if self._sentence[-1] == "?" else False
  
  def is_exclamation(self):
    return True if self._sentence[-1] == "!" else False
  
  def count_sentences(self):
    if not self._sentence:
      return 0
    sentences_array = re.split(r"[.?!]", self._sentence)
    return reduce(lambda acc, s: acc + 1 if s != "" else acc, sentences_array, 0)


  value = property(get_value, set_value)

# import ipdb; ipdb.set_trace()