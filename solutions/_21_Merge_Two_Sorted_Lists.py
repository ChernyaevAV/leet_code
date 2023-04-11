from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def mergeTwoLists(
                  list1: Optional[ListNode],
                  list2: Optional[ListNode]
                  ) -> Optional[ListNode]:

    cur_node = next_node = ListNode()

    while list1 and list2:
        if list1.val < list2.val:
            cur_node.next = list1
            list1, cur_node = list1.next, list1
        else:
            cur_node.next = list2
            list2, cur_node = list2.next, list2

    if list1 or list2:
        cur_node.next = list1 if list1 else list2
    return next_node.next

if __name__ == '__main__':
    list1 = ListNode(4, None)
    list1 = ListNode(2, list1)
    list1 = ListNode(1, list1)

    list2 = ListNode(4, None)
    list2 = ListNode(3, list2)
    list2 = ListNode(1, list2)

    res = mergeTwoLists(list1, list2)
    while res.next is not None:
        print(res.val, end=', ')
        res = res.next
