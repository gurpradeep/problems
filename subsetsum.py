def subset_sum(ls: tuple, total: int, total_sum: int) -> bool:

    if total == total_sum:
        return True

    for idx, val in enumerate(ls):

        new_ls = ls[:idx] + ls[idx + 1:],
        if subset_sum(new_ls, total, val + total_sum):
            return True

    return False



nTuple = (3,34,4,12,4,2)
nLen = len(nTuple)
nSum=9
print(subset_sum(nTuple,nLen,nSum ))