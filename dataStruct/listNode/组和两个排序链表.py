# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
# 输入：l1 = [10,20,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]

class LinkNode():
    def __init__(self,next=None, val=0):
        self.next = next
        self.val =val


def com_a_b(l1,l2):
    tmp = LinkNode()

    if l1 == None:
        return l2
    if l2 == None:
        return l1

    while(l1 and l2):
        if l1.val <= l2.val:
            tmp.next = l1.next
            l1 = l1.next

        else:
            tmp.next = l2.next
            l2 = l2.next

        temp = tmp.next

    if l1:
        tmp.next = l1

    if l2:
        tmp.next = l2

    return tmp




