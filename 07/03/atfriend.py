"""
在IDLE中创建一个名称为atfriend.py的文件,然后在该文件中定义一个字符串,
内容为"@明日科技　@扎克伯格　@盖茨",接着使用split()方法对该字符串进行分割,以获取出好友名称,最后输出被@的好友,代码如下：
"""
str1 = '@明日科技 @扎克伯格 @盖茨'
list1 = str1.split(' ')							# 用空格分割字符串
print('您@的好友有：')
for item in list1:
    print(item[1:])							# 输出每个好友名时,去掉@符号
