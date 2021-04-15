from collections import Counter
from heapq import heappush, heappop
def reorganize_results(initial_order):
    """
    :type initial_order: str
    :rtype: str
    """
    print (Counter(initial_order).most_common(1)[0])

    max_freq = Counter(initial_order).most_common(1)[0][1]
    if 2 * max_freq -1 > len(initial_order):
        return initial_order
    
    heap = []
    for c, freq in Counter(initial_order).items():
        heappush(heap, (freq*-1, c))
    result = []
    while heap:
        freq,c = heappop(heap)
        if not result or c != result[-1]: 
            result.append(c)
            if freq != -1:
                heappush(heap,(freq+1,c))
        else:                             
            freq1, c1 = heappop(heap)
            result.append(c1)
            heappush(heap, (freq, c))
            if freq1 != -1:
                heappush(heap, (freq1+1, c1))
    return "".join(result)

## Driver code
initial_order = "bbnnc"
print(reorganize_results(initial_order))