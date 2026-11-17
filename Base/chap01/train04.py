# 编写函数 get_min_max(a, b, c)，接收三个整数，返回其中的最小值和最大值。
# 要求：使用 return 返回两个结果，可以使用 min()、max()。
from statistics import NormalDist
def get_min_max(a, b, c):
    return min(a, b, c), max(a, b, c)

# 编写函数 power(x, n=2)，计算 x 的 n 次方，默认计算平方。
# 要求：使用默认参数，函数必须有返回值。
def power(x, n=2):
    return x ** n

# 编写函数 calculate_sum(*args)，接收任意数量的数字，返回它们的总和。
# 要求：使用 *args 和循环。
def calculate_sum(*args):
    ans = 0
    for i in range(0, len(args)):
        ans += args[i]
    return ans

# 编写函数 add_element(x, nums=None)，向列表添加元素并返回列表。
# 如果调用者没有传入列表，则创建一个新列表。
# 要求：避免使用可变对象作为默认参数。
def add_element(x, nums=None):
    if(nums == None):
        nums = []
    nums.append(x)
    return nums

a, b = get_min_max(1, 4, 5)
print(a, b)
