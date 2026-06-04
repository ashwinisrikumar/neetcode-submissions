class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        l=0
        res=0
        max_f=0
        for r in range(len(s)):
            if s[r] not in count:
                count[s[r]]=0
            count[s[r]]+=1
            max_f = max(max_f,count[s[r]])

            while(r-l+1)-max_f>k:
                count[s[l]]-=1
                l+=1

            res = max(res,r-l+1)
        return res

        

        """
        
        freq_counter = {
        
        }
        if char not in freq_counter:
                freq_counter[char] = 1
        else
        freq_counter[char] += 1

        AABACA
        AABACB
        A = 2, B = 1, C = 1
        Step1 -   1 - 1 = 0< 1 -> valid
        Step2 -  2 - 2 = 0 < 1 -> valid
        Step3 - 3 - 2 = 1 == 1-> valid
        Step4 - 4 - 3 = 1 == 1 -> valid
        Step5 - 5 - 3 = 2 > 1 -> invalid
        Step 6 - 5 - 3 = 2> 1
        step 6 - 5 - 

        for right in range...
            freq_counter[char] += 1

        """


                
    