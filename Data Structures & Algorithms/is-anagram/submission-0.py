class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        appear = {}
        for c in s:
            appear[c]=appear.get(c,0)+1
        
        for c in t:
            appear[c]=appear.get(c,0)-1
        print(appear)
            # print(appear)
        for key , pair in appear.items():
            if pair!=0:
                return False
        return True
        


        