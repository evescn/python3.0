# -*- coding: utf-8 -*-

def is_palindrome(n):
    a = str(n)
    for (i =0; i < len(a) / 2; i++)
        if a[i] != a[len(a) - i]:
            break


# 测试:
output = filter(is_palindrome, range(1, 1000))
print(list(output))
