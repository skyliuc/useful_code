#给定Path比如，/xxx/hf_round1_arrythmia.txt
#文件主要针对将文字类型的标签转化成数字
#比如将窦性心律转化成数字键0
def name2index(path):
    '''
    把类别名称转换为index索引
    :param path: 文件路径
    :return: 字典比如{'窦性心律'：0}
    '''
    list_name = []
    for line in open(path, encoding='utf-8'):
        list_name.append(line.strip())
    name2indx = {name: i for i, name in enumerate(list_name)}
    return name2indx

# 补充知识
# python 读取多行数据
# https://blog.csdn.net/qq_37383691/article/details/78078736
# open(file_path, ‘-模式-‘,encoding=’UTF-8’) 
# 即open(路径+文件名, 读写模式, 编码)
# 字典的每个键值 key=>value 对用冒号 : 分割，每个键值对之间用逗号 , 分割，整个字典包括在花括号 {} 中
# encoding='utf-8'解决中文数据必要的神技
# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
# >>>seq = ['one', 'two', 'three']
# >>> for i, element in enumerate(seq):
# ...     print i, element
# ... 
# 0 one
# 1 two
# 2 three
# name2indx输出第一行是名字，第二行是序号
# 比如{'窦性心律'：0}