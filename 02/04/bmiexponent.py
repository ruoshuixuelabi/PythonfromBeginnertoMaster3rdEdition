# -*- coding:utf-8 -*-

'''
   @ 功能：根据身高、体重计算BMI指数
   @ author:无语
   @ create:2018-3-30

'''

height = float(input("请输入您的身高（单位为m）："))	# 输入身高，单位为m
weight = float(input("请输入您的体重（单位为kg）："))	# 输入体重，单位为kg
bmi=weight/(height*height)					 # 用于计算BMI指数，公式为“体重/（身高×身高）”
print("您的BMI指数为："+str(bmi))					# 输出BMI指数
# 判断体重是否合理
if bmi<18.5:
    print("您的体重过轻 ~@_@~")
if bmi>=18.5 and bmi<24.9:
    print("正常范围，注意保持 (-_-)")
if bmi>=24.9 and bmi<29.9:
    print("您的体重过重 ~@_@~")
if bmi>=29.9:
    print("肥胖 ^@_@^")

