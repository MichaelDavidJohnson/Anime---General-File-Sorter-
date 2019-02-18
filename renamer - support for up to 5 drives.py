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
     words = ["first","second","third","fourth","fifth"]
     temp = input("How many directories do you want to use?\n")
     counter = -1
     numb = int(temp[0])
     alphabetstorage = []
     alphabetstorage.append(0)
     for i in range(numb):
                  print("What is the",words[i],"file path you want to use?:\n")
                  root = Tk()
                  root.directory = filedialog.askdirectory()
                  pathz.append(root.directory)
                  print("You have selected: ",root.directory)

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
          if text == 'n' or text == 'N':
               if len(pathz) == 1:
                    pass
               for i in range(1,numb+1):
                    j = (26//numb)*i
                    alphabetstorage.append(j)
               for path in pathz:
                    files = os.listdir(path)
                    for name in files:
                         totalcount += 1
               for path in pathz:
                    files = os.listdir(path)
                    for name in files:
                         
                         pattern = r'\[[^\]]*\] '
                         pattern2 = r' \[[^\]]*\]'
                         pattern3 = r'\[[^\]]*\]'
                         tempname = str(name)
                         tempname = re.sub(pattern,r'',tempname)
                         tempname = re.sub(pattern2,r'',tempname)
                         tempname = re.sub(pattern3,r'',tempname)
                         
                         if not name in namemoved:
                              currentcount += 1
                              print("Progress :", currentcount,"/",totalcount)
                         for _ in range(0,26,1):
                              letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                              Cletters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
                              for lol in range(0,len(alphabetstorage)-1):
                                   if tempname[0] == letters[_] or tempname[0] == Cletters[_]:
                                        if _ in range(alphabetstorage[lol],alphabetstorage[lol+1]):
                                             targetpath = pathz[lol]
                                             if os.path.join(targetpath,name) == os.path.join(path,name):
                                                  pass
                                             else:
                                                  if os.path.isdir(os.path.join(path,name)):
                                                       shutil.move(os.path.join(path,name),os.path.join(targetpath,name))
                                                       namemoved.append(name)
                                                  
                                                       moved = True
                                                  else:
                                                       shutil.copy(os.path.join(path,name),os.path.join(targetpath,name))
                                                       os.remove(os.path.join(path,name))
                                                       namemoved.append(name)
                                                       moved =  True
                                             if moved == True:
                                                  print("Files are moving, do not close the window")
                                                  moved = False
                                             if len(namemoved) == 0:
                                                  print("Nothing needs to be moved!")

                                   
          else:
               if len(pathz) == 1:
                    pass
               for i in range(1,numb+1):
                                      
                    j = (26//numb) * i
                    alphabetstorage.append(j)
               for path in pathz:
                    files = os.listdir(path)
                    for name in files:
                         if not name in namemoved:
                              currentcount += 1
                              print("Progress :",currentcount,"/",totalcount)
                         for _ in range(0,26,1):
                              letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                              Cletters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
                    
                              for lol in range(0,len(alphabetstorage)-1):
                                   if name[0] == letters[_] or name[0] == Cletters[_]:
                                        if  _  in range(alphabetstorage[lol],alphabetstorage[lol+1]):
                                             targetpath = pathz[lol]
                                             if os.path.join(targetpath,name) == os.path.join(path, name):
                                                  pass
                                             else:
                                                  if os.path.isdir(os.path.join(path,name)):
                                                       shutil.move(os.path.join(path,name),os.path.join(targetpath,name))
                                                       namemoved.append(name)
                                                  
                                                       moved = True
                                                  else:
                                                       shutil.copy(os.path.join(path,name),os.path.join(targetpath,name))
                                                       os.remove(os.path.join(path,name))
                                                       namemoved.append(name)
                                                       moved =  True
                                                  
                                             if moved == True:
                                                  print("Files are moving, do not close the window")
                                                  moved = False
                                             if len(namemoved) == 0:
                                                  print("Nothing needs to be moved!")
                         if name[0] == 'z' or name [0] == 'Z':
                              targetpath = pathz[len(alphabetstorage)-2]
                              if os.path.join(targetpath,name) == os.path.join(path, name):
                                   pass
                              else:
                                   if os.path.isdir(os.path.join(path,name)):
                                        shutil.move(os.path.join(path,name),os.path.join(targetpath,name))
                                        namemoved.append(name)
                                   
                                        moved = True
                                   else:
                                        shutil.copy(os.path.join(path,name),os.path.join(targetpath,name))
                                        os.remove(os.path.join(path,name))
                                        namemoved.append(name)
                                        moved =  True
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
