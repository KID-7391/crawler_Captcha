#coding=utf8
import os

s = []
file_name = os.listdir('data')
for i in file_name:
    file_data = open('data/' + i)
    s.append(file_data.read())

s = list(set(s))
print(len(s))
for idx, i in enumerate(s):
    file_output = open('useful_data/' + str(idx), 'w+')
    file_output.write(i)
    file_output.close()


