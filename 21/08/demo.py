import numpy as np                # 导入numpy模块

a = np.array([[1,2,3],[4,5,6],[7,8,9]])   # 创建多维数组
print('数组a内容为：\n',a)                  # 打印数组a内容
print('指定索引结果：',a[1])                # 打印指定索引结果
print('指定索引范围的结果：\n',a[1:])        # 打印1行以后的元素
print('指定行列结果：',a[0,1:4])             # 打印第1行中第2、3列元素
print('获取第2列元素：',a[...,1])            # 打印第2列所有元素
print('获取第2行元素：',a[1,...])            # 打印第2行所有元素
print('获取第2列及以后的元素：\n',a[...,1:]) # 打印第2列及以后的元素
