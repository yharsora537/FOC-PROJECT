import os
import shutil
import tkinter as tk
from tkinter import filedialog
import datetime
import glob

#functions

def submit():
    print('submitted')
    path=path_entry.get()
    list=os.listdir(path)
    path_dir=path_entry.get()
    sort_option=sort_var.get()
    for files in os.walk(path_dir):
        if sort_option=='Alphabetical':
            
            sorted(path_dir)
        
        else:
            print('datewise')
            '''sorted_items = ext(files, key=lambda item: os.path.getctime(os.path.join(path_dir,files))                        )
            return sorted_items'''
            files=path
            # Use the glob module to find all files in the current directory with a ".txt" extension.
            files = glob.glob("*.txt")

            # Sort the list of file names based on the modification time (getmtime) of each file.
            files.sort(key=os.path.getmtime)

            # Print the sorted list of file names, one per line.
            print("\n".join(files))

            #path_dir.sort(key=lambda date: datetime.strptime(date, "%m-%Y"))

            #readList[path_dir]=datetime.strptime(readList[path_dir],"%d/%m/%Y")
            #path_dir.sort(key=lambda x: os.path.getmtime(os.path.join(directory, x)))

    for file in list:
       name,ext=os.path.splitext(file)
       ext=ext[1:]
    
       if os.path.exists(path+'/'+ext):
           shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
       else:
          os.makedirs(path+'/'+ext)
          shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
       
    print('Your files are successfully moved')
    


#def sort_var():


#create GUI
root=tk.Tk()
root.title("file_organizer")

#input as path

tk.Label(root,text="enter your path= ").pack()
path_entry=tk.Entry(root)
path_entry.pack()

#creating radio buttons for choice

sort_var=tk.StringVar()
sort_var.set("Alphabetical")

alpha_radio=tk.Radiobutton(root,text="Alphabetical", variable=sort_var, value="Alphabetical")
alpha_radio.pack()

date_radio = tk.Radiobutton(root, text="Date-wise", variable=sort_var, value="Date-wise")
date_radio.pack()

#creating submit button

s_b=tk.Button(root,text="Submit",command=submit)
s_b.pack()

root.mainloop()



















