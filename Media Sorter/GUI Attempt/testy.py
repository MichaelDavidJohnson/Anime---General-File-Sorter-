import os
import re
import glob
import shutil
from tkinter import *
from tkinter import dialog
cwd = os.getcwd()
files = os.listdir(cwd)

def filelister():

    tempfileStorage = []
    for file in files:
        if file.lower().endswith(('.avi','.mp4','.mkv')):	
            tempfileStorage.append(file)
        else:
            continue
    if len(tempfileStorage) == 0:
        print("No suitable files found!")
    if not len(tempfileStorage) == 0:
            for filey in tempfileStorage:
                print( filey )
filelister()