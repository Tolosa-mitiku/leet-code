def selectionSort(arr,n):
    #code here
    minimum = 0
    for i in range(n):
        if arr[i] < arr[minimum]:
            minimum = i
    return minimum

def select(arr, i):
    # code here 
    for j in range(i):
        minimum = selectionSort(arr[j:], i-j)
        arr[j], arr[minimum + j] = arr[minimum + j], arr[j]
    return arr

print(select([4,1,3,9,7], 5))
