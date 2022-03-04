# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#
# 示例 1: 输入: s = "anagram", t = "nagaram" 输出: true
#
# 示例 2: 输入: s = "rat", t = "car" 输出: false
#
# 说明: 你可以假设字符串只包含小写字母。

def re_ab(s,t):
    res_map = {}
    res_map_2 = {}

    for i in s:
        if i in res_map.keys():
            res_map[i] +=1

        else:
            res_map[i] = 1

    for i in t:
        if i in res_map_2.keys():
            res_map_2[i] += 1

        else:
            res_map_2[i] = 1

    print(res_map,res_map_2)

    res = 0
    for i in res_map.keys():
        if res_map[i] != res_map_2[i]:
            res +=1

    for i in res_map_2.keys():
        if res_map[i] != res_map_2[i]:
            res += 1

    if res == 0:
        return True
    else:
        return False





print(re_ab("anagram","nagram"))
