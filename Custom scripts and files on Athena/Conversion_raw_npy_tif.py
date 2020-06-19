#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 21:12:35 2020

@author: Peter Rupprecht
"""

## convert from raw to npy

# fileList_channel1 = ws.file_list('raw', extension='raw')
# for file in fileList_channel1:
#     a = np.memmap(file,dtype="<i2",mode='r', shape =(2048,2048,3499),order='F')
#     np.save(file[:-4]+'.npy', a)

# fileList_channel2 = ws.file_list('arteries', extension='raw')
# for file in fileList_channel2:
#     a = np.memmap(file,dtype="<i2",mode='r', shape =(2048,2048,3499),order='F')
#     np.save(file[:-4]+'.npy', a)


## convert from npy to tif


input_filename = '/media/athena-admin/disk12_1/raw/osfstorage/Brain-39L/excerpt4x4_renamed/14-16-41_tricocktail_UltraII[01 x 01]_C00_UltraII Filter0000.ome.npy'

input_filename = '/media/athena-admin/disk12_1/raw/osfstorage/Brain-39L/binary_filled_debug.npy'

from ClearMap.Environment import io
io.convert_files(input_filename, extension='tif', processes=12, verbose=True);






