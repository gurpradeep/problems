def diskStacking(disks):
    
    for disk in disks:
        diskW = disk[0]
        diskD = disk[1]
        diskH = disk[2]

    for width in range(len(diskW)):
        idx, value = getMax(diskW)

    


def getMax(dimArray):
    max = dimArray[0]

    for i in range(1, len(dimArray)):
        if dimArray[i]>max:
            max=dimArray[i]
            maxIdx=i
        
    return maxIdx,max   
