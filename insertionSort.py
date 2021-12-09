def insertionSort1(n, arr):
    # Write your code here
        # Write your code here
    num = arr[n-1]
    for i in range(n-1, -1, -1):
        if arr[i-1] == arr[n-1]:
            arr[i] = num
        elif arr[i-1] > num:
            arr[i] = arr[i-1]
        else:
            arr[i] = num
            print(*arr)
            break
        print(*arr)   