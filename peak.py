# Utility function
def find_peak_recursive(low, high, lst):
    """
    Finds a peak element
    :param low: Starting index of a given list
    :param high: Ending index of a given list
    :param lst: List of integers
    :return: Returns a peak element in a given list
    """
    # Finding the middle index
    middle = low + (high - low) // 2

    # If there are neighbours
    if (middle == len(lst) - 1 or lst[middle + 1] <= lst[middle]) and (middle == 0 or lst[middle - 1] <= lst[middle]):
        return middle

    # If left neighbour is greater, then peak element is in the left half
    elif (lst[middle - 1] > lst[middle]) and middle > 0:
        return find_peak_recursive(low, (middle - 1), lst)

    # If right neighbour is greater, then peak element is in the right half
    else:
        return find_peak_recursive((middle + 1), high, lst)


def find_peak(lst):
    """
    Finds a peak element
    :param lst: List of integers
    :return: Returns a peak element in a given list
    """
    return lst[find_peak_recursive(0, len(lst) - 1, lst)]

# Driver code to test above function
if __name__ == '__main__':

    # Example: 1
    lst = [7, 11, 22, 13, 4, 0]
    print('One peak point is: ', find_peak(lst))

    # Example: 2
    lst = [0, 3, 100, 2, -1, 0]
    print('One peak point is: ', find_peak(lst))

    # Example: 3
    lst = [6, 5, 4, 3, 2, 1]
    print('One peak point is: ', find_peak(lst))