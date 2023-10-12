import pymysql

# 打开数据库连接
db = pymysql.connect(host="localhost", user="root", password="root", database="mrsoft",charset="utf8")
# 使用cursor()方法获取操作游标对象
cursor = db.cursor()
# 数据列表
data = [("Python树莓派开发从入门到精通",'Python','89.80','2021-10-01'),
	("Python算法设计与分析从入门到精通",'Python','79.80','2021-11-01'),
	("C++从入门到精通（第5版）",'C++','89.80','2021-12-01'),
	("PHP从入门到精通（第6版）",'PHP','99.80','2022-03-01'),
	("C#从入门到精通（第6版）",'C#','99.80','2021-11-01'),
]
try:
    # 执行SQL语句，插入多条数据
    cursor.executemany("insert into books(name, category, price, publish_time) values (%s,%s,%s,%s)", data)
    # 提交数据
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# 关闭数据库连接
db.close()
