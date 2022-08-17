"""
给你一个包含 n 个整数的数组 nums，
判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？
请你找出所有满足条件且不重复的三元组。

注意： 答案中不可以包含重复的三元组。

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为： [ [-1, 0, 1], [-1, -1, 2] ]

"""

# def three_sum(nums):
#     l = len(nums)
#     res = []
#     for i in range(1,l):
#         s = 0
#         f = i+1
#         if f<= l-1 and  nums[i] +nums[s] + nums[f] == 0:
#             tmp = [nums[i],nums[s],nums[f]]
#             res.append(tmp)
#
#     return res
def three_sum(nums):
    ans = []
    n = len(nums)
    nums.sort()
    for i in range(n):
        left = i+1
        right = n-1
        if nums[i]>0:
            break
        if i >= 1 and nums[i] == nums[i-1]:
            continue
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total <0:
                left += 1
            elif total >0:
                right -=1
            else:
                ans.append([nums[i],nums[left],nums[right]])
                while left != right and nums[left] == nums[left +1]:left +=1
                while left != right and nums[right] == nums[right -1]:right -=1
                left += 1
                right-=1

    return ans


print(three_sum([-1, 0, 1, -3, -1, 4]))

