def decode_ways(digits):

    prefixes = [str(i) for i in range(1,27)]
    level:int =0

    def dfs(i):
        nonlocal level
        
        print("****New level****", level)
        if i == len(digits):
            level -= 1
            return 1
        
        level +=1
        ways =0

        remaining = digits[i:]

        print("remaining: ", remaining)

        for prefix in prefixes:
            if remaining.startswith(prefix):
                print("prefix: ", prefix)
                print("substring len:", i+len(prefix))                
                ways+= dfs(i+len(prefix))

        return ways

    return dfs(0)


# Driver code
#inputs = ["12", "123", "11223"]
inputs = ["11223"]
for i in range(len(inputs)):
    print("Decode ways : ",decode_ways(inputs[i]))