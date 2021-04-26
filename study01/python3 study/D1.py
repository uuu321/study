
# 一、字典dict
# https://blog.csdn.net/xuanyin235/article/details/82390028
# https://www.runoob.com/python3/python3-dictionary.html
# 1、访问字典里的值（键必须不可变，所以可以用数字，字符串或元组充当）
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])
# 2、修改字典
dict['Name'] = 'A'
dict['Age'] = 8
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])
# 3、删除字典元素
del dict['Name']  # 删除键
print("dict:", dict)
dict.clear()  # 清空字典
print("dict:", dict)
# 4、字典内置函数&方法
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("字典元素个数，即键的总数：", len(dict))
print("输出字典：", str(dict))
print("返回输入的变量类型：", type(dict))

# 二、range（）函数
for i in range(5):
    print(i)
print(list(range(5)))
print(list(range(0, 30, 5)))  # start、stop、step（步长）
print(list(range(0, 30, 10)))

# 三、def:self
# https://www.runoob.com/python3/python3-function.html


# 四、append() 方法：用于在列表末尾添加新的对象。
list1 = ['Google', 'Runoob', 'Taobao']
print ("更新前的列表 : ", list1)
list1.append('Baidu')
print ("更新后的列表 : ", list1)

# 五、序列
line = "abcde"
  # 逆序操作：切片
print(line[-1], line[-2], line[-3])
print(line[::-1])

# 六、zip() 函数：用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象
# https://www.runoob.com/python3/python3-func-zip.html