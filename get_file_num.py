# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 15:58:25 2019
#统计文件数量
#应用时修改path即可
@author: skyliuhc
"""


import os
 
   #获取当前路径
def get_num_of_dir(path): 
    num_dirs = 0 #路径下文件夹数量
    num_files = 0 #路径下文件数量(包括文件夹)
    num_files_rec = 0 #路径下文件数量,包括子文件夹里的文件数量，不包括空文件夹
     
     
    for root,dirs,files in os.walk(path):    #遍历统计
            for each in files:
                    if each[-2:] == '.o':
                            print (root,dirs,each)
                    num_files_rec += 1
            for name in dirs:
                    num_dirs += 1
                    print (os.path.join(root,name))
     
    for fn in os.listdir(path):
            num_files += 1
            print (fn)
    print('-------')
    print ('路径下文件夹数量:',num_dirs)
    print ('路径下文件数量(包括文件夹)',num_files)
    print ('径下文件数量,包括子文件夹里的文件数量，不包括空文件夹',num_files_rec)
    return num_dirs

if __name__ == '__main__':
    print('ok')
    path = os.getcwd()+'\\save_data\\' 
    num_dirs=get_num_of_dir(path)