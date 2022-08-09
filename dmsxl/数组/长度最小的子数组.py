"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。
示例：
输入：s = 7, nums = [2,3,1,2,4,3] 输出：2 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
"""

def min_sub_arr_len(nums,tar):
    res = float("inf")
    Sum = 0
    index = 0

    for i in range(len(nums)):
        Sum += nums[i]
        while Sum >= tar:
            res = min(res,i-index+1)
            Sum -= nums[index]
            index += 1

    return 0 if res==float("inf") else res


print(min_sub_arr_len([2,3,1,2,4,3],7))

# def demo(nums,tar):
#     res = float("inf")
#     Sum = 0
#     index = 0
#
#     for i in range(len(nums)):
#         Sum += nums[i]
#         while Sum >= tar:
#             res = min(res,i-index+1)
#             Sum-=nums[index]
#             index += 1
#
#     return 0 if res == float("inf") else res
#
#
# print(demo([2,3,1,2,4,3],7))