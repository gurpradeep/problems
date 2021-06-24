def search_remain(remain,lst):
    first = 0
    last = len(lst)-1
    index=-1
    found=False
    while first <=last and not found:
        mid = first + last//2
        if lst[mid]==remain:
            index=mid
            found=True
        else:
            if remain < lst[mid]:
                last=mid-1
            else:
                first = mid+1
    if found:
        return index
    else:
        return -1


def find_sum(lst,sum):
    lst.sort()
    first=-1
    second=-1
    

    for i in lst:
        first=i
        remain = sum-i
        index = search_remain(remain,lst)
        if index!=-1:
            second=lst[index]
            break
    return first,second


print(find_sum([1, 2, 3, 4], 5))
print(find_sum([1, 2, 3, 4], 2))