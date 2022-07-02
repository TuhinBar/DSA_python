# Divide and Conquer

from array import array

# Defining the function
def merge_sort(arr):
    # Length checking and dividing the array like A=[p....r] => A=[p...q], A=[q+1...r]
    if len(arr)>1:
        mid= len(arr)//2
        left_side= arr[:mid]
        right_side= arr[mid:]
        # Dividing the array until it became p==r
        merge_sort(left_side)
        merge_sort(right_side)
        # Assigning iteration variables
        i=j=k=0
        # Comparing and sorting sub arrays and merging them in a new array K
        while i<len(left_side) and j<len(right_side):
            if left_side[i]< right_side[j]:
                arr[k]=left_side[i]
                i+=1
            else:
                arr[k]=right_side[j]
                j+=1
            k+=1
        # As the divisions may not be equal the remaining elemsnts should be inserted after the above part is done
        while i<len(left_side):
            arr[k]=left_side[i]
            i+=1
            k+=1

        while j< len(right_side):
            arr[k]=right_side[j]
            j+=1
            k+=1    
# Printing the sorted array
def print_list(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

# Driver code goes brrrr
arr=[576,1,4,5,3,2,6]
merge_sort(arr)

print('Sorted array is:')
print_list(arr)
