import hashlib, os, json, sys, shutil


dict = {}
sizes = {}
diff_files = {}


def main():
    run(sys.argv)


def loop_through_dir(path, find, find_ext):
    """
        Arguments(String path): The path leading to the directory the user wishes to read through

        Description: This method loops through all files in the given directory, as well as all the files within the sub directory.
        The method then hashed said files as hex digits, this is done so that the json.dumps() may use the hashed files.
        The hashed files are then stored within a dictionary.
        This method does not return anything, but rather writes to the global dictionary 'dict'.
    """
    for sub_d, directory, files in os.walk(path):
        for file in files:
            if(find and not file.endswith(find_ext)):
                pass
            else:
                if(not (path in diff_files.items())):
                    diff_files[path] = [file]
                else:
                    diff_files[path].append(file)
                hash_file = hashlib.sha256()
                read_size = 8096
                this_path = os.path.join(sub_d, file)
                sizes[file] = os.path.getsize(this_path)
                with open(this_path, 'rb') as fi:
                    file_block = fi.read(read_size)
                    while(len(file_block) > 0):
                        hash_file.update(file_block)
                        file_block = fi.read(read_size)
                if file in dict:
                    file = sub_d.split("/")[len(sub_d.split("/"))-1]+"/"+file
                if(hash_file.hexdigest() in dict):
                    dict[hash_file.hexdigest()].append(file)
                else:
                    dict[hash_file.hexdigest()] = [file]
                dict[file] = hash_file.hexdigest()

def run(inputs):
    size = False
    new = False
    find = False
    find_ext = ""
    path = ""
    if(len(inputs) < 2):
        print("Please enter a path to a directory:\n\"python3 detector.py <PATH_TO_DIRECTORY>\"")
        sys.exit(0)
    if("--sizes" in inputs):
        size = True
        inputs.remove("--sizes")
    if("--new" in inputs):
        new = True
        inputs.remove("--new")
    if("--find" in inputs):
        find = True
        find_ext = inputs[inputs.index("--find")+1]
        inputs.remove("--find")
        inputs.remove(find_ext)
    paths = inputs[1:]

    for path in paths:
        if(not os.path.isdir(path)):
            print("The given path is not valid. Please enter a valid directory path.")
            print(path)
            sys.exit(0)
        else:
            loop_through_dir(path, find, find_ext)
    dupe_dict = {}
    found = False
    json_d = {}
    for keys, values in dict.items():
        if (len(values) > 1 and isinstance(values, list)):
            found = True
            json_d[keys] = values
            print("\nFound", len(values)-1, "file(s) identical to", values[0])
            for val in values:
                json_d[val] = [keys]
                print(val, "= ", end = '')
            print(keys)
            if size:
                print("Size:", sizes[values[0].split("/")[len(values[0].split("/"))-1]], "Bytes\n")

    if(not found):
        print("Found no duplicates")
    else:
        with open('meta.json', 'w') as fp:
            json.dump(json_d, fp, indent=2)

    if(new and len(diff_files) > 1):
        org = diff_files[list(diff_files.keys())[0]]
        for x in range(1, len(diff_files)):
            for y in diff_files[list(diff_files.keys())[x]]:
                if(not y in org):
                    print(y, "in", list(diff_files.keys())[x], "is new (not found in", list(diff_files.keys())[0] + ")")
                    org.append(y)


main()
