import  os

#函数——得到源文件清单，含子文件夹，全路径
def get_file_list(file_path):
    file_list = os.walk(file_path)
    print(type(os.walk(file_path)))
    full_old_list = []
    for root,subdirs,files in file_list:
#        print(root)
#        print(subdirs)
#        print(files)
        if len(subdirs) != 0:
            for i in files:
                old_list = os.path.join(root, i)
                #print(old_list)
                full_old_list.append(old_list)
        else:
            for i in files:
                old_list = os.path.join(root, i)
                #print (old_list)
                full_old_list.append(old_list)
    return full_old_list

#函数——根据源文件清单，生成新文件清单
def rename_file(full_old_list):
    full_new_list = []
    for i in full_old_list:
        path_tmp = i.split("\\")[:-1]
        print(path_tmp)
        path_str = '\\'.join(path_tmp) + "\\"
        print(path_str)
        j = i.split("\\")[-1]
        print(j)
        j = j.split("(")[0]
        print(j)
        j = j.replace("][", "]|[")
        print(j)
        j = j.split("|")
        print(j)
        seq_temp = j.pop()
        print(seq_temp)
        print(j)
        j.insert(0, seq_temp)
        print(j)
        new_list = ''.join(j) + ".avi"
        print(new_list)
        new_list = path_str + new_list
        full_new_list.append(new_list)
    return full_new_list


if __name__ == '__main__':
    file_path = "C:\\Users\Administrator\Desktop\[迪士尼]"
    full_old_list = get_file_list(file_path)
    print(full_old_list)
    full_new_list = rename_file(full_old_list)
    print(full_new_list)
    for i,j in zip(full_old_list,full_new_list):
        os.rename(i, j)  # 重命名
