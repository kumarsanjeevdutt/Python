def insertion_sort(arr):
    """
    Sorts a list in ascending order using the insertion sort algorithm.
    
    Insertion sort is a simple comparison-based sorting algorithm. It works by iteratively
    building a sorted portion of the list by inserting each element from the unsorted portion
    into its correct position within the sorted portion.

    Parameters:
    arr (list): The list to be sorted.

    Returns:
    list: The sorted list.
    
    Time Complexity:
    - Worst-case: O(n^2) - when the list is in reverse order.
    - Best-case: O(n) - when the list is already sorted.


    Example:
    >>> insertion_sort([4, 3, 2, 1])
    [1, 2, 3, 4]
    """
    
    n=len(arr)
    for i in range (1,n):
        for j in range(i,0,-1):
            if arr[j-1] >arr[j]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
            else:
                break
    return arr        


list1=[-5,-3,8,-7,5,9,1,6,3,0]
res=insertion_sort(list1)
print(res)