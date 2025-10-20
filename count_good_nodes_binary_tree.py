class Solution(object):
    def goodNodes(self, root):
        if not root:
            return 0

        good = 0
        stack = [(root, root.val)]  # (node, max_so_far)

        while stack:
            node, max_so_far = stack.pop()

            if node.val >= max_so_far:
                good += 1

            new_max = max(max_so_far, node.val)

            if node.left:
                stack.append((node.left, new_max))
            if node.right:
                stack.append((node.right, new_max))

        return good

        #T:O(N), S:O(H)