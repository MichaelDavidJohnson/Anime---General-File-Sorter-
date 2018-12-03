import os
import re
import glob
import shutil
from tkinter import *
from tkinter import filedialog
def main():
     pathcount = 0
     totalcount = 0
     currentcount = 0
     moved = None
     namemoved = []
     pathz = []
     print("What is the first file path you want to use:\n")
     root1=Tk()
     root1.directory = filedialog.askdirectory()
     pathz.append(root1.directory)
     print("You have selected: ", root1.directory)
     print("What is the second file path you want to use:\n")
     root2=Tk()
     root2.directory = filedialog.askdirectory()
     pathz.append(root2.directory)
     print("You have selected: ",root2.directory)
     text = input("Do you want to remove square brackets? Y/N\n")
     if text == 'Y' or text == 'y':
          for path in pathz:
               files = os.listdir(path)
               pattern = r'\[[^\]]*\] '
               pattern2 = r' \[[^\]]*\]'
               pattern3 = r'\[[^\]]*\]'
               for name in files:
                    totalcount += 1
                    new_name = re.sub(pattern, r'', name)
                    new_name2 = re.sub(pattern2,r'',new_name)
                    new_name3 = re.sub(pattern3,r'',new_name2)
                    os.rename(os.path.join(path,name), os.path.join(path,new_name))
                    os.rename(os.path.join(path,new_name),os.path.join(path,new_name2))
                    os.rename(os.path.join(path,new_name2),os.path.join(path,new_name3))
     elif text == 'N' or text =='n':
          pass
     condition2 = input("Do you want to move the files? Y/N\n")
     if condition2 == 'Y' or condition2 == 'y':
          if len(pathz) == 1:
               pass

          for path in pathz:
               files = os.listdir(path)

               for name in files:     

                    if not name in namemoved:
                         currentcount+=1
                         print("Progress :", currentcount, "/", totalcount)
                         #if  moved == True:
                         #     print("Files are moving, do not close the window")
                         #     moved = False

                    for i in range(25,-1,-1):
                         letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                         Cletters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

                  

                         if name[0] == letters[i] or name[0] == Cletters[i]:
    
                                   if i > 13:
                                        targetpath = pathz[1]
                                        if os.path.join(targetpath,name) == os.path.join(path, name):

                                             continue
                                        else:
                                             shutil.move(os.path.join(path, name),targetpath)
                                             namemoved.append(name)
                                             moved = True
                                            
                              
                                   else:
                                        targetpath = pathz[0]
                                        if os.path.join(targetpath,name) == os.path.join(path,name):
                                             continue
                                        else:
                                             shutil.move(os.path.join(path, name),targetpath)
                                             namemoved.append(name)
                                             moved = True

                    if moved == True:
                         print("Files are moving, do not close the window")
                         moved = False
                    if len(namemoved) == 0:
                         print("Nothing needs to be moved!")
                         

     if condition2 == 'n' or condition2 == 'N':
          pass
                   
if __name__ == '__main__':
     main()
     input("Press ENTER to exit")     
