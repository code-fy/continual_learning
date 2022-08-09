"""
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
示例 1： 输入：nums = [-4,-1,0,3,10] 输出：[0,1,9,16,100] 解释：平方后，数组变为 [16,1,0,9,100]，排序后，数组变为 [0,1,9,16,100]
示例 2： 输入：nums = [-7,-3,2,3,11] 输出：[4,9,9,49,121]
"""

def sorted_square(nums):
    res = sorted([i**2 for i in nums])
    return res

print(sorted_square([-4,-1,0,3,10]))

def sorted_squares(nums):

    res = [0]*len(nums)
    i,j,k = 0,len(nums)-1,len(nums)-1

    while i<=j:
        l = nums[i]**2
        r = nums[j]**2
        if l>r:
            res[k] = l
            i+=1
        else:
            res[k] = r
            j-=1

        k-=1

    return res

print(sorted_squares([-4,-1,0,3,10]))


