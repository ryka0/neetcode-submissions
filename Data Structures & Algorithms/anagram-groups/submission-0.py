class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            letterCount = [0]*26
            for char in word:
                letterCount[ord(char) - ord("a")] += 1
            res[tuple(letterCount)].append(word)
        
        return list(res.values())

