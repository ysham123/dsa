class Solution(object):
    def pairSum(self, head):
        check = []
        if head is None:
            return
        current_node = head
        while current_node is not None:
            check.append(current_node.val)
            current_node = current_node.next
        n = len(check)
        max_twin_sum = 0
        for x in range(n//2):
            twin_sum = check[x] + check[n-1-x]
            max_twin_sum = max(max_twin_sum, twin_sum)
        return max_twin_sum

        
        #T:O(n), S:O(1)