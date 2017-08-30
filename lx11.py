# -*- coding: utf-8 -*-

def is_palindrome(n):
    l = len(str(n))
    i = 1
    while i <= int(l / 2):
        n_left = int(n / (10 ** (l - i)))
        n_right = n % 10
        n = int(n / 10)
        i += 1
        if n_left != n_right:
            return False
    else:
        return True


# 测试:
output = filter(is_palindrome, range(1, 1000))
print(list(output))
