class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for ch in strs:
            sorted_ch = ''.join(sorted(ch))
            if sorted_ch not in result:
                result[sorted_ch]=[]
            result[sorted_ch].append(ch)
        return list(result.values())



        