def can_segment_string(word, wordList):
    wordLen = len(word)
    return any ([(word[i:] in wordList) and can_segment_string(word[:i],wordList) for i in range(1, wordLen+1)])


s = "applepie"
dictionary= set(["pear", "pie", "apple", "peach"])
dict2 = can_segment_string(s, dictionary)
if len(dict)>0:
  print("String Can be Segmented")
else:
  print("String Can NOT be Segmented")