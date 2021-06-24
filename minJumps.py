def minNumberOfJumps(array):
    # Write your code here.
    arrayLen = len(array)
    idx=0
    steps=0
    while idx > 0 and idx < arrayLen :
        currentVal = array[idx]
        maxIdx, maxval = findMax(array, idx, currentVal,arrayLen)
        idx = maxIdx
        steps=steps + 1
        print(maxIdx,maxval)
    
    return steps

def findMax(array, index,value,nLen ):
	maxIdx = index
	maxVal = 0
  
	for i in range(index+1,index + value+1 ):
        if array[i] > maxVal:
            maxVal=array[i]
            maxIdx=i
        else:
            maxIdx=-1

	return maxIdx, maxVal	
	
	
array=[3,4,2,1,2,3,7,1,1,1,3]
print(minNumberOfJumps(array))