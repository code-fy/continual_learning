# 题意：删除链表中等于给定值 val 的所有节点。
#
# 示例 1：
# 输入：head = [1,2,6,3,4,5,6], val = 6
# 输出：[1,2,3,4,5]
#
# 示例 2：
# 输入：head = [], val = 1
# 输出：[]
#
# 示例 3：
# 输入：head = [7,7,7,7], val = 7
# 输出：[]

class LinkNode(object):
    def __init__(self,next=None, val=0):
        self.next = next
        self.val = val


def delete_node(head,val):

    dummy_node = LinkNode(next=head)

    while(dummy_node != None):
        if(dummy_node.next.val) == val:
            dummy_node.next = dummy_node.next.next

        dummy_node = dummy_node.next

    return dummy_node.next
