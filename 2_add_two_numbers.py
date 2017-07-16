"""You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0

        dummy = ListNode(-1)
        head = dummy

        while l1 or l2:
            if l1 and l2:
                dig_sum = l1.val + l2.val + carry
                head.next = ListNode(dig_sum % 10)
                head = head.next
                l1, l2 = l1.next, l2.next
                carry = dig_sum // 10
            elif l1:
                dig_sum = l1.val + carry
                head.next = ListNode(dig_sum % 10)
                head = head.next
                l1 = l1.next
                carry = dig_sum // 10
            elif l2:
                dig_sum = l2.val + carry
                head.next = ListNode(dig_sum % 10)
                l2 = l2.next
                head = head.next
                carry = dig_sum // 10
        if carry:
            head.next = ListNode(carry)
            head = head.next
        return dummy.next
