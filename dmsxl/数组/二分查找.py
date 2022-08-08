"""
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，
写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
"""

def binary_search(nums,tar):
    l = 0
    r = len(nums)-1

    while l<=r:
        mid = l+(r-l) // 2
        if nums[mid] > tar:
            r = mid-1
        if nums[mid] < tar:
            l = mid+1
        if nums[mid] == tar:
            return mid

    return -1

# print(binary_search([1,2,4,5],3))

"""给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。
"""
def binary_search_1(nums,tar):
    l = 0
    r = len(nums)-1

    while l<=r:
        mid = l + (r - l) // 2
        if tar > nums[-1]:
            return r+1

        if nums[mid] > tar:
            r = mid -1
        if nums[mid] < tar:
            l = mid +1
        if nums[mid] == tar:
            return mid

    return l


# print(binary_search_1([1,2,4,5],9))

"""
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。
请你找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
"""

# print(binary_search_2([1,2,5,5,5,5,6,7,8,8],8))
def get_right(nums,tar):
    tmp = -2
    l = 0
    r = len(nums) -1
    while l <= r:
        mid = l+(r-l) // 2
        if nums[mid] > tar:
            r = mid -1
        else:
            l = mid + 1
            tmp = l

    return tmp

def get_left(nums,tar):
    tmp = -2
    l =0
    r = len(nums) -1
    while l <= r:
        mid = l + (r-l) // 2
        if nums[mid] >= tar:
            r = mid - 1
            tmp = r
        else:
            l = mid +1

    return tmp

def binary_search_2(nums,tar):

    l = get_left(nums,tar)
    r = get_right(nums,tar)

    if l ==-2 and r == -2:
        return [-1,-1]

    if r-l > 1:
        return [l+1,r-1]

    return [-1,-1]

# print(binary_search_2([1,2,5,5],5))
