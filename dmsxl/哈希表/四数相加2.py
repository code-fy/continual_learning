"""
给定四个包含整数的数组列表 A , B , C , D ,
计算有多少个元组 (i, j, k, l) ，
使得 A[i] + B[j] + C[k] + D[l] = 0。
为了使问题简单化，
所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。
所有整数的范围在 -2^28 到 2^28 - 1 之间，
最终结果不会超过 2^31 - 1 。

"""

def four_sum_count(A,B,C,D):

    tmp = {}
    count = 0
    for n1 in A:
        for n2 in B:
            if n1+n2 in tmp:
                tmp[n1+n2] += 1
            else:
                tmp[n1+n2] = 1

    for n3 in C:
        for n4 in D:
            if -n3-n4 in tmp:
                count += tmp[-n3-n4]

    return count

print(four_sum_count([1,2],[-2,-1],[-1,2],[0,2]))


