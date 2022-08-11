"""
题意：反转一个单链表。
示例: 输入: 1->2->3->4->5->NULL 输出: 5->4->3->2->1->NULL
"""

class Node():
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def resver_link(l):
    # 生成一个遍历的游标
    cur = l
    # 生成一个存放当前游标下一个节点的指针
    tmp = Node()
    # 生成一个反转的指针
    prev = None

    while cur:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp

    return prev

