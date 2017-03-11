# -*- coding: utf-8 -*-

import os
'''读文件'''
file_path = r'C:\Users\Administrator\Desktop\西部世界,Westworld 2016.txt'
print(file_path)

file_data = open(file_path,encoding= 'utf8').readlines()
print(file_data)

#文件下载来源，'ed2k'电驴下载
find_str = r'ed2k://'
#视频分辨率关键字
video_frame = r'1024X576'


ed2k_list_1 =[]
ed2k_list_2 =[]
ed2k_list_3 =[]

for i in file_data:
    if find_str in i:
        ed2k_list_1.append(i)

for i in ed2k_list_1:
    if video_frame in i:
        ed2k_list_2.append(i)

for i in ed2k_list_2:
    j = i.split(' ')
    m = j[1]
    m = m[6:]
    m = m[:-1]
#    print m
    ed2k_list_3.append(m)

target = open(r'C:\Users\Administrator\Desktop\2.txt', 'w')
for i in ed2k_list_3:
    target.write(i)
    target.write('\n')
target.close()


