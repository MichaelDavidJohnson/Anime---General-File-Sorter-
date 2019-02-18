import os
from tkinter import filedialog
from tkinter import *
nameList = []

pathz = []
def stringError(text):
    val = int(totalDir)
    return val
def driveNumber():
    totalDir = input("How many directories do you want to use?\n")
    return totalDir
    stringError(totalDir)
    return totalDir,val
def directoryFinder(value):
    count = 1
    master = Tk()
    while count < int(value)+1:
        print("What is the ",count," st/th directory?")
        master.directory = filedialog.askdirectory()
        pathz.append(master.directory)
        count += 1
    return pathz
def fileLister(paths):
    for path in paths:
        files = os.listdir(path)
        for names in files:
            nameList.append(names)
    return nameList
def turntotxt(namelist):
    cwd  = os.getcwd()
    f = open("File_Names.txt","w+")
    for name in namelist:
        f.write('%s\n' % name)
    return f    
    
    



def main():
    val = driveNumber()
    pathz = directoryFinder(val)
    nameList = fileLister(pathz)
    turntotxt(nameList)



if __name__ == '__main__':
     main()
     input("Press ENTER to exit")    
