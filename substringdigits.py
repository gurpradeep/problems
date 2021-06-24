def substr_digits(s):
    nlen = len(s)
    sum=[[0 for i in range(nlen)] for _ in range(nlen)]
    maxLen = 0

    for i in range(nlen):
        sum[i][i]=ord(s[i])-ord("0")

    for length in range(2,nlen):
        for i in range(nlen-length+1):
            j= i+length-1
            k = length//2
            sum[i][j]=sum[i][j-k]+sum[j-k+1][j]
            if length%2==0 and sum[i][j-k]==sum[(j-k+1)][j] and length > maxLen:
                maxLen=length

    return maxLen

print(substr_digits("9430723"))