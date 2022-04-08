class Solution:
    @staticmethod
    def topKFrequent(nums, k: int):
        dictN = {}
        for i in set(nums):
            dictN[i] = 0 
        for i in nums:
            dictN[i] += 1
        dictN = dict(sorted(dictN.items(), key=lambda item: item[1], reverse=True))
        print(dictN)
        ll = []
        # 词典操作
        for key, value in dictN.items():
            ll.append(key)
            k -= 1
            if k == 0:
                break
        return ll


print(Solution().topKFrequent([1,1,1,2,2,3], 2))