from multiprocessing import Process  # 导入模块

"""
为了实现在同一时间运行多个任务,Python 引入了多线程的概念。在 Python 中可以通过方便、快捷的方式启动多线程模式。
多线程经常被应用在符合并发机制的程序中,如网络程序等。为了进一步将工作任务细分,在一个进程内可以使用多个线程。本章将结合实例由浅入深地向读者介绍在Python中如何创建并使用多线程和多进程。

14.1 什么是进程

了解进程前,需要先知道多任务的概念。多任务,顾名思义就是指操作系统能够执行多个任务。
例如,使用Windows或Linux操作系统可以同时看电影、聊天、查看网页等,此时操作系统就是在执行多任务。
每个任务都是一个进程,打开Windows任务管理器可查看系统当前执行的进程,如图14.1所示。
从该图中可以看到,当前进程中不仅包括应用程序(如QQ、Microsoft Word、PyCharm等)进程,还包括系统进程。

进程(process)是计算机中已运行程序的实体。进程与程序不同,程序本身只是指令、数据及其组织形式的描述,
而进程才是程序(那些指令和数据)的真正运行实例。例如：在没有打开腾讯QQ时,腾讯QQ只是程序;
打开腾讯QQ后,操作系统就为腾讯QQ开启了一个进程;再打开一个腾讯QQ,则又开启了一个进程,如图14.2所示。

14.2 创建进程的常用方式

Python 中有多个模块可以创建进程,比较常用的有 os.fork()函数、multiprocessing 模块和 Pool 进程池。
由于 os.fork() 函数只适合在 UNIX/Linux/Mac 系统上运行,而在 Windows 操作系统中不可用,
因此本章重点介绍 multiprocessing 模块和 Pool 进程池这两个跨平台模块。

14.2.1 使用multiprocessing模块创建进程

multiprocessing 模块提供了一个 Process 类来代表一个进程对象,其语法格式如下：
Process([group [, target [, name [, args [, kwargs]]]]])

Process类的参数说明如下。
- group：参数未使用,值始终为None。
- target：表示当前进程启动时执行的可调用对象。
- name：表示当前进程实例的别名。
- args：表示传递给target函数的参数元组。
- kwargs：表示传递给target函数的参数字典。

例如,实例化Process类,执行子进程,代码如下：
"""


# 执行子进程代码
def test(interval):
    print('我是子进程')


# 执行主程序
def main():
    print('主进程开始')
    p = Process(target=test, args=(1,))  # 实例化Process进程类
    p.start()  # 启动子进程
    print('主进程结束')


if __name__ == '__main__':
    main()
"""
上述代码中,先实例化 Process 类,然后使用 p.start() 方法启动子进程,开始执行 test()函数。
Process 的实例p常用的方法除start()外,还有如下方法。
- is_alive()：判断进程实例是否还在执行。
- join([timeout])：是否等待进程实例执行结束,或等待多少秒。
- start()：启动进程实例(创建子进程)。
- run()：如果没有给定target参数,对这个对象调用start()方法时,则将执行对象中的run()方法。
- terminate()：不管任务是否完成,立即终止。

Process类还有如下常用属性。
- name：当前进程实例别名,默认为Process-N,N为从1开始递增的整数。
- pid：当前进程实例的PID值。
"""
