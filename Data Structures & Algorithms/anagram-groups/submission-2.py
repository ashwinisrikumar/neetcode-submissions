class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # cache = {}
        res = []

        """
        cache = {}
        for each word
          freq = [0] * 26
          for each letter in word
             freq[ord(letter) - ord('a')] += 1
          cache(tuple(freq)).append(word)

          a => 1
          b => 0
          c => 1
          .

          t => 1

        for each word
           cache[sorted(word)].append(word)
        for each key in cache
          res.append(cache[key])
        """
        cache = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            cache[sortedS].append(s)
        for key in cache:
            res.append(cache[key])
        return res

        

        
        

        