﻿print("\n","="*10,"蚂蚁庄园动态","="*10)
file = open('message.txt','w')		# 创建或打开保存蚂蚁庄园动态信息的文件
# 写入一条动态信息
file.write("你消耗了50g饲料雇佣mingri的小鸡来生产肥料，记得喂食哦。\n")
print("\n 写入了一条动态……\n")
file.close()						# 关闭文件对象


'''以下为追加文件内容的代码

print("\n","="*10,"蚂蚁庄园动态","="*10)
file = open('message.txt','a')   # 创建或打开保存蚂蚁庄园动态信息的文件
# 追加一条动态信息
file.write("mingri的小鸡在你的庄园待了22分钟，吃了6g饲料之后，被你赶走了。\n")
print("\n 追加了一条动态……\n")
file.close()    # 关闭文件对象
'''
