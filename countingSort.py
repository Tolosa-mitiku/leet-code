def countingSort(arr):
    # Write your code here
    list = [0] * 100
    for i in arr:
        list[i] +=1
    return list