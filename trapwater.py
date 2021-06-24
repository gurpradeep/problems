def trap(height):
    nLen = len(height)
    
    left_view =[0 for _ in range(nLen)]
    left_max=0
    for i in range(nLen):
        bar_height = height[i]
        left_view[i] =left_max 
        left_max = max(left_max,bar_height)
    
    right_view =[0 for _ in range(nLen)]
    right_max=0
    for r in reversed(range(nLen)):
        bar_height = height[r]
        right_view[r] =right_max 
        right_max = max(right_max,bar_height)   
        
    trap_water=[0 for _ in range(nLen)]
    for w in range(nLen):
        min_height = min(left_view[w],right_view[w])
        if height[w]<min_height:
            trap_water[w]= min_height-height[w]
        else:
            trap_water[w]=0
    
    return sum(trap_water)


heights = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(heights))