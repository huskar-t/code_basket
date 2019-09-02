# encoding: utf-8
# 求解1+2+3+...+n,要求不能使用乘除法、while、for、if 、else、switch、case等关键字

# 短路运算+递归
n = 55
total = 0


def a_sum(s):
    s += 1
    global total
    total += s
    s ^ n and a_sum(s)


if __name__ == '__main__':
    a_sum(0)
    print(total)
