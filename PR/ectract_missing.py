# coding=utf-8
import sys
import os, shutil, glob

# 提取所有missing视频
classes = ['baichunlu', 'chihu', 'gaoyuanshanchun', 'gaoyuantu', 'lanmaji', 'ma', 'malu', 'maoniu',
           'mashe', 'person', 'xuebao', 'yang', 'yanyang', 'zanghu']
kongpai_list = ['baichunlu/00200', 'chihu/00015', 'chihu/00021', 'chihu/00097', 'chihu/00124', 'chihu/00234',
                'chihu/00289',
                'gaoyuanshanchun/00058', 'gaoyuanshanchun/00067', 'gaoyuantu/00052', 'gaoyuantu/00063',
                'gaoyuantu/00080',
                'lanmaji/00033', 'ma/00056', 'malu/00019', 'malu/00639', 'malu/00740', 'maoniu/00160', 'maomiu/00375',
                'mashe/00006', 'mashe/00100',
                'mashe/00106', 'person/00109', 'person/00472', 'yang/00004',
                'zanghu/00028', 'zanghu/00030', 'zanghu/00058', 'zanghu/00085']
drop_kongpai = ['19', '14', '18', '17', '19', '19', '17', '18', '17', '18', '20', '19', '20', '16']

base_path = '/apdcephfs/private_alisayfwu/ft_local/Tencent_WWF/PR/0727label_stat/'
Txt = glob.glob(base_path + '/*/' + '/labels-0.2/' + '*.txt')
src_base = r'/apdcephfs/private_alisayfwu/ft_local/Tencent_WWF/data/video/'
dst_base = r'/apdcephfs/private_alisayfwu/ft_local/Tencent_WWF/data/missing_extract/'
jianchu_list = []
for file_path in Txt:
    # print(file_path)
    f = open(file_path)
    line = f.readline()
    line = line.strip('\n')
    while line:
        a = line.split(' ')
        c = str(a[0])
        new_dir = c.split('/')[-3] + '/' + c.split('/')[-1]
        repeated = new_dir.split('.')[-2]  # format: xuebao/00001
        # print(repeated)
        jianchu_list.append(str(repeated))
        line = f.readline()
        line = line.strip('\n')
# print(jianchu_list)

for j in classes:
    all_file = glob.glob(src_base + str(j) + '/' + '*')
    print(all_file)
    for file in all_file:
        print(file)
        new_dir_2 = file.split('/')[-2] + '/' + file.split('/')[-1]
        repeated_2 = new_dir_2.split('.')[-2]
        # print(repeated_2)
        if repeated_2 not in jianchu_list and repeated_2 not in kongpai_list:
            try:
                os.makedirs(dst_base + file.split('/')[-2])
            except:
                pass
            dst_path = str(dst_base + file.split('/')[-2] + '/')
            print(dst_path)
            shutil.copy(file, dst_path)