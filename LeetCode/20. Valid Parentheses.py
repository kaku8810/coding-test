class Solution:
    def isValid(self, s: str) -> bool:
        while len(s) > 0:
            length = len(s)
            s = s.replace("()", "").replace("{}", "").replace("[]", "")
            if len(s) == length:
                return False
        return True
