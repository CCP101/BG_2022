class Solution:
    def minSubArrayLen(self, target, nums) -> int:
        # 常规写法
        # slow = 0
        # length = float("inf") #考虑极端情况
        # FLAG = False
        # while(slow <= len(nums)):
        #     sum = 0
        #     for num in range(slow, len(nums)):
        #         sum += nums[num]
        #         if sum >= target:
        #             if num-slow <= length:
        #                 FLAG = True
        #                 length = num-slow+1
        #                 break
        #     slow += 1
        # if FLAG:
        #     return length
        # else:
        #     return 0

        # 滑动窗口
        res = float("inf")
        Sum = 0
        index = 0
        for i in range(len(nums)):
            Sum += nums[i]
            print(str(Sum)+"XXXX")
            while Sum >= target:
                res = min(res, i-index+1)
                Sum -= nums[index]
                index += 1
        return 0 if res==float("inf") else res

print(Solution().minSubArrayLen(7,[2,3,4,3,1,2]))
