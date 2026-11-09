#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int p1 = m - 1;        // 指向 nums1 有效元素的末尾
        int p2 = n - 1;        // 指向 nums2 的末尾
        int tail = m + n - 1;  // 指向合并后 nums1 的最末尾

        // 只要 nums2 还有元素没放进去，就继续从后往前比大小
        while (p2 >= 0) {
            if (p1 >= 0 && nums1[p1] > nums2[p2]) {
                nums1[tail] = nums1[p1];
                p1--;
            } else {
                nums1[tail] = nums2[p2];
                p2--;
            }
            tail--;
        }
    }
};

int main() {
    // 准备示例 1 的测试数据
    vector<int> nums1 = {1, 2, 3, 0, 0, 0};
    int m = 3;
    vector<int> nums2 = {2, 5, 6};
    int n = 3;

    // 创建 Solution 对象并调用 merge 函数
    Solution sol;
    sol.merge(nums1, m, nums2, n);

    // 打印合并后的 nums1 验证结果
    cout << "合并后的数组结果: [ ";
    for (int num : nums1) {
        cout << num << " ";
    }
    cout << "]" << endl;

    return 0;
}