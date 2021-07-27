# coding=utf-8
import sys
import os
import os, shutil, glob
import xlwt

# 计算PR等指标并打印，包括训练集每类的图片数量
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
training_image = ['1796', '358', '717', '770', '1524', '531', '1298', '2128', '1271', '1513', '4999', '2156', '1739', '585']
class_number = 14
weijianchu = [0] * class_number
file_line_num = [0] * class_number
TP = [0] * class_number
TP_FP = [0] * class_number
TP_FN = drop_kongpai


class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


path = os.path.abspath(os.path.dirname(__file__))
type = sys.getfilesystemencoding()  # 获取系统的当前编码格式
sys.stdout = Logger('v6-result.txt')

for i in range(1, 8):
    for index, value in enumerate(classes):
        # print(index,value)
        base_path = r'D:\program\tencent\PR_0726\0727label_stat/' + str(value) + '/'
        all_path = r'D:\program\tencent\PR_0726\0727label_stat/'
        Txt = glob.glob(base_path + 'labels-0.' + str(i) + '/' + '*.txt')

        for file_path in Txt:
            f = open(file_path)
            line = f.readline()
            line = line.strip('\n')
            while line:
                a = line.split(' ')
                b = a[1:]
                if str(index) in b:
                    TP[index] = TP[index] + 1
                    # print(TP)
                file_line_num[index] = file_line_num[index] + 1
                line = f.readline()
                line = line.strip('\n')

        All_flie_path = glob.glob(all_path + '*' + '/labels-0.' + str(i) + '/' + '*.txt')
        # print(All_flie_path)
        for all_file_path in All_flie_path:
            f2 = open(all_file_path)
            line2 = f2.readline()
            line2 = line2.strip('\n')
            while line2:
                a2 = line2.split(' ')
                b2 = a2[1:]
                # print(b2)
                if str(index) in b2:
                    TP_FP[index] = TP_FP[index] + 1
                line2 = f2.readline()
                line2 = line2.strip('\n')
                # print(TP_FP)
    recall = [float(a) / float(b) for a, b in zip(TP, TP_FN)]
    precision = [float(c) / float(d) for c, d in zip(TP, TP_FP)]
    weijianchu = [float(1) - (float(e) / float(f)) for e, f in zip(file_line_num, TP_FN)]

    pf2 = '%20s' + '%11.5g' * 3 + '%11s' * 2  # print format,保留3位有效位
    s2 = ('%20s' + '%11s' * 3 + '%11s' * 2) % ('classes', 'recall', 'precision', 'missing', 'videoNUM', 'TrainImg')
    print("This is the result based on confidence resulting at" + " threshold" + " 0." + str(i))
    print(s2)
    for i_w, c_w in enumerate(classes):
        print(
            pf2 % (classes[i_w], recall[i_w], precision[i_w], weijianchu[i_w], drop_kongpai[i_w], training_image[i_w]))
    weijianchu = [0] * class_number
    file_line_num = [0] * class_number
    TP = [0] * class_number
    TP_FP = [0] * class_number
    TP_FN = drop_kongpai
