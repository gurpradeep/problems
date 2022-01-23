def insertionSort(array):
    for i in range( 1, len( array)):
        j = i-1 
        element_next = array[ i] 
        while (array[ j] > element_next) and (j >= 0): 
            array[ j + 1] = array[ j] 
            j = j-1 
            array[ j + 1] = element_next 
    return array

print(insertionSort([64, 34, 25, 12, 22, 11, 90]))
