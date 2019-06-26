import time


# This is the bubble sort example with time complexity of O(n*n) [I mean O (n square)]
"""
Time Complexity:
Best : Omega(n*n)
Worst : O(n*n)
Average : Theta(n*n)

"""
def sort_1(arr,n):
    start = time.time()
    for i in range(0,n-1):

        for j in range (0,n-1):
            if arr[j+1] < arr[j]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    print("--- %s seconds ---" % (time.time() - start))
    return arr

# We will try to optimise the program to reduce the time complexity
"""
As we are aware that in bubble sort after every pass, the last element is the biggest element (in case of increasing 
order) hence we can reduce the number of time the second for loop executes. We need to understand that after every pass,
the list has last element at correct place, so no need to take it into account
After Pass 1 : List is (n-1) sorted
After Pass2 : List is (n-2) sorted
After Pass 3 : List is (n-3) sorted
.
.
.
.
After Pass K : List is (n-K) sorted

Hence we can formulate it as that the second loop will depend on the first loop for the subtraction from n

Time Complexity:
Best : Omega(n*n)
Worst : O(n*n)
Average : Theta(n*n)

The Complexity still remains the same , we need to furhter improve
"""


def sort_2(arr,n):

    for i in range(0,n-1):

        for j in range(0,(n-1)-i):
            if arr[j+1] < arr[j]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

# As now we optimized the program futher to get better complexities

"""
Now we can include the case where the elements get sorted even before completing all the passes
In that case there is no need to keep on performing the passes as the data is already sorted

For this we will use a flag whose value is by default 1 , which says its not soretd and the moment the value of flag 
becomes 0, we are sure that the list is sorted an we do not need to further sort the list

Time Complexity:
Best : Omega(n)  [Already Sorted List] = Only the inner loop will run n times and outer loop for only 1 time
Worst : O(n*n)   [Not a sorted List ] =  Both loops will run n times
Average : Theta(n*n)  [We need to consider all cases]

Like:
1,2,3,4,5 = Runs n times
2,1,3,4,5 = Runs 2n times
3,2,1,4,5 = Runs 3n times
4,3,2,1,5 = Runs 4n times
5,4,3,2,1 = Runs 5n times

hence it will sun ........ n*n times
We need to take average of all cases
So taking average:
n + 2n+ 3n + 4n + 5n + ....... +nxn/n
n(1+2+3+4+5.......+n)/n
n(n+1)/2
= n*n =O(n*n)


"""


def sort_3(arr,n):
    flag = 1
    for i in range(0,n-1):  # Here we assure that the passes only happen if flag is 1
        if flag == 1:
            for j in range(0,(n-1)-i):
                flag = 0                       # Here we keep the flag as 0 , so that it shows that the list is sorted
                if arr[j+1] < arr[j]:
                    flag = 1                    # Only change the flag to 1 if there is a swap , which means data is still not sorted and more passes need to happen
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
        else:
            break
    return arr


user_input = [1,4,0,3,9,6,2]
print(sort_3(user_input,len(user_input)))
