import os
import re
import glob
import shutil
from tkinter import *
from tkinter import filedialog
from subprocess import check_output
import BackEnd
labels = []
master = Tk()
master.title("Media Sorter and Mover")
master.geometry('640x480')
LC = 1
W =  "w"
count = 0 
def fileshowcase():
        cwd = os.getcwd()
        files = os.listdir(cwd)
        for label in labels:
                label.destroy()
        output = BackEnd.filelister()
        
        for file in output:
                if output == "No suitable files found!":
                        label = Label(master,text = "No suitable files found!", font = ('Helvetica',12), anchor = W)
                        label.grid(column = 1,row=0, sticky=W)
                        labels.append(label)
                        break
                else:
                        label = Label(master,text = str(file), font = ('Helvetica',12), anchor = W)
                        label.grid(column=LC,row=count, sticky=W)
                        labels.append(label)
                        count += 1
                        if count == 18:
                                count = 0
                                for label in labels:
                                        label.destroy()
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

def GUImove():
        cwd = os.getcwd()
        files = os.listdir(cwd)
        count = 0
        for label in labels:
                label.destroy()
        for _ in files:
            if _.lower().endswith(('.avi', '.mp4', '.mkv')):
                temp = "Attempting to copy: " + str(_)
                label = Label(master,text = temp, font = ('Helvetica',12), anchor = E)
                label.grid(column = LC, row = count, sticky=W)
                labels.append(label)
                count += 1
                if count == 18:
                                count = 0
                                for label in labels:
                                        label.destroy()
            if _ == '.ipynb_checkpoints':
                continue
            if extensionremover(_) == _:
                continue
            else:
                if _.lower().endswith(('.avi', '.mp4', '.mkv')):
                    if not os.path.exists(extensionremover(_)):
                        os.mkdir(extensionremover(_))
                        shutil.copy(os.path.join(cwd,_),os.path.join(cwd,extensionremover(_)))
                        label = Label(master,text = "Copy complete, verifying", font = ('Helvetica',12), anchor = E)
                        label.grid(column=LC,row = count, sticky=W)
                        labels.append(label)
                        count += 1
                        if count == 18:
                                count = 0
                                for label in labels:
                                        label.destroy()
                        if crc16(open(os.path.join(cwd,_))) == crc16(open(os.path.join(cwd,extensionremover(_),_))):
                            os.remove(os.path.join(cwd,_))
                            temp = "File " + str(_) + " is verified"
                            label = Label(master,text = temp, font = ('Helvetica',12), anchor = E)
                            label.grid(column=LC,row = count, sticky=W)
                            labels.append(label)
                            count += 1
                            if count == 18:
                                count = 0
                                for label in labels:
                                        label.destroy()
                        else:
                            os.remove(os.path.join(cwd,extensionremover(_),_))
                            temp = "Copying Failed for: " + str(_)
                            label = Label(master,text = temp, font = ('Helvetica',12), anchor = E)
                            label.grid(column=LC,row=count, sticky=W)
                            labels.append(label)
                            count += 1
                            if count == 18:
                                count = 0
                                for label in labels:
                                        label.destroy()
                    else:
                        shutil.copy(os.path.join(cwd,_),os.path.join(cwd,extensionremover(_)))
                        label = Label(master,text = "Copy complete,verifying", font = ('Helvetica',12), anchor = E)
                        label.grid(column=LC,row=count, sticky=W)
                        labels.append(label)
                        count += 1
                        if count == 18:
                                count = 0
                                for label in labels:
                                        label.destroy()
                        if crc16(open(os.path.join(cwd,_))) == crc16(open(os.path.join(cwd,extensionremover(_),_))):
                            os.remove(os.path.join(cwd,_))
                            temp = "File " + str(_) + " is verified"
                            label = Label(master,text = temp, font = ('Helvetica',12), anchor = E)
                            label.grid(column=LC,row=count, sticky=W)
                            labels.append(label)
                            count += 1
                            if count == 18:
                                count = 0
                                for label in labels:
                                        label.destroy()
                        else:
                            os.remove(os.path.join(cwd,extensionremover(_),_))
                            temp = "Copying Failed for: " + str(_)
                            label = Label(master,text = temp, font = ('Helvetica',12), anchor = E)
                            label.grid(column = LC, row = count, sticky=W)
                            labels.append(label)
                            count += 1
                            if count == 18:
                                count = 0
                                for label in labels:
                                        label.destroy()
def FileMover():
        return 0
        

                        
        
button1 = Button(master,text="Verify Files", font = ('Helvetica',12),command = fileshowcase)
button1.grid(column=0,row=0)
button2 = Button(master,text = "Organise Files", font = ('Helvetica',12), command = GUImove)
button2.grid(column=0,row=1)
var = IntVar()
variable2 = IntVar()
checkbox1 = Checkbutton(master,text = "Database?",variable = var, font = ('Helvetica',12), anchor = E)
checkbox1.grid(column=0,row=2)
checkbox2 = Checkbutton(master,text = "Remove Square Brackets?",variable = variable2, font = ('Helvetica',12), anchor = E)
checkbox2.grid(column=0,row=3)
entrybutton = Label(master,text = "How many drives?")
entrybutton.grid(column=0,row=4)
variable = IntVar(master)
variable.set(1)
entrybutton2 = OptionMenu(master,variable,1,2,3,4,5)
entrybutton2.grid(column=0,row=5)
button3 = Button(master, text = "Move Files", font = ('Helvetica',12),command = FileMover)
button3.grid(column=0,row=6)
mainloop()
