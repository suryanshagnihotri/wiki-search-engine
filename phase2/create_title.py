# multilevel indexing
import os
index_path = ('./Title/doc_title.txt')

f = open(os.path.abspath(index_path))
path = './Title/Split/'
count = 1
temp_list = []
store_index = []
with open(os.path.abspath(index_path)) as f1:
    for line in f1:
        if(count%500 == 0):
            name = path + str(count/500)
            out = open(os.path.abspath(name),"w")
            for i in temp_list:
                out.write(i)
            store_index.append(temp_list[0][:-1].split()[0] + ' ' + str(count/500) + '\n')
            temp_list = []
        temp_list.append(line)
        count += 1
if(len(temp_list)!=0):
    name = path + str((count/500)+1)
    out = open(os.path.abspath(name),"w")
    for i in temp_list:
        out.write(i)
    store_index.append(temp_list[0][:-1].split()[0] + ' ' + str((count/500)+1) + '\n')
    temp_list = []

indexno = 0
while(len(store_index) > 200):
    store_top = []
    temp_index = []
    count = 1
    for i in store_index:
        if(count%200 == 0):
            store_top.append(temp_index[0][:-1].split()[0] + ' ' + str(count/200) + '\n')
            name = path + str(indexno) + str(count/200)
            out = open(os.path.abspath(name),"w")
            for j in temp_index:
                out.write(j)
            temp_index = []
        temp_index.append(i)
        count += 1
    if(len(temp_index)!=0):
        store_top.append(temp_index[0][:-1].split()[0] + ' ' + str((count/200)+1) + '\n')
        name = path + str(indexno) + str((count/200)+1)
        out = open(os.path.abspath(name),"w")
        for j in temp_index:
            out.write(j)
        temp_index = []
    indexno+=1
    store_index = store_top

name = path + 'main'
out = open(os.path.abspath(name),"w")
for i in store_index:
    out.write(i)
    count += 1