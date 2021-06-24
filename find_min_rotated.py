def find_min_rotated(arr):

    left ,right = 0, len(arr)-1
    minIndex=-1
    while left < right:
        mid = (right + left)//2
        if arr[mid] <= arr[-1]:
            minIndex = mid
            right = mid -1
        else:
            left = mid +1
    return minIndex

print("Find minimum rotated :", find_min_rotated([30, 40, 50, 10, 20]))
print("Find minimum rotated :", find_min_rotated([0, 1, 2, 3, 4, 5]))
print("Find minimum rotated :", find_min_rotated([0]))

