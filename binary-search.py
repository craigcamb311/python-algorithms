"""
Binary Search Algorithm "Divide and Conquer"
"""

def binary_search(lst, high, low, x):
    if high >= low:
        mid = (high + low) // 2
        if lst[mid] == x:
            return mid
        elif lst[mid] > x:
            return binary_search(lst, mid - 1, low, x)
        else:
            return binary_search(lst, high, mid + 1, x)
    else:
        return -1 
        
    
lst = [2, 3, 4, 8, 16, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100]

#target_number = 40
target_number = 33

if binary_search(lst, len(lst) - 1, 0, target_number) != -1:
    print(f"Element {target_number} is present at index", str(binary_search(arr, len(arr) - 1, 0, target_number)))
else:
    print(f"Element {target_number} is not present in list")


