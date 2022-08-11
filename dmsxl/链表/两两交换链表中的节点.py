"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换
"""
from .反转链表 import Node

def swapPairs(head):

    # 生成一个虚拟的头节点
    dumy = Node(next=head)
    # 生成游标
    cur = dumy

    while cur.next and cur.next.next:
        # 生成存储的临时节点
        tmp = cur.next
        # 生成存储的临时节点1
        tmp1 = cur.next.next.next

        # 第一步
        cur.next = cur.next.next
        # 第二步
        cur.next.next = tmp
        # 第三步
        tmp.next = tmp1

        cur = cur.next.next
    return dumy.next





