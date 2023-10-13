# -*- coding:utf-8 -*-
from threading import Thread
import time

"""
14.6 线程间通信

我们已经知道进程之间不能直接共享信息,那么线程之间可以共享信息吗？我们可以通过一个例子来验证这一点。
定义一个全局变量g_num,然后创建两个线程来对g_num执行不同的操作,
其中plus()函数执行全局变量g_num += 50的操作,minus()函数执行全局变量g_num -= 50的操作,最后输出操作后的结果,代码如下：
"""
def plus():
    print('-------子线程1开始------')
    global g_num
    g_num += 50
    print('g_num is %d' % g_num)
    print('-------子线程1结束------')


def minus():
    time.sleep(1)
    print('-------子线程2开始------')
    global g_num
    g_num -= 50
    print('g_num is %d' % g_num)
    print('-------子线程2结束------')


g_num = 100  # 定义一个全局变量
if __name__ == '__main__':
    print('-------主线程开始------')
    print('g_num is %d' % g_num)
    t1 = Thread(target=plus)  # 实例化线程t1
    t2 = Thread(target=minus)  # 实例化线程t2
    t1.start()  # 开启线程t1
    t2.start()  # 开启线程t2
    t1.join()  # 等待t1线程结束
    t2.join()  # 等待t2线程结束
    print('-------主线程结束------')
"""
上述代码中定义了一个全局变量g_num,赋值为100。然后创建两个线程：一个线程将g_num增加50；另一个线程将g_num减少50。
如果g_num最终结果为100,则说明线程之间可以共享数据。运行结果如图14.17所示。

从上述例子中可以得出,在一个进程内的所有线程共享全局变量,这样可以在不使用其他方式的前提下完成多线程之间的数据共享。
"""