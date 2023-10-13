# -*- coding: utf-8 -*-
import threading
import time

"""
14.5.2 使用Thread子类创建线程

Thread 线程类和 Process 进程类使用方式非常相似。也可以通过定义一个继承 Thread 线程类的子类来创建线程。
下面通过一个例子来学习使用Thread子类创建线程的方式。

【例14.5】使用Thread子类创建线程。 

创建一个子类SubThread,它继承threading.Thread线程类,然后定义一个run()方法。
实例化 SubThread 类以创建两个线程,并调用 start()方法来开启线程。此时,线程会自动调用 run()方法。具体代码如下：
"""


class SubThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "子线程" + self.name + '执行,i=' + str(i)  # name属性中保存的是当前线程的名字
            print(msg)


if __name__ == '__main__':
    print('-----主线程开始-----')
    t1 = SubThread()  # 创建子线程t1
    t2 = SubThread()  # 创建子线程t2
    t1.start()  # 启动子线程t1
    t2.start()  # 启动子线程t2
    t1.join()  # 等待子线程t1
    t2.join()  # 等待子线程t2
    print('-----主线程结束-----')
"""
对比例14.2可以发现：例14.2在使用子类创建进程时,SubProcess类定义了__init__()初始化方法,
并且在__init__()方法中调用了父类的__init__()方法；
而在例14.5中,SubThread类并没有定义__init__()方法,所以在实例化SubThread类时会自动调用父类的__init__()初始化方法。
是否使用__init__()初始化方法,取决于实例化类时是否需要传递参数。
"""