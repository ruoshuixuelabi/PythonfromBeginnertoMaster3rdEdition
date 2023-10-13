import asyncio  # 导入asyncio模块
import time  # 导入时间模块

"""
在实现使用协程执行多个耗时任务时,首先需要创建一个可以模拟耗时任务的协程函数,然后根据需求创建多个协程任务,
再将所有协程任务添加至列表中,最后运行多个协程任务的列表。具体代码如下：
"""


# 创建一个用于测试的协程任务的函数
async def test_task(a, b):
    result = a + b  # 计算传入值的结果
    await asyncio.sleep(result)  # 等待结果对应的时间,模拟耗时任务
    return "执行耗时任务：{}秒！".format(result)


start_time = time.time()  # 获取当前时间,记录程序开始时间
loop = asyncio.new_event_loop()  # 创建事件循环
asyncio.set_event_loop(loop)  # 设置事件循环对象
task1 = loop.create_task(test_task(0, 1))  # 创建协程任务1
task2 = loop.create_task(test_task(0, 2))  # 创建协程任务2
task3 = loop.create_task(test_task(0, 3))  # 创建协程任务3
# 创建多个协程任务的列表
tasks = [task1, task2, task3]
loop.run_until_complete(asyncio.wait(tasks))
for task in tasks:  # 遍历所有协程任务
    print(task.result())  # 输出每个任务结果
end_time = time.time()  # 获取当前时间,记录程序结束时间
print('程序实际执行时间为：', end_time - start_time, '秒！')
"""
程序运行结果如图14.23所示。
执行耗时任务：1秒！
执行耗时任务：2秒！
执行耗时任务：3秒！
程序实际执行时间为： 3.008784294128418 秒！

从图14.23所示的运行结果中可以看出,3个耗时任务分别为1秒、2秒、3秒,但整个程序实际的执行时间为3秒左右,确实提升了很大的运行效率。
"""