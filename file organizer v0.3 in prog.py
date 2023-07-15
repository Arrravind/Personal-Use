import os
import shutil

def organize(path):
    files = os.listdir(path)
    for file in files:
        filename,extension = os.path.splitext(file)
        extension = extension[1:]

        if os.path.exists(path+'/'+extension):
            shutil.move(path+'/'+file,path+'/'+extension+'/'+file)

        else:
            os.makedirs(path+'/'+extension)
            shutil.move(path+'/'+file,path+'/'+extension+'/'+file)
    
ans=input("Enter \'y\' or \'Y\' to Organize : ").lower()
while ans=='y':         
    pa = input("Enter the path here :")
    if pa in os.listdir():
        organize(pa)
        print("File Organized Successfully!!! :)")
    else:
        print("Invalid Path")
    ans=input("Do You Want To Continue ? [y] or [Y] :")

