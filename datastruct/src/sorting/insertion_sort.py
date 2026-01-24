#Time: O(n^2)
#Space: O(1) 

#Pass through the array and compare the current element with the elements before it
def insertion_sort(arr):
    for i in range(len(arr)):
        j = i - 1
        #Keep going back until the current element is in the right position
        while j >= 0 and arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j -= 1
        
test_arr = [3,2,1,8, -2, 6]

insertion_sort(test_arr)

print(test_arr)