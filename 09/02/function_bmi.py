def fun_bmi(person,height,weight):
    '''功能：根据身高和体重计算BMI指数
       person：姓名
       height：身高，单位：m
       weight：体重，单位：kg
    '''
    print(person + "的身高：" + str(height) + "m \t 体重：" + str(weight) + "kg")
    bmi=weight/(height*height)					# 用于计算BMI指数，公式为“体重/（身高×身高）”
    print(person + "的BMI指数为："+str(bmi))		# 输出BMI指数
    # 判断体重是否合理
    if bmi<18.5:
        print("您的体重过轻 ~@_@~\n")
    if bmi>=18.5 and bmi<24.9:
        print("正常范围，注意保持 (-_-)\n")
    if bmi>=24.9 and bmi<29.9:
        print("您的体重过重 ~@_@~\n")
    if bmi>=29.9:
        print("肥胖 ^@_@^\n")
#*****************************调用函数***********************************#
fun_bmi("路人甲",1.83,60)						# 计算路人甲的BMI指数
fun_bmi("路人乙",1.60,50)						# 计算路人乙的BMI指数
