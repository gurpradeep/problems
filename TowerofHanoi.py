def towers_of_hanoi(start,dest,extra,n):
    if n <=0:
        return
    towers_of_hanoi(start,extra,dest,n-1)
    print("Move Disk-%d From %s To %s" % (n,start,dest))
    towers_of_hanoi(extra,dest,start,n-1)



print(towers_of_hanoi('s','d','e',3))