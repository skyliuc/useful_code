def read_code_from_txt(file_add):
    '''从文本中按行读取'''
    list=[]
    for line in open(file_add,'r'):
        line=line.split('\n')
        list.append(line[0])
    return list