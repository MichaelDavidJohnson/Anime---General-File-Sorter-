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
        return("No suitable files found!")
    if not len(tempfileStorage) == 0:
            for filey in tempfileStorage:
                print( filey )
                return tempfileStorage

def extensionremover(filename):
    registry = '\.(avi|mp4|mkv)|([-])+([ ])+([0-9])+'
    new_name = re.sub(registry,r'',filename)
    return new_name
def crc16(data: bytes, poly=0x8408):
    data = bytearray(data)
    crc = 0xFFFF
    for b in data:
        cur_byte = 0xFF & b
        for _ in range(0, 8):
            if (crc & 0x0001) ^ (cur_byte & 0x0001):
                crc = (crc >> 1) ^ poly
            else:
                crc >>= 1
            cur_byte >>= 1
    crc = (~crc & 0xFFFF)
    crc = (crc << 8) | ((crc >> 8) & 0xFF)
    return crc & 0xFFFF

def move():
        for _ in files:
            if _.lower().endswith(('.avi', '.mp4', '.mkv')):
                print("Attempting to copy: ",_)
            if _ == '.ipynb_checkpoints':
                continue
            if extensionremover(_) == _:
                continue
            else:
                if _.lower().endswith(('.avi', '.mp4', '.mkv')):
                    if not os.path.exists(extensionremover(_)):
                        os.mkdir(extensionremover(_))
                        shutil.copy(os.path.join(cwd,_),os.path.join(cwd,extensionremover(_)))
                        print("Copy complete, verifying")
                        if crc16(open(os.path.join(cwd,_))) == crc16(open(os.path.join(cwd,extensionremover(_),_))):
                            os.remove(os.path.join(cwd,_))
                            print("File",_,"is verified")
                        else:
                            os.remove(os.path.join(cwd,extensionremover(_),_))
                            print("Copying Failed for: ",_)
                    else:
                        shutil.copy(os.path.join(cwd,_),os.path.join(cwd,extensionremover(_)))
                        print("Copy complete,verifying")
                        if crc16(open(os.path.join(cwd,_))) == crc16(open(os.path.join(cwd,extensionremover(_),_))):
                            os.remove(os.path.join(cwd,_))
                            print("File",_,"is verified")
                        else:
                            os.remove(os.path.join(cwd,extensionremover(_),_))
                            print("Copying Failed for: ",_)
