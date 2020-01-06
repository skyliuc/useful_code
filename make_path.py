#判断有无path这个路径，如果没有则手动创建
#author:skyliuhc
if not os.path.exists(path):
    os.makedirs(path)