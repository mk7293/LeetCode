class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if not l1:
            return l2
        elif not l2:
            return l1

        ret_list = ListNode(0)
        current = ret_list

        while l1 or l2:
            if not l1 and l2:
                current.next = ListNode(l2.val)
                l2 = l2.next
            elif not l2 and l1:
                current.next = ListNode(l1.val)
                l1 = l1.next
            elif l1.val < l2.val:
                current.next = ListNode(l1.val)
                l1 = l1.next
            elif l1.val > l2.val:
                current.next = ListNode(l2.val)
                l2 = l2.next
            else:
                current.next = ListNode(l1.val)
                current = current.next
                current.next = ListNode(l2.val)
                l1 = l1.next
                l2 = l2.next

            current = current.next

        return ret_list.next


    if __name__ == '__main__':
        mergeTwoLists()