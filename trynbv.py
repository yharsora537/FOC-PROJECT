import os
import shutil
path=input('path= ')
list=os.listdir(path)

for file in list:
    name,ext=os.path.splitext(file)
    ext=ext[1:]
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file,ext)
    else:
       os.mkdir(path+'/'+ext)
       shutil.move(path+'/'+file,ext)
       

           
