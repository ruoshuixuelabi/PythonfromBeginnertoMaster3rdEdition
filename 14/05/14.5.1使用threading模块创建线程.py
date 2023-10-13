# -*- coding:utf-8 -*-
import threading, time

"""
14.5 创建线程

由于线程是操作系统直接支持的执行单元,因此高级语言(如Python、Java等)通常都内置多线程的支持。
Python的标准库提供了两个模块,即 _thread 和 threading。其中：_thread 是低级模块；
threading 是高级模块,它对 _thread 进行了封装。绝大多数情况下,我们只需要使用 threading 这个高级模块。

14.5.1 使用threading模块创建线程

threading 模块提供了一个 Thread 类来代表一个线程对象,其语法格式如下：
Thread([group [, target [, name [, args [, kwargs]]]]])

Thread类的参数说明如下。
- group：值为None,为以后版本而保留。
- target：表示一个可调用对象,线程启动时,run()方法将调用此对象。默认值为None,表示不调用任何内容。
- name：表示当前线程名称,默认创建一个Thread-N格式的唯一名称。
- args：表示传递给target函数的参数元组。
- kwargs：表示传递给target函数的参数字典。

对比发现,Thread类和前面讲解的Process类的方法基本相同,这里就不再赘述了。
下面通过一个例子来学习如何使用threading模块创建进程,代码如下：
"""


def process():
    for i in range(3):
        time.sleep(1)
        print("thread name is %s" % threading.current_thread().name)


if __name__ == '__main__':
    print("-----主线程开始-----")
    threads = [threading.Thread(target=process) for i in range(4)]  # 创建4个线程,存入列表中
    for t in threads:
        t.start()  # 开启线程
    for t in threads:
        t.join()  # 等待子线程结束
    print("-----主线程结束-----")
"""
-----主线程开始-----
thread name is Thread-4 (process)
thread name is Thread-3 (process)thread name is Thread-2 (process)
thread name is Thread-1 (process)

thread name is Thread-4 (process)thread name is Thread-2 (process)thread name is Thread-3 (process)

thread name is Thread-1 (process)

thread name is Thread-2 (process)thread name is Thread-1 (process)
thread name is Thread-3 (process)
thread name is Thread-4 (process)

-----主线程结束-----
"""
