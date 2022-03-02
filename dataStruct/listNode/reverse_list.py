# 题意：反转一个单链表。

# 示例: 输入: 1->2->3->4->5->NULL 输出: 5->4->3->2->1->NULL

class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


def resverse_list_node(head):
    pre = None
    cur = head

    while(cur!=None):
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp

    return pre