def test(n):
    j=1
    while (j < n):
        k =j
        while (k < n):
            if k // 2:
                k+=0.01*n
            else:
                k+=1
        j+=0.1*n

print(test(10))        