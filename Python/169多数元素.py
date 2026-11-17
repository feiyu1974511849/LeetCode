class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # 肯定存在多数元素，多数元素的个数大于⌊ n/2 ⌋
        # 可以使用打擂法，如果相等，生命加一，如果不相等，同归于尽

        # 生命值
        count = 0
        # 候选人，擂主
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate

    