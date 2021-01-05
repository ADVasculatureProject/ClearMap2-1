#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 18:41:29 2020

@author: athena-admin
"""

import os, re
import glob

folder_name = "/media/user/Daten 1/ADf_1.2.CX_P_hFTAA_SMA-Cy3_Pdxl-647"

os.chdir(folder_name)

files_channel1 = glob.glob('*.raw') + glob.glob('*.txt')

for file in files_channel1:
    
    new_filename = ''
    for t in file.split("_"):
        if re.match("^X[-+]?[0-9]+$", t):
            t = re.sub("^X", "", t)
            x = -int(int(t)/2500)
        elif re.match("^Y[-+]?[0-9]+$", t):
            t = re.sub("^Y", "", t)
            y = -int(int(t)/2500)
            tile_ID = '_[%02d x %02d]' % (y,x) # change dimensions
            new_filename += tile_ID
            
        else:
            if new_filename == '':
                new_filename = t
            else:
                new_filename += '_'+t
       # if x == None:
           # print("no x in '%s'" % folder_name)
        #if y == None:
           # print("no y in '%s'" % folder_name)
    
    new_filename = new_filename[:-11]+'.raw'
    
    os.rename(file, new_filename)