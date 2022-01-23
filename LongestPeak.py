def longestPeak(array):

    longestPeak=0
    peakIdx=[]
    # peak will start after index 0
    i=1
    while i < len(array)-1:
        isPeak = array[i-1] < array[i] and array [i] > array[i+1]
        if not isPeak:
            i+=1
            continue

        leftIdx = i-2
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx+1]:
            leftIdx-=1
        rightIdx=i+2
        while rightIdx >= 0 and array[rightIdx] < array[rightIdx-1]:
            rightIdx-=1

        currentPeakLength = rightIdx-leftIdx-1
        peakIdx.append((i,currentPeakLength))
        i=rightIdx

        return peakIdx


print (longestPeak([1, 1, 1, 2, 3, 10, 12, -3, -3, 2, 3, 45, 800, 99, 98, 0, -1, -1, 2, 3, 4, 5, 0, -1, -1]))
print (longestPeak([1, 2, 3, 3, 4, 0, 10]))
