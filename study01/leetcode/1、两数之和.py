class Solution:
    def twoSum(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            if target-nums[i] not in dict:
                dict[nums[i]] = i
            else:
                return[dict[target-nums[i]], i]


if __name__ == "__main__":
    a = Solution()
    print(a.twoSum([3, 5, 4, 8, 11, 9], 15))

