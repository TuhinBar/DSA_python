
# Defining a binary search Function
def binarySearch(arr,value):
    # Setting low and High value
    low=0
    # High value is last index of array e.g 6 (here)
    high=len((arr))-1
    #Starting the iteration
    while(low<=high):
        # Getting the mid of the array(if odd no of total index low mid value among two value e.g 3(here))
        mid=(low+high)//2
        # Checking the value is prensent in mid index of array or not and if present returning mid
        if(value==arr[mid]):
            return mid
            # Checking if the value is greater than mid (if yes checking the last half and setting the low to mid plus 1 index in every iteration)
        elif(value>arr[mid]):
            low=mid+1
        else:
            # Checking if the value is lower than mid (if yes checking the first half and setting the high to mid minus 1 index in every iteration)
            high=mid-1
            # returning messege if the value doesn't exist in the array
    return "Target do not exist in array"


# Driver code
arr=[1,2,3,4,5,6,7]
target=6
target2= 20
print("The index of target",target,"is:",binarySearch(arr,target))
print("The index of target",target2,"is:",binarySearch(arr,target2))