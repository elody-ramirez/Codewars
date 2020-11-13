# What is an anagram? Well, two words are anagrams of each other if they both
# contain the same letters. For example:
#
# 'abba' & 'baab' == true
#
# 'abba' & 'bbaa' == true
#
# 'abba' & 'abbba' == false
#
# 'abba' & 'abca' == false
#
# Write a function that will find all the anagrams of a word from a list. You
# will be given two inputs a word and an array with words. You should return an
# array of all the anagrams or an empty array if there are none. For example:
#
# anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
#
# anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) =>
#                                                             ['carer', 'racer']
#
# anagrams('laser', ['lazing', 'lazy',  'lacer']) => []

def anagrams(word, words):
    return [w for w in words if sorted(word) == sorted(w)]

# BRUTE FORCE METHOD
# def anagrams(word, words):
#     result =[]
#     for i in range(0, len(words)):
#         if (sorted(word) == sorted(words[i])):
#             result.append(words[i])
#     return result

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
# ['aabb', 'bbaa']
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
# ['carer', 'racer']
