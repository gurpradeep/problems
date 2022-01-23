def make_squares(arr):
    squares=[0 for i in range(len(arr))]
    left,right = 0,len(arr)-1
    idxSquare=len(arr)-1
    while(left <=right):
        leftSquare = arr[left]*arr[left]
        rightSquare = arr[right]*arr[right] 
        if leftSquare < rightSquare:
            squares[idxSquare]=rightSquare
            right-=1
        else:
            squares[idxSquare]=leftSquare
            left+=1
        idxSquare-=1
    return squares


print(make_squares([-7,-3,2,3,11]))