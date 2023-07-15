import zipfile, os, sys

# Get folder path and zip name
folder_path = sys.argv[1]
zip_name = sys.argv[2]

# Zip function
def zipDir(path, zipname):
    zipf = zipfile.ZipFile(f"{zipname}.zip", 'w', zipfile.ZIP_DEFLATED)
    abs_src = os.path.abspath(path)
    for root, dirs, files in os.walk(path):
        for file in files:
            absname = os.path.abspath(os.path.join(root,file))
            arcname = absname[len(abs_src)+1:]
            zipf.write(absname,arcname=arcname)
    zipf.close()

# Zip the files
zipDir(folder_path,zip_name)