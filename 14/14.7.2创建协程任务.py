"""
14.7 异步编程asyncio模块

我们如果要执行上千个任务,则可以创建上千个线程,但这样会消耗不可估量的内存。
于是,业界尝试创建较小数量的线程并以较小的并发性来执行任务。
在传统的同步线程代码中,内核必须检测线程何时被IO绑定,并选择在线程之间随意切换。
Python提供了 asyncio 模块,该模块可以实现在同一个线程内进行任务的调度,不会消耗过多的内存,因此特别适合IO阻塞性任务。
本节将对asyncio模块的使用进行详细讲解。

14.7.1 什么是异步编程

异步编程是一种并发编程的模式,通过调度不同任务之间的执行和等待时间,达到减少整个程序的执行时间。
异步编程跟同步编程最大的不同就是其任务的切换,当遇到一个需要等待长时间执行的任务时,我们可以切换到其他的任务来执行,
以加快程序的执行速度。与多线程和多进程相比,异步编程只是在同一个线程之内的任务调度,不会消耗过多的内存,因此特别适合IO阻塞性任务。

Python 提供了 asyncio 模块来支持异步编程,该模块中有3个重要概念,具体如下。

- event loops：事件循环,主要负责跟踪和调度所有异步任务,用于管理某个时间点需要执行的任务。
- coroutines：协程,是一种用 async def 关键字定义的函数,该函数可以在执行中暂停并切换到事件循环执行流程的特殊类型的函数。
当处于I/O等待时,该函数会将控制权归还给事件循环。协程函数只有在被封装到 task 容器中后,才能被事件循环执行任务调度。
此时,协程函数才算真正被执行,协程对象中包含需要执行的任务。
- futures：用于托管多个协程对象并返回其执行结果,同时随着任务的执行来记录任务的执行状态。
asyncio 模块在执行异步任务时,需要 event loops(事件循环)、coroutines(协程)、futures 三者的紧密协作。
首先事件循环启动后,会从任务队列中获取第一个需要执行的协程任务。当协程执行到IO阻塞的地方时,当前协程会被挂起,
任务的执行就会暂停并释放执行线程给事件循环,接着事件循环会获取下一个等待执行的协程,以此类推。
当事件循环执行完队列中的最后一个协程才会切换到第一个协程。
当任务执行结束后,事件循环会将任务从列队中移除,对应的执行结果会同步到future中,这个过程会持续到所有的任务执行结束,如图14.22所示。

14.7.2 创建协程任务

在使用 asyncio 模块实现异步编程时,首先需要创建一个以 async 关键字开头的协程任务,然后需要创建一个事件循环用于执行协程任务,
最后绑定回调函数用于获取返回的执行结果。asyncio 常用关键字与函数说明如下。

- async关键字：用于定义一个协程函数。
- await关键字：用于挂起协程,当事件循环遇到需要挂起的协程时,就会执行其他协程,
直到其他的协程也挂起或者执行完毕,再进行下一个协程的执行。
- new_event_loop()函数：用于创建一个新的事件循环对象。
- set_event_loop()函数：设置当前线程的事件循环。
- create_task()函数：用于创建一个协程任务。
- add_done_callback()函数：用于绑定回调函数。
- run_until_complete()函数：运行循环事件中的协程任务,直到所有协程任务被完成。

下面将通过一个实例来演示如何创建一个简单的协程任务,具体代码如下：

"""
import asyncio  # 导入 asyncio 模块


# 创建一个用于测试的协程任务的函数
async def test_task(a, b):
    return a + b


t = test_task(3, 2)  # 实例化测试的协程函数
loop = asyncio.new_event_loop()  # 创建事件循环
asyncio.set_event_loop(loop)  # 设置事件循环对象
task = loop.create_task(t)  # 创建协程任务
loop.run_until_complete(task)  # 将协程注册到事件循环,然后启动事件循环
print('协程函数中的结果为：', task.result())  # 输出协程函数中的结果
