# Detector

## Requirements
__None__

## Usage
To run the program, simply advance through your directories to where the detector.py script is located and enter:
```bash
python3 detector.py <PATH_TO_DIRECTORY>
```
In order to run the a test of the program, run the script <make_dirs.py>. This will create a new directory at the same location the script is located, and fill this directory with files.
After running the script, run the <detector.py> script with the path to the newly made directory.

## Contents
This script includes the functionality of: <br>
* new: Displays files found in the second directory path, which were not found in the first 
* sizes: Displays the size of all files which have copies, in bytes<br>
-find <EXTENSION>: Only runs the program on files which have the extension written by the user in <EXTENSION><br>
  
