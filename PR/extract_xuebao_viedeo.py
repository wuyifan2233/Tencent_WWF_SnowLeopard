# coding=utf-8
import sys
import os
import os, shutil, glob
import xlwt
import shutil

# 提取所有检出雪豹的视频
classes = ['baichunlu4', 'chihu', 'gaoyuanshanchun', 'gaoyuantu', 'lanmaji', 'ma', 'malu', 'maoniu',
           'mashe2', 'person4', 'xuebao', 'yang', 'yanyang', 'zanghu']
kongpai_list = ['baichunlu4/00200', 'chihu/00015', 'chihu/00021', 'chihu/00097', 'chihu/00124', 'chihu/00234',
                'chihu/00289',
                'gaoyuanshanchun/00058', 'gaoyuanshanchun/00067', 'gaoyuantu/00052', 'gaoyuantu/00063',
                'gaoyuantu/00080',
                'lanmaji/00033', 'ma/00056', 'malu/00019', 'malu/00639', 'malu/00740', 'maoniu/00160', 'maomiu/00375',
                'mashe2/00006', 'mashe2/00100',
                'mashe2/00106', 'person4/00109', 'person4/00472', 'yang/00004',
                'zanghu/00028', 'zanghu/00030', 'zanghu/00058', 'zanghu/00085']
drop_kongpai = ['19', '14', '18', '17', '19', '19', '17', '18', '17', '18', '20', '19', '20', '16']

base_path = 'D:/program/tencent/PR/drop_stat/'
Txt = glob.glob(base_path + '/*/' + '/labels-0.2/' + '*.txt')
src_base = r'E:\WWF/'
dst_base = r'E:\xuebao_extact/'
for file_path in Txt:
    print(file_path)
    f = open(file_path)
    line = f.readline()
    line = line.strip('\n')
    while line:
        a = line.split(' ')
        b = a[1:]
        c = str(a[0])
        if str(10) in b:
            new_dir = c.split('/')[-3] + '/' + c.split('/')[-1]
            repeated = new_dir.split('.')[-2]  # format: xuebao/00001
            print(repeated)
            try:
                os.makedirs(dst_base + c.split('/')[-3])
            except:
                pass
            src_file = str(glob.glob(src_base + repeated + '.*')[0])
            print(src_file)
            dst_path = str(dst_base + c.split('/')[-3] + '/')
            print(dst_path)
            # print(TP)
            shutil.copy(src_file, dst_path)
        line = f.readline()
        line = line.strip('\n')
