"""
题意：给定一个包含 n 个整数的数组 nums 和一个目标值 target，
判断 nums 中是否存在四个元素 a，b，c 和 d ，
使得 a + b + c + d 的值与 target 相等？
找出所有满足条件且不重复的四元组。
"""

def four_sum(nums,tar):
    res = []

    nums.sort()

    n = len(nums)
    for i in range(n):
        s = i+1
        f = n-1
        if s <n:
            t_sum = nums[i] + nums[s] + nums[f]
            y = tar - t_sum
            for idx,k in enumerate(nums):
                if y == k:
                    t_l = [nums[i], nums[s], nums[f],nums[idx]]
                    res.append(t_l)

    return res

print(four_sum([1, 0, -1, 0, -2, 2],0))

def four_sum_res(nums,tar):
    nums.sort()
    n = len(nums)
    res= []
    for i in range(n):
        if i >0 and nums[i] == nums[i-1]:continue
        for k in range(i+1,n):
            if k>i+1 and nums[k] == nums[k-1]:continue
            p = k+1
            q = n-1

            while p < q:
                if nums[i] + nums[k] + nums[p] +nums[q] > tar:q -= 1
                elif nums[i] + nums[k] + nums[p] +nums[q] < tar:p += 1
                else:
                    res.append([nums[i], nums[k], nums[p],nums[q]])
                    while p<q and nums[p] == nums[p+1]:p+=1
                    while p<q and nums[q] == nums[q-1]:q-=1

                    p+=1
                    q-=1
    return res
print(four_sum_res([1, 0, -1, 0, -2, 2],0))
