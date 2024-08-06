def bubble_sort(arr):
    """
    Sorts a list using the bubble sort algorithm.

    Bubble sort works by repeatedly stepping through the list, comparing each pair
    of adjacent items, and swapping them if they are in the wrong order. Each pass
    through the list moves the largest unsorted item to its correct position at the end.
    This process is repeated until the entire list is sorted.

    Key Points:
    - Simple and easy to understand.
    - Not very efficient for large lists.
    - Best for small or nearly sorted lists.

    Time Complexity:
    - Worst-case: O(n^2) - when the list is in reverse order.
    - Best-case: O(n) - when the list is already sorted.

    Parameters:
    arr (list): The list of items to be sorted.

    Returns:
    list: The sorted list.
    """
    
    n=len(arr)
    visited=True
    while visited:
        visited=False
        for i in range(1,n):
            if arr[i-1]>arr[i]:
                visited=True
                arr[i-1],arr[i]=arr[i],arr[i-1]
    return arr

list1=[5,-5,9,-4,45,-8,2,6]                
res=bubble_sort(list1)
print(res)
            
        