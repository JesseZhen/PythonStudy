#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('输入身高')
height = input()
height = float(height)
print('输入体重')
weight = input()
weight = float(weight)
bmi = (weight/height**2)  #**2表示2次方 如果为3则为3次方
if bmi<18.5:
    print('过轻')
elif 18.5<=bmi<25:
    print('正常')
elif 25<=bmi<28:
    print('过重')
elif 28<=bmi<32:
    print('肥胖')
elif bmi>=32:
    print('严重肥胖')
