def find_permutation_first(str1, pattern):
  window_start, matched = 0, 0
  char_frequency = {}

  for chr in pattern:
    if chr not in char_frequency:
      char_frequency[chr] = 0
    char_frequency[chr] += 1

  # our goal is to match all the characters from the 'char_frequency' with the current window
  # try to extend the range [window_start, window_end]
  for window_end in range(len(str1)):
    print(str1[window_start:window_end+1])  
    right_char = str1[window_end]
    if right_char in char_frequency:
      # decrement the frequency of matched character
      char_frequency[right_char] -= 1
      if char_frequency[right_char] == 0:
        matched += 1

    if matched == len(char_frequency):
      return True

    # shrink the window by one character
    if window_end >= len(pattern) - 1:
      left_char = str1[window_start]
      window_start += 1
      if left_char in char_frequency:
        if char_frequency[left_char] == 0:
          matched -= 1
        char_frequency[left_char] += 1

  return False

def find_permutation(str1, pattern):

    win_start, win_end,matched=0,0,0
    dict_pattern={}

    for char in pattern:
        if char not in dict_pattern:
            dict_pattern[char]=0
        dict_pattern[char]+=1

    for win_end in range(len(str1)):
        right = str1[win_end]
        if right in dict_pattern:
            dict_pattern[right]-=1
            if dict_pattern[right]==0:
                matched+=1
        
        if matched == len(pattern):
            return True

        if win_end+1>=len(pattern):
            left=str1[win_start]
            win_start+=1
            if left in dict_pattern:
                if dict_pattern[left]==0:
                   matched-=1
                dict_pattern[left]+=1   






    
    return False

def main():
  print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
  print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
  print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
  print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))


main()