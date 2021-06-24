def findSubArrays(arr):
    nLen = len(arr)
    indexMap=[]
    
    for i in range(nLen):
        sum = arr[i]
        if (i<nLen-1):
            for j in range(i+1,nLen):
                print (i,j)
                sum += arr[j]
                if sum ==0:
                    indexMap.append((i,j))

    return indexMap           
                


if __name__ == '__main__':
    arr = [6, 3, -1, -3, 4, -2,2, 4, 6, -12, -7]
    out = findSubArrays(arr)
    for i in range(len(out)):
        print(out[i],end=" ")
        
