def two_sum(nums, target):
    counter = {}
    for i in range(len(nums)):
        res = target - nums[i]
        if res in counter:
            return [counter[res], i]
        counter[nums[i]] = i


if __name__ == "__main__":
    res1 = two_sum([2,7,11,15], 9) 
    print(res1) # [0,1]
    res2 = two_sum([3,2,4],6) 
    print(res2) # [1,2]
    res3 = two_sum([3,3],6) 
    print(res3) # [0,1]
