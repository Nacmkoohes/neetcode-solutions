class Solution:
    def isValid(self, s: str) -> bool:
        hashmap={')':'(','}':'{',']':'['}
        stack=[]
        for char in s:
            if char not in hashmap:
#means that it is an opening character
                stack.append(char)
            else:
#it is a closing character
                if not stack:
                    return False
                else:
                    top_element=stack.pop()
                    if hashmap[char]!= top_element:
                        return False
        return not stack

