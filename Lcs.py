def LCSRecurse(str1,str2,left,right):

    if left==len(str1) or right==len(str2):
        return 0

    if str1[left]!=str2[right]:
        return max(LCSRecurse(str1,str2,left+1,right),LCSRecurse(str1,str2,left,right+1))


    if str1[left]==str2[right]:
        return 1+LCSRecurse(str1,str2,left+1,right+1)



def LCS(str1,str2):
    return LCSRecurse(str1,str2,0,0) 

print(LCS("hustle", "uncle"))