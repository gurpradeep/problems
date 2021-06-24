def lastNonConflict(index,schedule,isSorted):
    if not isSorted:
        sorted(schedule,key=lambda tup:tup[1])
    
    for i in range(index,-1,-1):
        if schedule[index][0]>=schedule[i][1]:
            return i
    return -1

def WSrecursive(schedule,n,memo):
    if n<0:
        return 0
    if n==0:
        return schedule[n][2]
    if n in memo:
        return memo[n]
    
    memo[n]=max(schedule[n][2]+WSrecursive(schedule,lastNonConflict(n,schedule,isSorted=True),memo),WSrecursive(schedule,n-1),memo)
    return memo[n]

def WeightedSchedule(schedule):
    sorted(schedule,key=lambda tup:tup[1])
    memo={}
    return WSrecursive(schedule,len(schedule)-1,memo)

print(WeightedSchedule([(0, 2, 25), (1, 6, 40), (6, 9, 170), (3, 8, 220)]))