# -*- coding: utf-8 -*-
'''
参数文件，通用模板

@ author: skyliuhc
'''
import os


class Config:
    # for data_process.py
    #root = r'D:\ECG'
    #把数据放在data文件下
    root = r'data'
    train_dir = os.path.join(root, 'Your_train_dir')
    test_dir = os.path.join(root, 'Your_test_dir')
    train_label = os.path.join(root, 'Your_train_label_dir')
    test_label = os.path.join(root, 'Your_test_label_dir')
    Label = os.path.join(root, 'Your_label_dir')#总的label
    train_data = os.path.join(root, 'train.pth')
    # train_data保存的是里面有traindata,validdata,index2name,file2index等，使用pytorch里面的方法保存的
    # for train
    # 
    #训练的模型名称
    model_name = 'Your_model_name'
    #在第几个epoch进行到下一个state,调整lr
    stage_1=100
    stage_2=160
    stage_3=200
    stage_epoch = [stage_1,stage_2,stage_3]
   
    batch_size = 64 #训练时的batch大小
 
    num_classes = 55 #label的类别数
 
    max_epoch = 256  #最大训练多少个epoch
 
    #保存模型的文件夹
    ckpt = 'ckpt'
    #保存提交文件的文件夹
    sub_dir = 'submit'
    #初始的学习率
    lr = 1e-3
    #保存模型当前epoch的权重
    current_w = 'current_w.pth'
    #保存最佳的权重
    best_w = 'best_w.pth'
    # 学习率衰减 lr/=lr_decay
    lr_decay = 10

    #for test
    temp_dir=os.path.join(root,'temp')


config = Config()
