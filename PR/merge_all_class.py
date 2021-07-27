# coding=utf-8
import os, shutil, glob

# 将单个txt检测文件按video划分
classes = ['baichunlu4', 'gaoyuanshanchun', 'lanmaji', 'malu', 'yang', 'zanghu', \
           'chihu', 'gaoyuantu', 'ma', 'maoniu', 'mashe2', 'xuebao', 'yanyang',
           'person4']  # person类别损坏，ma,gaoyuanshanchun（已经解决）文件读取问题

print(classes)
for j in classes[-1:]:
    base_path = '/apdcephfs/private_alisayfwu/ft_local/Tencent_WWF/PR/test/' + str(j) + '/'
    try:
        os.makedirs(base_path)
    except:
        pass
    for i in range(5, 8):
        catfile = '/apdcephfs/private_alisayfwu/ft_local/Tencent_WWF/exp/combine/taiji/' + str(j) + '/' + 'labels-0.'
        Txt = glob.glob(catfile + str(i) + '/' + '*.txt')
        print(Txt)
        try:
            os.makedirs(base_path + 'labels-0.' + str(i) + '/')
        except:
            pass
        for file_path in Txt:
            new_dir = file_path.split('-')[-2]
            repeated = new_dir.split('/')[-1]
            print(file_path)
            print(new_dir)
            print(repeated)
            fp = open(file_path, 'r')
            for line in fp:
                fq = open(base_path + 'labels-0.' + str(i) + '/' + repeated + '.txt', 'a')  # 这里用追加模式
                fq.write(line)
            fp.close()
            fq.close()
