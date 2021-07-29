import os
import glob
import shutil
for filepath,dirnames,filenames in os.walk(r'F:\0728differ\archive\val\images'):
    # print (filenames)
    pass
for filepath1,dirnames2,filenames2 in os.walk(r'F:\0728differ\valset-images\images'):
    # print (filenames2)
    pass
z = set(filenames).difference(set(filenames2))
z = list(z)
dst_path = r"F:\0728differ\differ_file/"
print(z)
print(len(z))
differ_path = glob.glob(r'F:\0728differ\archive\val\images/'+'*')
for file in differ_path:
    print(file)
    differ_file =file.split('\\')[-1]
    print(differ_file)
    txt = str(r'F:\0728differ\archive\val\labels/')+file.split('\\')[-1].replace('jpg','txt')
    if differ_file in z:
        print(1)
        shutil.copy(txt, dst_path)
# if differ_file in
# print(len(differ_file))

# 找到image对应的label
differ_base_path = glob.glob(r'F:\0728differ\differ_file/'+'*')
for file in differ_path:
    print(file)
    differ_file =file.split('\\')[-1]
    print(differ_file)
    if differ_file in z:
        print(1)
        shutil.copy(file, dst_path)