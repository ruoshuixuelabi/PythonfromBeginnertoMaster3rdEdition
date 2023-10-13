"""
除了通过task.result()方法来获取异步函数的返回值，还可以通过绑定回调函数的方式来获取。示例代码如下：
"""
import asyncio  # 导入asyncio模块


# 创建一个用于测试的协程任务的函数
async def test_task(a, b):
    return a + b


def callback(future):  # 定义的回调函数
    print('回调函数中的结果为:', future.result())


t = test_task(3, 2)  # 实例化测试的协程函数
loop = asyncio.new_event_loop()  # 创建事件循环
asyncio.set_event_loop(loop)  # 设置事件循环对象
task = loop.create_task(t)  # 创建协程任务
task.add_done_callback(callback)  # 绑定一个回调函数
loop.run_until_complete(task)  # 将协程注册到事件循环,然后启动事件循环
print('协程函数中的结果为：', task.result())  # 输出协程函数中的结果
