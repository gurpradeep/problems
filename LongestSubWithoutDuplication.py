from collections import defaultdict

def longestSubstringWithoutDuplication2(string):
    lenStr = len(string)
    left,right = 0,0
    map = defaultdict()
    maxLen=0
    bestLeft,bestRight=0,0
    isDuplicate=False
    while right < lenStr:
        charValue = string[right]
        if charValue in map:
            isDuplicate=True
            tempLen = right-left
            if maxLen < tempLen:
                bestLeft = left
                if map[charValue] <left:
                    bestRight=right+1
                else:
                    left=right-1
                    bestRight=right
                maxLen=max(tempLen,maxLen)
            map[charValue]=right
        elif isDuplicate==False:
            map[charValue]=right
            tempLen = right-left+1
            if tempLen > maxLen:
                bestRight=right+1
                maxLen=max(tempLen,maxLen)
        else:
            map[charValue]=right
        
        right+=1
    return string[bestLeft:bestRight]

def longestSubstringWithoutDuplication(string):
    lenStr = len(string)
    left,right = 0,0
    map = defaultdict()
    maxLen=0
    while right < lenStr:
        charValue = string[right]
        if charValue in map:
            isDuplicate=True
            tempLen = right-left
            if maxLen < tempLen:
                bestLeft = left
                if map[charValue] <left:
                    bestRight=right+1
                else:
                    left=right-1
                    bestRight=right
                maxLen=max(tempLen,maxLen)
            map[charValue]=right
        elif isDuplicate==False:
            map[charValue]=right
            tempLen = right-left+1
            if tempLen > maxLen:
                bestRight=right+1
                maxLen=max(tempLen,maxLen)
        else:
            map[charValue]=right
        
        right+=1
    return string[bestLeft:bestRight]

#print(longestSubstringWithoutDuplication("abcb"))
#print(longestSubstringWithoutDuplication("clementisacap"))
print(longestSubstringWithoutDuplication("abcdeabcdefc"))

