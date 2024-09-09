def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def search():
    arr = [int(x) for x in input("Enter sorted numbers separated by spaces: ").split()]
    target = int(input("Enter the number to search for: "))
    
    index = binary_search(arr, target)
    
    if index != -1:
        print(f"Number found at index {index}.")
    else:
        print("Number not found.")

search()
