def find_product(lst):

    result=[]
    left =1

    for index in range(len(lst)):
        currentProduct=1
        for elem in lst[index+1:]:
            currentProduct = elem*currentProduct
        
        currentProduct = left*currentProduct
        result.append(currentProduct)
        left = left*lst[index]
    return result


def find_product2(lst):
    # get product start from left
    left = 1
    product = []
    for ele in lst:
        product.append(left)
        left = left * ele
    # get product starting from right
    right = 1
    for i in range(len(lst)-1, -1, -1):
        product[i] = product[i] * right
        right = right * lst[i]

    return product

print(find_product2([1, 2, 3, 4]))