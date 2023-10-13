# -*- coding: utf-8 -*-
from queue import Queue
import random, threading, time

"""
14.6.3 使用队列在线程间进行通信

我们知道 multiprocessing 模块的 Queue 队列可以实现进程间通信,同样在线程间也可以使用 Queue 队列实现线程间通信。
不同之处在于,我们需要使用 queue 模块的 Queue 队列,而不是 multiprocessing 模块的 Queue 队列,
但二者的 Queue 队列的使用方法都相同。

使用 Queue 队列在线程间通信通常应用于生产者和消费者模式。产生数据的模块称为生产者,而处理数据的模块称为消费者。
在生产者与消费者之间的缓冲区称为仓库。生产者负责往仓库运输产品,而消费者负责从仓库里取出产品,这就构成了生产者和消费者模式。
下面通过一个例子来学习使用Queue在线程间进行通信。

【例14.7】 使用队列模拟生产者和消费者模式。 

定义一个生产者类Producer和一个消费者类Consumer。
生产者共生成5件产品,并将这5件产品依次写入队列中,而消费者依次从队列中取出产品,代码如下：
"""


# 生产者类
class Producer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.data = queue

    def run(self):
        for i in range(5):
            # print("生产者%s将产品%d加入队列!" % (self.getName(), i))
            print("生产者%s将产品%d加入队列!" % (self.name, i))
            self.data.put(i)
            time.sleep(random.random())
        print("生产者%s完成!" % self.name)


# 消费者类
class Consumer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.data = queue

    def run(self):
        for i in range(5):
            val = self.data.get()
            # print("消费者%s将产品%d从队列中取出!" % (self.getName(), val))
            print("消费者%s将产品%d从队列中取出!" % (self.name, val))
            time.sleep(random.random())
        # print("消费者%s完成!" % self.getName())
        print("消费者%s完成!" % self.name)


if __name__ == '__main__':
    print('-----主线程开始-----')
    queue = Queue()  # 实例化队列
    producer = Producer('Producer', queue)  # 实例化线程Producer,并传入队列作为参数
    consumer = Consumer('Consumer', queue)  # 实例化线程Consumer,并传入队列作为参数
    producer.start()  # 启动线程Producer
    consumer.start()  # 启动线程Consumer
    producer.join()  # 等待线程Producer结束
    consumer.join()  # 等待线程Consumer结束
    print('-----主线程结束-----')
