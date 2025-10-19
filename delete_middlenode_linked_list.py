class Sol(object):
    def deleteMiddle(self, head):
        slow, fast = head, head
        prev = None

        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if prev is None:
            head = head.next
        else:
            prev.next = slow.next
        return head

        #T:O(n),S:O(1)