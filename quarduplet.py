def find_array_quadruplet(arr, s):
    result = []
    for i in range(len(arr)):
        if len(result)==0:
            for j in range(i+1,len(arr)):
                if len(result)==0:
                    for k in range(j+1,len(arr)):
                        if len(result)==0:
                            for l in range(k+1,len(arr)):
                                if len(result)==0:
                                    if arr[i]+arr[j]+arr[k]+arr[l]==s:
                                        result.append((arr[i],arr[j],arr[k],arr[l]))
                                else:
                                    break
    return result





def find_array_quadruplet2(arr, s):
     result = []
    if len(arr)>4:
        arr.sort()
        for i in range(len(arr)-3):
            for j in range(i+1,len(arr)-2):
                left = j+1
                right = len(arr)-1

                while left<right:
                    sum = arr[i]+arr[j]+arr[left]+arr[right]
                    if(sum ==s):
                        result.append((i,j,left,right))
                        left+=1
                        right-=1
                    elif (sum < s):
                        left+=1
                    else:
                        right-=1
                
        return result




                

    

print(find_array_quadruplet2([2, 7, 4, 0, 9, 5, 1, 3],20))