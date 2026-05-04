




from datetime import datetime
import os
import shutil
from ftplib import FTP
import ftplib
import socket

switching_box2 = []

switching_box = []

def re_run():
 print("please insert folder path for good files")
 while True:
  good_folder = input().replace('"', '')
  try:
   if not os.path.isdir(good_folder):
    raise FileNotFoundError(f"Folder not found: {good_folder}")
  except FileNotFoundError:
   print("please input valid file path")
  else:
    switching_box.append(good_folder)
    break  
  
 print(f"{good_folder} valid file path")
 return good_folder 
re_run()

def re_run2():
 print("please insert folder path for bad files")
 while True:
  bad_folder = input().replace('"', '')
  try:
     if not os.path.isdir(bad_folder):
      raise FileNotFoundError(f"Folder not found: {bad_folder}")
  except FileNotFoundError:
     print("please input valid file path")
  else:
     switching_box2.append(bad_folder)
     break
   
 return bad_folder 
re_run2()


while True:
 if switching_box  ==  switching_box2:
  switching_box.clear()
  switching_box2.clear()
  print("good and bad path cannot be the same")
  re_run()
  re_run2()
 else:
  print("all folder paths are valid")
  all_good_paths = switching_box
  break
 
 path_one = switching_box[0]

 path_two = switching_box2[0]




