def max_profit(arr):
    # write your code here
    minNum = arr[0]
    indexNum = 0
    for i in range(len(arr)):
        if arr[i] < minNum:
            minNum = arr[i]
            indexNum =i

    maxNum=arr[indexNum]
    for j in range(indexNum, len(arr)):
        if arr[j] >=maxNum:
            maxNum=arr[j]

    profit = maxNum-minNum
    return profit

print(max_profit([7, 1, 5, 3, 6, 4]))