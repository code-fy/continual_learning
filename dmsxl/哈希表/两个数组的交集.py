"""
题意：给定两个数组，编写一个函数来计算它们的交集。
"""

def intersection(nums1,num2):

    res = []
    if len(nums1) >= len(num2):
        for i in num2:
            if i in nums1:
                res.append(i)
    else:
        for i in nums1:
            if i in num2:
                res.append(i)

    return res

print(intersection([4,9,5],[9,4,9,8,4]))

