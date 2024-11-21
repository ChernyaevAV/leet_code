# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if self.next:
            return f"{str(self.val)}" + f"{str(self.next)}"
        return f"{str(self.val)}"


def convert_number_to_node(num: str) -> ListNode | None:
    if num is None:
        return None
    num = int(num[::-1])
    head = ListNode(int(num) % 10)
    pointer = head
    num //= 10
    while num > 0:
        pointer.next = ListNode(num % 10)
        num //= 10
        pointer = pointer.next
    return head


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        pointer = result

        while True:
            pointer.val += (l1 and l1.val or 0) + (l2 and l2.val or 0)

            if l1: l1 = l1.next
            if l2: l2 = l2.next

            if pointer.val >= 10:
                pointer.next = ListNode(1)
            elif l1 or l2:
                pointer.next = ListNode(0)

            pointer.val = pointer.val % 10

            if not l1 and not l2:
                return result
            else:
                pointer = pointer.next


if __name__ == '__main__':
    # l1 = convert_number_to_node("123")
    # l2 = convert_number_to_node("457")

    # l1 = ListNode(1)
    # l1.next = ListNode(2)
    # l1.next.next = ListNode(3)
    #
    # l2 = ListNode(4)
    # l2.next = ListNode(5)
    # l2.next.next = ListNode(7)

    # print(Solution().addTwoNumbers(l1, l2))

    a = [5, 6, 7]
    b = [3, 4]
    a = int(''.join(map(str, a)))  # 567
    b = int(''.join(map(str, b)))  # 34
    c = a + b  # 601
    res = list(map(int, str(c)))
    print(res)  # [6, 0, 1]

