# A pangram is a sentence that contains every single letter of the alphabet at
# least once. For example, the sentence "The quick brown fox jumps over the lazy
# dog" is a pangram, because it uses the letters A-Z at least once
# (case is irrelevant).
#
# Given a string, detect whether or not it is a pangram. Return True if it is,
# False if not. Ignore numbers and punctuation.

import string

def is_pangram(s):
    return True if set('abcdefghijklmnopqrstuvwxyz').issubset(set(s.lower())) else False
# def is_pangram(s):
#     def char_range(c1, c2):
#         for c in range(ord(c1), ord(c2)+1):
#             yield chr(c)
#     count = 0
#     s = s.lower()
#     for c in char_range('a', 'z'):
#         if s.find(c) != -1:
#             count += 1
#     return True if count == 26 else False

pangram = "The quick, brown fox jumps over the lazy dog!"
print(is_pangram(pangram)) #True
