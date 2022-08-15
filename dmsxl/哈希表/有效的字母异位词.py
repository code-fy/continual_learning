"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1: 输入: s = "anagram", t = "nagaram" 输出: true

示例 2: 输入: s = "rat", t = "car" 输出: false

说明: 你可以假设字符串只包含小写字母。
"""

def isAnagram(s,t):
    if t in s:
        return True
    else:
        return False


print(isAnagram("anagram","anagram"))

def isAnagram1(s,t):
    record = {}
    for i in s:
        if i in record:
            record[i] += 1
        else:
            record[i] = 0


    for i in t:
        if i not in record.keys():
            return False
    else:
        return True

print(isAnagram1("anagram","anagrsm"))