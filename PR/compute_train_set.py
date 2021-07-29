#coding=utf-8
import os, shutil, glob
from collections import Counter

# 只计算训练集的图片个数打印，汇总训练集图片数的代码已经在v2_compute_PR.py里
# classes = ['baichunlu4','chihu', 'gaoyuanshanchun','gaoyuantu','lanmaji', 'ma','malu', 'maoniu', \
# 'mashe2','person4','xuebao','yang', 'yanyang','zanghu']
# print(classes)

class_number = 14
train_num = [0]*class_number
catfile = r'F:\0728differ\archive\val\labels/'
Txt = glob.glob(catfile + '*.txt')
count = []
for file_path in Txt:
    f = open(file_path)
    first_line = f.readline()
    print(first_line)
    a = first_line.split(' ')
    b = a[0]
    count.append(b)
    print(count)
    print(len(count))
sum = Counter(count)
print(sum)
