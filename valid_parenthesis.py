class Solution():
    def is_valid(self, s:str) -> bool:
        mapping = {")":"(", "]":"[", "}":"{"}
        stack = []

        for c in s:
            if c in mapping:
                if stack and stack[-1] == mapping[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack
#T:O(n), S:O(n)