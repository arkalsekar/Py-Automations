import os
import sys 
import collections 
import shutil
import argparse

# Creating Argument Parser
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--input', type=str, help="Input Directory", required=False)
ap.add_argument("-o", "--output", type=str, help="Output Directory", required=False)
arg = vars(ap.parse_args())

a = 'C://Users//sulta_000//Downloads'
# ab = os.listdir(arg['input'])
ab = os.listdir(a)

basedir = arg['output']
if os.path.isdir(arg['output']):
    print("Directory Already Exists")
else:
    print("Creating Directorys")
    basedir = arg['output']
    basedire = os.mkdir(arg['output'])      
    print('Created PNG')
    direcr = os.mkdir(os.path.join(basedir, 'png'))
    print("Created JPG")
    os.mkdir(os.path.join(basedir, 'jpg'))
    print("Created PDF")
    os.mkdir(os.path.join(basedir, 'pdf'))
    print('Created EXE')
    os.mkdir(os.path.join(basedir, 'exe'))

# print(ab)
for filename in ab:
    print(filename)
    if filename.endswith('.jpg, ,jpeg'):
        print(filename)
        shutil.copy2(filename, os.path.join(basedir, 'jpg'))
    # elif filename.endswith('.png'):
    #     shutil.copy2(filename, os.path.join(basedir, 'png'))
    elif filename.endswith('.csv'):
        shutil.copy2(filename, os.path.join(basedir, 'pdf'))

    # filename, ext = os.path.splitext(filename)
    # ext  = ext[1:]

