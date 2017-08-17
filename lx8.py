# -*- coding: utf-8 -*-

def normalize(str):
	return str.capitalize()

# 测试:
L1 = ['adam', 'LISA', 'barT', 'ROOT']
L2 = list(map(normalize, L1))
print(L2)