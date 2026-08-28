class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_str_count(s):
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            return tuple(count)
        
        counts = {}
        for wrd in strs:
            wrd_count = get_str_count(wrd)
            counts[wrd_count] = counts.get(wrd_count, []) + [wrd]
        return list(counts.values())
        