def maxSubArray(nums):
        msf = -float('inf')
        subarray = []
        meh = 0
        s = 0
        for i in range(len(nums)):
            meh += nums[i]
            if meh > msf:
                subarray.clear()
                msf = meh
                subarray.append(s)
                subarray.append(i)
            if meh < 0:
                meh = 0
                s = i + 1
        return msf



if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    target = 8
    x = maxSubArray(nums)
    print(x)