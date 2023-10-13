import asyncio  # 导入asyncio模块
import time  # 导入时间模块

"""
使用协程执行多个耗时任务时,还可以使用协程嵌套与列表推导式的方法来简化代码。
首先需要将协程函数中的 return 换成 print,然后创建一个名称为 main 的协程函数,
在该函数中通过列表推导式创建多个协程任务的列表并通过 asyncio.wait 方式挂起协程。简化后的代码如下：
"""


# 创建一个用于测试的协程任务的函数
async def test_task(a, b):
    result = a + b  # 计算传入值的结果
    await asyncio.sleep(result)  # 等待结果对应的时间,模拟耗时任务
    print("执行耗时任务：{}秒！".format(result))


async def main(loops):
    # 创建多个协程任务的列表
    tasks = [loops.create_task(test_task(0, i)) for i in range(1, 4)]
    await asyncio.wait(tasks)  # 挂起协程任务


start_time = time.time()  # 获取当前时间,记录程序开始时间
loop = asyncio.new_event_loop()  # 创建事件循环
asyncio.set_event_loop(loop)  # 设置事件循环对象
loop.run_until_complete(main(loop))  # 运行所有协程任务
end_time = time.time()  # 获取当前时间,记录程序结束时间
print('程序实际执行时间为：', end_time - start_time, '秒！')
