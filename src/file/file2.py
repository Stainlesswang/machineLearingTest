'''
Created on 2018年8月17日

@author: chinaso
'''

#!/bin/env python
# -*- coding:utf-8 -*-
 
def replace(file_path, old_str, new_str):
  try:
    f = open(file_path,'rw+')
    all_lines = f.readlines()
    f.seek(0)
    f.truncate()
    for line in all_lines:
      line = line.replace(old_str, new_str)
      f.write(line)
    f.close()
  except Exception as e:
    print(e)
 
if __name__ == "__main__":
  replace("C:\Users\chinaso\Desktop\allenWang1\controller\AllenWangController.java", "AllenWang", "YouGa")