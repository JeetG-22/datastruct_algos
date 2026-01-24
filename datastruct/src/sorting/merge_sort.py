#Time: O(nlogn)
#Space: O(n)
def merge_sort(arr, s, e):
    if e - s + 1 <= 1: #until there is one element in the array
        return arr
    
    m = (e + s) // 2 #midpoint needed to split the array
    
    merge_sort(arr, s, m) #left branch
    merge_sort(arr, m + 1, e) #right branch

    merge(arr, s, m, e) #called after array is broken down such that there is only one element

def merge(arr, s, m, e):
    L = arr[s:m+1] #left branch array
    R = arr[m+1: e+1] #right branch array

    #triple pointer system
    i = 0
    j = 0
    k = s #used to track how the elements are going to be placed in the merge array
    
    while i < len(L) and j < len(R):
        if L[i] <= R[j]: #le is needed for keeping the sort stable (reletive position of elements is maintained in the case of the same value)
            arr[k] = L[i]
            i += 1
            k += 1
        else: 
            arr[k] = R[j]
            j += 1
            k += 1
   
    #if there is anything leftover in the subarrays after comparing the left and right branches
    while i < len(L):
        arr[k] = L[i] 
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j] 
        j += 1
        k += 1

test_arr = [3,2,1,8, -2, 6]

merge_sort(test_arr, 0, len(test_arr)-1)

print(test_arr)
