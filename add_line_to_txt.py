import numpy as np

def add_line_to_txt(line,file_add):
    '''按行添加到指定文本中'''
    f = open(file_add, 'a+')
    f.write(line + '\n')
    f.closed