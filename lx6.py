#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#


def move(n, from_pz, to_pz):
	global i
	#print(i,n,from_pz,to_pz)
	print('第%d步,将%s号盘子%s到%s' % (i,n,from_pz,to_pz))
	i = i + 1
	
def hanoi(n,from_pz,denpend_on,to_pz):
	if (n == 1):
		move(1,from_pz,to_pz)
	else:
		hanoi(n-1,from_pz,to_pz,denpend_on)
		move(n,from_pz,to_pz)
		hanoi(n-1,from_pz,denpend_on,to_pz)		


i = 1		
hanoi(3,'A','B','C')

n = 2
print(i)
print('i=%d,n=%d' % (i, n))
print("i={0},n={1}".format(i, n))
