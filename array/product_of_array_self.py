def productExceptSelf(nums):
        '''
        Example: 
        [ 1, 2,3,4]
        [ /, 1,2,6] Prefix
        [24,12,4,/] Suffix
        [24,12,8,6] Total
        '''
        products = [1] * (len(nums))
        
        # Prefix Loop
        prefix = 1
        for i in range(len(nums)):
            products[i] = prefix
            prefix = prefix * nums[i]

        # Postfix Loop
        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            products[i] = suffix * products[i]
            suffix = suffix * nums[i]
   
        return products


if __name__ == "__main__":
    res1 = productExceptSelf([1,2,3,4]) 
    print(res1) # [24,12,8,6]
    res2 = productExceptSelf([-1,1,0,-3,3]) 
    print(res2) # [0,0,9,0,0]
