# 编写函数 analyze_number(n)，接收一个正整数 n，返回以下三个结果：
# 1. digit_sum：n 的各位数字之和。
# 2. reverse_num：将 n 的各位数字反转后得到的整数。
# 3. is_palindrome：判断 n 是否为回文数，返回 True 或 False。

def analyze_number(n):
    m = n
    digit_sum = 0
    reverse_num = 0
    is_palindrome = True
    temp = []
    
    while(n):
        # 计算各位数字之和
        temp = n % 10
        digit_sum += temp
        # 反转数字
        reverse_num = reverse_num * 10 + temp
        n //= 10
    is_palindrome = True if reverse_num == m else False
    return digit_sum, reverse_num, is_palindrome

if __name__ == '__main__':
    a,b,c = (analyze_number(1221))
    print(a, b, c)
    