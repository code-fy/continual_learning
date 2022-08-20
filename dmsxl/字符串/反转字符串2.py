"""
给定一个字符串 s 和一个整数 k，
你需要对从字符串开头算起的每隔 2k 个字符的前 k 个字符进行反转。
如果剩余字符少于 k 个，则将剩余字符全部反转。
如果剩余字符小于 2k 但大于或等于 k 个，
则反转前 k 个字符，其余字符保持原样。

"""


def resver_s(nums,k):

    l = len(nums)

    n = l // (2*k)


    for i in range(1,n+1):
        if n % 2 * k >= k or n % 2 * k <= 2 * k:
            cur = 2*k*i
            p = cur -2*k
            e = cur -k-1
            while p <= e:
                nums[p],nums[e] = nums[e],nums[p]

                e-=1
                p +=1

        # elif n % 2*k < k:
            if (l - (cur-1) )>= k and (l - cur )< 2*k:

                pp = l - (cur-1)
                ee = l -1

                # a = n % 2*k
                while pp <= ee:
                    nums[pp], nums[ee] = nums[ee] ,nums[pp]
                    pp+=1
                    ee-=1

    return nums


print(resver_s(["a","b","c","d","e","f"],2))





