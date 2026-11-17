# 输入正整数 n，使用 for 循环计算 1～n（包含 n）之间所有偶数的和。
n = int(input())
ans = 0
for i in range(2, n + 1, 2):
    ans += i

# 输入一个非负整数 n，使用 while 循环将其数字顺序反转。输入：`12340`,输出：`4321`
# 123 12 3 * 100
# 12  1  2 * 10
# 1   0  1 * 1
# 321
n = int(input())
ans = 0

while n > 0:
    digit = n % 10
    ans = ans * 10 + digit
    n //= 10

print(ans)
# 输入正整数 n，找到 1～n 中第一个既能被 3 整除、又能被 5 整除的数字。如果不存在，输出 -1。
n3 = int(input())
for i in range(1, n3 + 1):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
        break
else:
    print(-1)

# 使用两层 for 循环输出九九乘法表。
# 1*1=1
# 1*2=2 2*2=4
# 1*3=3 2*3=6 3*3=9
# ...
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={j * i}", end=' ')
    print()