"""
In Quick Sort the process is to partition and then get the list with one element at it correct sorted place where
all elements to its left are lesser and to the right are greater to it.

Also once the partiotion is done we will recursively call the program to partition the list and sort

"""

def partitioning(arr,p,q):

    j = p  # Initialiaing the first pointer
    i = p-1
    pivot = q-1

    for j in range(p,q):

        if arr[j] <= arr[pivot]:
            i = i+1
            # Need to swap the values at i and j
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

            j = j+1

    return i  # Returns the position of the element which is at its correct position after the partition


def quick_sort(arr, p, r):

    if p < r:

        q = partitioning(arr,p,r)
        quick_sort(arr,p,q)
        quick_sort(arr,q+1,r)

    return arr


# user_input = [4,0,1,5,2,6]
user_input = [5,4,9,6,3,5]

print(quick_sort(user_input,0,len(user_input)))