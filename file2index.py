#将类似||2.txt           窦性心律    QRS低电压||的文件转换成
#'2.txt':[0,9]
#也就是文件名对应着所属的文件
def file2index(path, name2idx):
    '''
    获取文件id对应的标签类别
    :param path:文件路径
    :name2idx:{'窦性心律'：0}
    :return:文件id对应label列表的字段
    eg:
    '2.txt':[0,9]
    '5.txt':[0,9]
    ...
    '14330.txt':[0,1]
    '''
    file2index = dict()
    for line in open(path, encoding='utf-8'):
        arr = line.strip().split('\t')
        id = arr[0]
        labels = [name2idx[name] for name in arr[3:]]
        # print(id, labels)
        file2index[id] = labels
    return file2index
    # 输出文件名，和对应包含的label数字比如[0,1]