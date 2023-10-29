import os
import shutil

fromdir ='C:/Users/nisha/Downloads'
todir ='C:/Users/nisha/OneDrive/Documents/docs_file'

list_of_files = os.listdir(fromdir)
print(list_of_files)

for i in list_of_files:
  os.path.splitext(list_of_files)