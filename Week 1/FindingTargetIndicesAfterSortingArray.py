x = len(nums) 
            a=[]
            for i in range(0,x):
                for j in range (0,x):
                    if j < x-1 and nums[j]>nums[j+1]:
                        c = nums[j+1]
                        nums[j+1]=nums[j]
                        nums[j]=c
            for i in range(0,x):
                if nums[i]==target :
                    a.append(i)    
            return a        
