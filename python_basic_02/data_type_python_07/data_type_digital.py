#!/usz/bin/env python
# -*- coding:utf-8 -*-


"""
@file       : data_type_digital.py
@author     : zgf
@brief      : 数据类型- digital
@attention  : life is short,I need python
"""


# =========================================  数据类型 =========================================
# 在 Python 中定义变量是 不需要指定类型（在其他很多高级语言中都需要）
# 数据类型可以分为 数字型 和 非数字型
# 数字型： 整型 (int) 浮点型（float） 布尔型（bool）真 True 非 0 数 —— 非零即真 假 False 0 复数型 (complex)
# 非数字型 -字符串 -列表 -元组 -字典
# flag = True
flag = False
if flag:
    pass


# =========================================  数字类型 - 字节（bytes） =========================================
# python的基础数据类型之一，他和str相当于双胞胎，str拥有的所有方法，bytes类型都适用
# 内部编码方式：非unicode
# 你想将一部分内容（字符串）写入文件，或者通过网络socket传输，这样这部分内容（字符串）必须转化成bytes才可以进行
# 平时你代码中，使用字符串。
# flag = True
flag = False
if flag:
    i = b"alex"
    print(i, type(i))  # 查询十进制转化成二进制占用的最小位数


# =========================================  数字类型 - 整型（int） =========================================
# 整型是不可变类型
# 数据类型之间的转化。 int ---> str str (int) int(str) - int----bool:非零及True,零即为False,True--->1 False--->0
# flag = True
flag = False
if flag:
    age = 18
    print(age, type(age))


# =========================================  数字类型 - 整型（int） - 进制转换 =========================================
# 数据类型之间的转化。 int ---> str str (int) int(str) - int----bool:非零及True,零即为False,True--->1 False--->0
# flag = True
flag = False
if flag:
    print(16 == 0b10000 == 0o20 == 0x10)  # 默认输入十进制 二进制0b、八进制0o、十六进制0x
    # 十进制与其他进制的转换
    # bin：将十进制转换成二进制并返回。
    a = bin(16)  # 转二进制 注意：上述转换后结果为字符串类型
    # oct：将十进制转化成八进制字符串并返回。
    b = oct(16)  # 转八进制 注意：上述转换后结果为字符串类型
    # hex：将十进制转化成十六进制字符串并返回。
    c = hex(16)  # 转十六进制 注意：上述转换后结果为字符串类型
    print(
        a,
        b,
        c,
        type(a),
        type(b),
        type(c),
    )  # 0b10000 0o20 0x10
    print(a == b == c)  # False
    # 其他进制转换十进制
    d = int(a, 2)  # 二进制转十进制
    e = int(b, 8)  # 八进制转十进制
    f = int(c, 16)  # 十六进制转十进制
    print(d, e, f)  # 16 16 16

    i = 4
    print(i.bit_length())  # 查询十进制转化成二进制占用的最小位数


# =========================================  1.数字类型 - 浮点型（float） =========================================
# 浮点型是不可变类型
# 计算机采用二进制小数来表示浮点数的小数部分
# 部分小数不能用二进制小数完全表示,通常情况下不会影响计算精度
# flag = True
flag = False
if flag:
    height = 1.83
    print(height, type(height))
    # 不确定小数问题
    print((0.1 + 0.2) == 0.3)  # False
    print(0.1 + 0.2)  # 0.30000000000000004
    print(0.1 + 0.7)  # 0.7999999999999999
    a = 3 * 0.1
    print(a)
    b = round(a, 1)
    print(b, b == 0.3)


# =========================================  1.数字类型 - 复数（complex）a+bj =========================================
# 大写J或小写j均可
# 虚部系数为1时，需要显式写出
# 3是实部，4是虚部
# flag = True
flag = False
if flag:
    a = 3 + 4j
    print(a, type(a))
    print(3 + 4j, 2 + 5j, type(3 + 4j), type(2 + 5j))
    print(2 + 1j)  # 虚部系数为1时，需要显式写出
