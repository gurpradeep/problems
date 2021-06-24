def find_boundary2(arr):

    left, right = 0, len(arr)-1

    boundary_index=-1

    while left<right:
        mid = (left + right)//2
        if arr[mid]:
            boundary_index =mid
            right = mid-1
        else:
            left = mid+1
        
    
    return boundary_index




def find_boundary(arr):
    left, right = 0, len(arr) - 1
    boundary_index = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index

# Driver code
print("Find boundary :", find_boundary2([False, False, True, True, True]))
print("Find boundary :", find_boundary2([True]))
print("Find boundary :", find_boundary2([False, False, False]))
print("Find boundary :", find_boundary2([False, False, True, True, True]))
print("Find boundary :", find_boundary2([True, True, True, True, True]))
print("Find boundary :", find_boundary2([False, True]))