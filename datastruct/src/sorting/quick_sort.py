def quick_sort(arr, s, e):
    #base case
    if e - s + 1 <= 1:
       return arr 
    

    pivot = arr[e] #assuming we choose the last element to be the pivot
    left = s
   
    #logic is to partition the array such that all elements smaller than the pivot are to the left and all elements greater are to the right 
    for i in range(s, e):
        if arr[i] < pivot:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1
        
    arr[e], arr[left] = arr[left], arr[e] #when it gets to the end swap the pivot with the position of left
    
    quick_sort(arr, s, left - 1) #left side 
    quick_sort(arr, left + 1, e) #right side

    return arr

test_arr = [3,2,1,8, -2, 6]

quick_sort(test_arr, 0, len(test_arr)-1)

print(test_arr)