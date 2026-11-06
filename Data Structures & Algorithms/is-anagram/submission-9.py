class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        char_count = [0]* 26
        for i in range(len(s)):
            char_count[ord('a')-ord(s[i])]+=1
        for i in range(len(t)):
            char_count[ord('a')-ord(t[i])]-=1
        for value in char_count:
            if value !=0:
                return False
        return True