class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
         t = "abcc"
         countT = {a:1, b:1, c:2}

         s = "xzabcxyz"
         window = {X:1, Z:1, a: 1, b:1, c: 2}
        """
        
        if t == "":
            return ""
        countT, window = {},{}
        for c in t:
            countT[c]=1+countT.get(c,0)
        have,need = 0,len(countT)
        res, resLen = [-1,-1],float('infinity')
        l =0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)

            if c in countT and window[c]==countT[c]:
                have+=1
            while have == need:
                if (r-l+1)<resLen:
                    res = [l,r]
                    resLen = r-l+1
                window[s[l]]-=1
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if resLen!=float('infinity') else ""




        

        """
s = "OUZODYXAZV", t = "XYZ"

       need_counter = {X: 0, Y: 0, Z: 1}
       window - {X: 1, Y: 1, Z: 1}
       need_len = 3

       left = 0

       for right, char in enumeraet(s):
            if char in need_counter:
                need_counter[char] -= 1
                if need_counter[char] == 0:
                   need_len-= 1 

             while need_len == 0:
                window_size = right - left
                smallest_window = min(window_size, smallest_window)
                
                if counter[left] in t:
                    need_couter[left] += 1
                    need_len += 1
                left +=1

        """
