import subprocess
import os
import shutil
import re
import glob


def gen():
    file = open("prokaryotes.csv", "r")
    file.readline()
    for line in file:
        cmd = "wget -r -nd -P"
        line2List = line.split(",")
        directory = line2List[5]
        directory = directory[1:len(directory)-1]
        url = line2List[len(line2List)-1]
        url = url[1:len(url)-2]
        cmd += " "+directory+" " + url
        subprocess.call(cmd, shell=True)


def copy_rename():
    #get all directories names
    Alldirectories = glob.glob("*.1")
    Alldirectories += glob.glob("*69")

    regex1 = r".*\_protein\.faa\.gz"
    dst_dir = os.path.join(os.curdir , "proteins")  
    AllFiles2 =[]
    AllFiles = glob.glob('**/*.faa.gz')

    for file in AllFiles: 
        if re.search(regex1, file):
                AllFiles2.append(file)

    for i in range(0,10):
        src_file = os.path.join(os.curdir, AllFiles2[i])
        shutil.copy(src_file,dst_dir)
        print(str(i)+" copy file to proteins...")

    file_names_path = glob.glob("proteins/*.gz")
    file_names = []
    for name in file_names_path:
        name = name[9:24]
        file_names.append(name)

    for i in range(0,10):
        dst_file = file_names_path[i]
        new_dst_file_name = os.path.join(dst_dir, file_names[i])
        print("rename "+ file_names_path[i]+ " to "+ file_names[i])
        os.rename(dst_file, new_dst_file_name)
    print("Copy and rename done.")

#gen()    
if glob.glob("proteins") == []:
    subprocess.call("mkdir proteins", shell= True)
    print("starting copy and rename...")
    copy_rename()
    
else:
    subprocess.call("rm -r proteins", shell= True)
    subprocess.call("mkdir proteins", shell= True)
    print("starting copy and rename...")
    copy_rename()
    