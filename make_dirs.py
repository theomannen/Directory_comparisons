import hashlib, os, json, sys, shutil

def make_dirs():
    """
        This script makes new directories.
    """
    d = Detector()
    path = os.path.realpath(__file__)
    list_dir_path = path.split("/")[:len(path.split("/"))-1]
    list_dir_path.remove(list_dir_path[0])
    full_path = ""
    for dir in list_dir_path:
        full_path = full_path+"/"+dir
    full_path = os.path.join(full_path, "test_dir")
    if(not os.path.exists(full_path)):
        os.mkdir(full_path)
    for x in range(3):
        with open(os.path.join(full_path, "cpy_file"+str(x))+".txt", 'w') as file:
            file.write("this file will be equal to two other files")
    for x in range(2):
        with open(os.path.join(full_path, "python_cpy_file"+str(x))+".py", 'w') as file:
            file.write("#this file will be equal to one other files")
    with open(os.path.join(full_path, "random_file"+str(x))+".md", 'w') as file:
        file.write("#this file will be equal to no other files")



make_dirs()
