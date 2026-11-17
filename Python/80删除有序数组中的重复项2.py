class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # 通过栈来控制元素的个数，如果当前元素等于栈顶下方的元素，说明元素的个数超过了2个，不能入栈

        # 前两个元素默认保留
        stack_size = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[stack_size - 2]:
                nums[stack_size] = nums[i]
                stack_size += 1
        return min(stack_size, len(nums))