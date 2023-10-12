import math													# 导入Python的数学模块
# 以货币形式显示
print('1251+3950的结果是（以货币形式显示）：￥{:,.2f}元'.format(1251+3950)) 
print('{0:.1f}用科学记数法表示：{0:E}'.format(120000.1))					# 用科学记数法表示
print('π取5位小数点：{:.5f}'.format(math.pi))				# 输出小数点后5位
print('{0:d}的16进制结果是：{0:#x}'.format(100))			# 输出十六进制数
# 输出百分比，并且不带小数
print('天才是由 {:.0%} 的灵感，加上 {:.0%} 的汗水 。'.format(0.01,0.99))  