class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = { ')': '(', '}': '{', ']': '[' }
        stack = []
        for char in s:
            if char not in hashmap:
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    top_element = stack.pop()
                    if hashmap[char] != top_element:
                        return False
        return not stack

