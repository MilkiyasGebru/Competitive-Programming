    def select(self, arr, i):
        # code here 
        
        b=arr[i]
        for j in range(i,len(arr)):
            if j<len(arr)-1 and b>=arr[j+1]:
                b=arr[j+1]
                k=j+1
        return b         
    def selectionSort(self, arr,n):
        arr.sort()
      
