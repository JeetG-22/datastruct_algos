arr = [-10, 3, 6, 8, 25, -35, -1]
arr.sort()

print(arr)

low = 0
high = len(arr) - 1

target = int(input("Number To Search For: "))

while(low < high):
    mid = int(high + low / 2)
    if(arr[mid] == target):
        print("Index:", mid)
        break
    elif(arr[mid] < target):
        low = mid + 1
    else:
        high = mid - 1

if(low > high):
    print("Index:", -1)