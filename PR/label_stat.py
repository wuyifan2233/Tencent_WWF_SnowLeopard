#coding=utf-8
import os, shutil, glob
classes = ['baichunlu','chihu', 'gaoyuanshanchun','gaoyuantu','lanmaji', 'ma','malu', 'maoniu', \
'mashe','person','xuebao','yang', 'yanyang','zanghu']
# print(classes)
kongpai_list = ['baichunlu/00200','chihu/00015','chihu/00021','chihu/00097','chihu/00124','chihu/00234','chihu/00289', \
'gaoyuanshanchun/00058','gaoyuanshanchun/00067','gaoyuantu/00052','gaoyuantu/00063','gaoyuantu/00080', \
'lanmaji/00033','ma/00056','malu/00019','malu/00639','malu/00740','maoniu/00160','maomiu/00375','mashe/00006','mashe/00100', \
'mashe/00106','person/00109','person/00472','yang/00004', \
'zanghu/00028','zanghu/00030','zanghu/00058','zanghu/00085']
drop_kongpai = [19,14,18,17,19,19,17,18,17,18,20,19,20,16]

for j in classes:
    # print(classes)
    base_path= 'C:/Users/wuyifan/Desktop/label_stat/'+str(j)+'/'
    # print(base_path)
    try:
        os.makedirs(base_path)
    except:
        pass
    for i in range(1,8):
        catfile = 'C:/Users/wuyifan/Desktop/frames-all-combine/'+str(j)+'/'+'labels-0.'
        Txt = glob.glob(catfile+str(i)+'/'+ '*.txt')
        Txt.sort()
        print(Txt)
        try:
            os.makedirs(base_path+'labels-0.'+str(i)+'/')
        except:
            pass
        for file_path in Txt:
            print(file_path)
            new_dir = file_path.split('/')[-3]+'/'+file_path.split('/')[-1]
            repeated = new_dir.split('.')[-2]
            print(new_dir)
            print(repeated)
            if repeated not in kongpai_list:  # drop_kongpai
                print(repeated not in kongpai_list)
                f = open(file_path)
                line = f.readline()
                list1 = []
                while line:
                    a = line.split(' ')
                    b = a[0:1]
                    list1.append(b)
                    outlst = [' '.join([str(c) for c in lst]) for lst in list1]
                    video_class_label = list(set(outlst))
                    line = f.readline()
                with open (base_path+'labels-0.'+str(i)+'/'+str(j)+'.txt','a') as q:
                    q.write(str(file_path) + " " + " ".join([str(a) for a in video_class_label]) + '\n')
                f.close()

