class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        stack = [(root, 1)]
        max_depth = 0

        while stack:
            current_node, current_depth = stack.pop()

            if current_depth >= max_depth:
                max_depth = current_depth

            if current_node.left:
                stack.append((current_node.left, current_depth + 1))
            if current_node.right:
                stack.append((current_node.right, current_depth + 1))
        return max_depth

        #T:O(n), S:O(h)