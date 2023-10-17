import pandas as pd

#读入文件
data = pd.read_excel('shuju.xlsx')
data['year'] = data['type'].apply(lambda x:x.split('/')[0].strip())
#取出表格中type这一列的元素命名为x，将x按’/‘分割，取出分割的第一个命名为year，取出两边空格
data['c'] = data['type'].apply(lambda x:x.split('/')[1].strip())
data['t'] = data['type'].apply(lambda x:x.split('/')[2].strip())

#根据年限分割
for i in data['year'].unique():
    data[data['year'] == i].to_excel(writer, sheet_name=i)

#根据类型分割
type_list = set(z for i in data['t'] for z in i.split(' '))
"""
相当于：
type_list = []
for i in data['t‘]:
    for z in i.split(' '):
        type_list.append(z)
set(type_list)
"""
for ty in type_list:
    data[data['t'].str.contains(ty)].to_excel(writer,sheet_name=ty)
writer.close()