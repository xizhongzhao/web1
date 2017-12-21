#!/usr/bin/env python3
import os
import json

filename_list = os.listdir('./files')
def file_to_dict(file):
    with open(file,'r') as f:
        f_dict = json.loads(f.read())
    return f_dict

if __name__ == '__main__':
    file_dict_list = [ file_to_dict('./files/'+filename)  \
                   for filename in filename_list ]
    print(file_dict_list)
