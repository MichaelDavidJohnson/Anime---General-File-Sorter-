import os
import re
import glob
import shutil
paths = [r'C:\Users\TeamKnowhow\Documents\File_Renaming\Test',r'C:\Users\TeamKnowhow\Documents\File_Renaming\Test2']
#Change paths to the anime folders

def main():
     for path in paths:
          files = os.listdir(path)
          pattern = r'\[[^\]]*\] '
          for name in files:
               #print(name)
               new_name = re.sub(pattern, r'', name)
               #print(new_name)
               os.rename(os.path.join(path,name), os.path.join(path,new_name))
               
     #for i in range(26):
          #if i < 14
     for path in paths:
          files = os.listdir(path)
          for name in files:     
               
               for i in range(25,-1,-1):
                    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                    Cletters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
               
                    
                    if name[0] == letters[i] or name[0] == Cletters[i]:
                         
                              if i > 13:
                                   targetpath = paths[1]
                                   if os.path.join(targetpath,name) == os.path.join(path, name):
                                        continue
                                   else:
                                        shutil.move(os.path.join(path, name),targetpath)
                              
                              else:
                                   targetpath = paths[0]
                                   if os.path.join(targetpath,name) == os.path.join(path,name):
                                        continue
                                   else:
                                        shutil.move(os.path.join(path, name),targetpath)
                    
                   
if __name__ == '__main__':
     main()
     
