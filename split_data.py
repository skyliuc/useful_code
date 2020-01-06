#划分数据集
#输入是file2idx
#val_ratio是验证集的比例
#划分方式，采用python的集合操作
def split_data(file2idx, val_ratio=0.1):
    '''
    划分数据集,val需保证每类至少有1个样本
    :param file2idx:
    :param val_ratio:验证集占总数据的比例
    :return:训练集，验证集路径
    '''
    data = set(os.listdir(config.train_dir))
    # set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等
    # >>>x = set('runoob')
    # {'b', 'r', 'u', 'o', 'n'}# 重复的被删除
    # 'set' object does not support indexing
    val = set()
    idx2file = [[] for _ in range(config.num_classes)]
    # idx2file = [[] for _ in range(3)]
    # Out: [[], [], []]
    for file, list_idx in file2idx.items():
    
        for idx in list_idx:
            idx2file[idx].append(file)
    # Python 字典(Dictionary) items() 函数以列表返回可遍历的(键, 值) 元组数组,用法：dict.items()
    # dict_items([('2.txt', [0, 9]), ('5.txt', [0, 9]).....
    # file如'2.txt'，
    # list_idx如[0, 9]
    # idx2file:['1036.txt','17675.txt', '17893.txt', '17900.txt', '17937.txt', '18030.txt',.. '34219.txt']
    # 至此统计了每一个idx比如序号为54的顺钟向转位，含有该类标签的全部文件
    for item in idx2file:
        # print(len(item), item)
        num = int(len(item) * val_ratio)#每一个Idx对应生成10%的验证集
        val = val.union(item[:num])#生成只出现一次的文件
    # union() 方法返回两个集合的并集，即包含了所有集合的元素，重复的元素只会出现一次。
    # x = {"apple", "banana", "cherry"}
    # y = {"google", "runoob", "apple"}
    # z = x.union(y) 
    # print(z) 输出为{'cherry', 'runoob', 'google', 'banana', 'apple'}
    train = data.difference(val)
    #把所有的data中剔除val就是训练集了
    #z = x.difference(y) -->> {'cherry', 'banana'}
    return list(train), list(val)