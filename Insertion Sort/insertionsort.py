def insertion_sort(arr, n):

    for i in range(0,n-1):
        temp = arr[i+1]
        j = i
        while j >= 0 and arr[j] > temp:
            arr[j+1] = arr[j]
            j = j-1

        arr[j+1] = temp

    return arr


user_input = [4,0,1,5,2,6]
print(insertion_sort(user_input,len(user_input)))

"""
Time Complexity:
Best : omega(n) [Completely sorted array] this will make the for loop run only not the while loop
Worst : O(n*n) [Both loops will run n times]
Average : O(n*n) [Since all cases will be considered and hence n square will be average]
"""