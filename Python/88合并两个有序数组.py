class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1
        tail = m + n - 1

        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1
            tail -= 1
        

if __name__ == '__main__':
    # 准备示例 1 的测试数据
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    
    # 实例化 Solution 并调用方法
    sol = Solution()
    sol.merge(nums1, m, nums2, n)
    
    # 打印结果验证
    print(f"合并后的数组结果: {nums1}")