# 输入一行两个整数 a 和 b（保证 b != 0），输出它们的和、差、积，以及浮点数除法的结果。
a, b = map(int, input().split())
print(f"和：{a + b}")
print(f"差：{a - b}")
print(f"积：{a * b}")
print(f"商：{a / b}")

# 输入两个整数，使用 Python 的多变量赋值完成交换，然后输出交换后的两个整数。
print(f"交换之前：{a, b}")
a, b = b, a
print(f"交换之后：{a, b}")

# 输入学生姓名、年龄和成绩（分别占一行），使用 f-string 输出学生信息，成绩保留两位小数。
name = input()
age = int(input())
score = float(input())
print(f"姓名：{name}, 年龄：{age}, 成绩：{score:.2f}")
