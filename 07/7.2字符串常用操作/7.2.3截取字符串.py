"""
7.2.3 截取字符串

由于字符串也属于序列,因此如果截取字符串,则可以采用切片方法来执行此操作。切片方法的语法格式如下：
string[start : end : step]
参数说明如下。
-  string：表示要截取的字符串。
-  start：表示要截取的第一个字符的索引(包括该字符),如果不指定,则默认为0。
-  end：表示要截取的最后一个字符的索引(不包括该字符),如果不指定,则默认为字符串的长度。
-  step：表示切片的步长,如果省略,则默认为1,当省略该步长时,最后一个冒号也可以被省略。

说明：字符串的索引同序列的索引是一样的,也是从0开始的,并且每个字符占一个位置,如图7.4所示。

例如，定义一个字符串，然后应用切片方法截取不同长度的子字符串，并输出结果，代码如下：
"""
str1 = '人生苦短，我用Python!'  # 定义字符串
substr1 = str1[1]  # 截取第2个字符
substr2 = str1[5:]  # 从第6个字符开始截取
substr3 = str1[:5]  # 从左边开始截取5个字符
substr4 = str1[2:5]  # 截取第3个到第5个字符
print('原字符串：', str1)
print(substr1 + '\n' + substr2 + '\n' + substr3 + '\n' + substr4)
"""
执行上述代码，将显示以下内容：
原字符串： 人生苦短，我用Python!
生
我用Python!
人生苦短，
苦短，

注意:进行字符串截取时,如果指定索引不存在,则会抛出如图7.5所示的异常信息。
要解决该问题，需要采用try…except语句(参见第12章)捕获异常。例如,下列代码在执行后将不会抛出异常：
"""
str1 = '人生苦短，我用Python!'  # 定义字符串
try:
    substr1 = str1[15]  # 截取第15个字符
except IndexError:
    print('指定的索引不存在')
