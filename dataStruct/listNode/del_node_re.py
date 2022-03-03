class LinkNode(object):
    def __init__(self,next=None,val=0):
        self.next = next
        self.val = val



def del_no_node(head,n):

    dummy_head = LinkNode(next=head)

    slow ,fast = dummy_head, dummy_head

    while(n != 0):
        fast = fast.next
        n-=1

    while(fast != None):
        slow =slow.next
        fast = fast.next

    slow.next = slow.next.next

    return dummy_head

