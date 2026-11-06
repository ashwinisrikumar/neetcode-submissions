class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for char in strs:
            count = [0] * 26
            for c in char:
                count[ord('a')-ord(c)]+=1
            res[tuple(count)].append(char)
        return list(res.values())
