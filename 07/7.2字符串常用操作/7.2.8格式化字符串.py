"""
7.2.8 格式化字符串

格式化字符串的意思是先制定一个模板,在这个模板中预留几个空位,然后根据需要填上相应的内容。
这些空位需要通过指定的符号进行标记(也称为占位符),而这些符号将不会被显示。在Python中,格式化字符串有以下两种方法。

1.使用"%"操作符

在Python中,要实现格式化字符串,可以使用"%"操作符。其语法格式如下：
'%[-][+][0][m][.n]格式字符'%exp

参数说明如下。
  -：可选参数,用于指定左对齐,正数前面无符号,负数前面加负号。
  +：可选参数,用于指定右对齐,正数前面加正号,负数前面加负号。
  0：可选参数,表示右对齐,正数前面无符号,负数前面加负号,用0填充空白处(一般与m参数一起使用)。
  m：可选参数,表示占有宽度。
  .n：可选参数,表示小数点后保留的位数。
  格式字符：用于指定类型。其值如表7.1所示。
  表7.1 常用的格式字符及其说明
| 格式字符 | 说明                      | 格式字符 | 说明                        |
| -------- | ------------------------- | -------- | --------------------------- |
| %s       | 字符串(采用str()方法显示) | %r       | 字符串（采用repr()方法显示) |
| %c       | 单个字符                  | %o       | 八进制整数                  |
| %d或者%i | 十进制整数                | %e       | 指数(基底写为e)             |
| %x       | 十六进制整数              | %E       | 指数(基底写为E)             |
| %f或者%F | 浮点数                    | %%       | 字符%                       |

  exp：要转换的项。如果要指定的项有多个,需要通过元组的形式进行指定,但不能使用列表的形式来指定。

例如,格式化输出一个保存公司信息的字符串,代码如下：
"""
template = '编号：%09d\t公司名称： %s \t官网： http://www.%s.com'  # 定义模板
context1 = (7, '百度', 'baidu')  # 定义要转换的内容1
context2 = (8, '明日学院', 'mingrisoft')  # 定义要转换的内容2
print(template % context1)  # 格式化输出
print(template % context2)  # 格式化输出
"""
说明：由于使用"%"操作符是早期Python中提供的方法,因此自从Python 2.6版本开始,字符串对象提供了format()方法对字符串进行格式化。
当前一些Python社区也推荐使用这种方法。所以建议大家重点学习format()方法的使用。

2.使用字符串对象的format()方法

字符串对象提供了format()方法对字符串进行格式化。其语法格式如下：
str.format(args)

其中：str用于指定字符串的显示样式(即模板);args用于指定要转换的项,如果有多项,则用逗号进行分隔。

下面重点介绍如何创建模板。在创建模板时,需要使用"{}"和":"指定占位符,基本语法格式如下：
{[index][:[[fill]align][sign][#][width][.precision][type]]}

参数说明如下。
-  index：可选参数,用于指定要设置格式的对象在参数列表中的索引位置,索引值从0开始。如果省略,则根据值的先后顺序进行自动分配。
误区警示：当一个模板中出现多个占位符时,指定索引位置的规范必须统一,即全部采用手动指定,或者全部采用自动指定。
例如,定义"'我是数值：{:d},我是字符串：{1:s}'"模板是错误的,将会抛出如图7.18所示的异常信息。
-  fill：可选参数,用于指定空白处填充的字符。
-  align：可选参数,用于指定对齐方式。该参数的值为"<"时,表示内容左对齐；值为">"时,表示内容(包括符号)右对齐;
值为"="时,只对数字类型有效,表示数字内容右对齐,如果是负数,则将负号放在填充内容的最左侧,如果是正数,不添加符号;
值为"^"时,表示内容居中。该参数需要配合width一起使用。
-  sign：可选参数,用于指定有无符号数(值为"+"表示正数加正号,负数加负号；值为"-"表示正数不变,负数加负号;
值为空格表示正数加空格,负数加负号)。
-  #：可选参数,对于二进制、八进制和十六进制,如果加上"#",表示会显示0b/0o/0x前缀,否则不显示前缀。
-  width：可选参数,用于指定所占宽度。
-  .precision：可选参数,用于指定保留的小数位数。
-  type：可选参数,用于指定类型,其值如表7.2所示。

例如，定义一个保存公司信息的字符串模板，然后应用该模板输出不同公司的信息，代码如下：
"""
template = '编号：{:0>9s}\t公司名称： {:s} \t官网： http://www.{:s}.com'  # 定义模板
context1 = template.format('7', '百度', 'baidu')  # 转换内容1
context2 = template.format('8', '明日学院', 'mingrisoft')  # 转换内容2
print(context1)  # 输出格式化后的字符串
print(context2)  # 输出格式化后的字符串
