def countingSort(arr):
    # Write your code here
    x= len(arr)
    y=[0]*100
    for var in range(0,x,1):
        y[arr[var]] = y[arr[var]]+1
    return y   
