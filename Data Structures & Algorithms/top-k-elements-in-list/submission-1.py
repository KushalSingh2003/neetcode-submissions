# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         appear = {}
#         for num in nums:
#             appear[num] = appear.get(num ,0)+1
#         temp_res = []
#         for key , value in appear.items():
#             temp_res.append([key , value])
#         temp_res.sort()

#         res = []
#         while len(res)<k:
#             res.append(temp_res.pop()[0])
#         return res
            
            
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
            
        