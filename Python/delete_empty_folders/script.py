import os
import sys

# enter path to the directory with the files
x = input('Absolute path of folder, from which empty subfolders are to be removed: ')

# check if path is valid
if not os.path.exists(x):
	print('Invalid path\nTerminating program')
	sys.exit()

# cleanup of empty subfolders
walk = list(os.walk('/home/naman/Desktop/del_folders/folder_struct'))

for path, folders, files in walk:
	if (len(folders) == 0) and (len(files) == 0):
		os.rmdir(path)
		print(f'Removed empty directory: {path}')
