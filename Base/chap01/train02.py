
# 输入一个年份 year，判断它是否为闰年。
year = int(input())
ans = "yes" if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) else "no"
print(ans)
# 输入一行三个整数 a b c，使用 if-elif-else 判断并输出最大值。
a, b, c = map(int, input().split())
if a >= b and a >= c:
    ans = a
elif b >= a and b >= c:
    ans = b
else:
    ans = c
print(ans)

# 输入一行两个整数 a b，第二行输入运算符 op（+、-、*、/ 中的一个）。根据运算符输出结果。如果是除法且除数为零，输出 ERROR。
x, y = map(int, input().split())
op = input()
if op == '+':
    print(x + y)
elif op == '-':
    print(x - y)
elif op == '*':
    print(x * y)
elif op == '/':
    if y == 0:
        print("ERROR")
    else:
        print(x / y)
else:
    print("ERROR")
