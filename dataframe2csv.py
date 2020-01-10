from pandas import DataFrame
import pandas

def dataframe2csv(dataframe,dest_add):
    '''将dataframe格式的数据保存为csv格式文件'''
    dataframe.to_csv(dest_add, encoding='utf_8_sig')