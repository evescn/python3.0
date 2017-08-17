#!/usr/bin/env python3
# -*- coding:utf-8 -*-

string = 'Input your password :'
'''string = 'Input your password '(Only three times chance):'''
i = 3
username = 'root'
password = 'rootgm'
while i != 0:
    input_user = input('your name :')
    input_passwd = input(string)
    '''print(i)'''
    if input_passwd == password and input_user == username:
        print('your passwd is ok!')
        break
    elif i >= 1:
        print('your name or password is error!')
    i -= 1

