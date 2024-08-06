def selection_sort(arr):
    """
    Sorts a list in ascending order using the selection sort algorithm.

    Selection sort works by repeatedly finding the minimum element from the unsorted portion
    of the list and moving it to the beginning.

    Parameters:
    arr (list): The list of elements to be sorted.

    Returns:
    list: The sorted list.

    Time Complexity:
    - Average and Worst-case: O(n^2)
    - Best-case: O(n^2)

    Example:
    >>> selection_sort([64, 25, 12, 22, 11])
    [11, 12, 22, 25, 64]
    """
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range (i+1, n):
            if arr[j]<arr[min_index]:
                min_index=j                
        arr[i],arr[min_index]=arr[min_index],arr[i] 
    
    return arr

list1=[-3,4,-6,-1,-10,0,77]
res=selection_sort(list1)
print(res)