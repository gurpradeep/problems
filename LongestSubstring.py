def lengthOfLongestSubstring(s):

    count =0
    visited={}
    found =0
    
    for i in range(len(s)):
        if s[i] in visited:
            found = max(count,found)
            count=0
        count+=1
        visited[s[i]]=1

    return found

s = ""
print(lengthOfLongestSubstring(s))

s = "bbbbb"
print(lengthOfLongestSubstring(s))

s = "pwwkew"
print(lengthOfLongestSubstring(s))