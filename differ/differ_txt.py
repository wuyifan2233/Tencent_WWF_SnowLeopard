import os
import glob
import shutil

# 找到image对应的label
differ_base_path = glob.glob(r'F:\0728differ\differ_file/'+'*')
txt_base_path = glob.glob(r'F:\0728differ\archive\val\labels/'+'*')
txt_save_path = r'F:\0728differ\differtxt/'
for file in differ_base_path:
    print(file)
    txt_name =file.split('\\')[-1].replace('jpg','txt')
    txt_path = str(r'F:\0728differ\archive\val\labels/')+str(txt_name)
    txt_path_glob = glob.glob(str(r'F:\\0728differ\\archive\\val\\labels\\')+str(txt_name))
    print(str(txt_path_glob))
    print(txt_path)
    # print(txt_base_path)
    if txt_path_glob in txt_base_path:
        print(1)
        shutil.copy(txt_path, txt_save_path)
    break