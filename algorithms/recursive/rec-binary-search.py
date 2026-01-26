def bin_search(nums, l, h, target):
    mid = (h+l) // 2
    if nums[mid] == target:
        return mid
    if l > h:
        return -1
    
    if nums[mid] < target:
        return bin_search(nums, mid + 1, h, target)
    else:
        return bin_search(nums,l, mid - 1, target)
    
arr = [-6, 3, 8, 2, -4, 8]
arr.sort()

print(bin_search(arr, 0 , len(arr) - 1, -6))