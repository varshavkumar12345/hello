import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        try:
            l=re.findall(p,s)
            if l!=[] and l[0]==s:
                return True
            return False
        except error:
            for i in s:
                if i not in p:
                    return False
            return True
