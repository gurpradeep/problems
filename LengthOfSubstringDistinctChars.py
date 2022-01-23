def lengthOfLongestSubstringDistinctChars(s,k):
   maxLen=0
   winPosStart,currentPos=0,0
   distinctWord={}
   while currentPos < len(s):
        if s[currentPos] not in distinctWord:
            distinctWord[s[currentPos]]=1
        else:
            distinctWord[s[currentPos]]+=1
        
        if len(distinctWord)>k:
            distinctWord[s[winPosStart]]-=1
            winPosStart+=1
            if distinctWord[s[winPosStart]] == 0:
                distinctWord.pop(s[winPosStart])
                #currentPos is 0 indexed
                tempLen = currentPos-winPosStart+1 
                maxLen=max(tempLen,maxLen)
        
        currentPos+=1


   return maxLen

#s = "arraci"
#print(lengthOfLongestSubstringDistinctChars(s,2))

s = "arraci"
print(lengthOfLongestSubstringDistinctChars(s,1))

s = "cbbebi"
print(lengthOfLongestSubstringDistinctChars(s,3))

s = "cbbebi"
print(lengthOfLongestSubstringDistinctChars(s,10))
