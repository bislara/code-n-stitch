import os
import hashlib


result_file_name = 'results.txt'
separation_line = '___________________'


def find_duplicates(root_dir):
    files = {}
    for dir_name, _, file_list in os.walk(root_dir):
        print(f'Scanning folder: {dir_name}')
        for filename in file_list:
            path = os.path.join(dir_name, filename)
            file_hash = calculate_hash(path)
            if file_hash in files:
                files[file_hash].append(path)  # append duplication
            else:
                files[file_hash] = [path]  # add new file
    return files


def calculate_hash(path):
    hasher = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


if __name__ == '__main__':
    path_to_scan = input('Enter path to check for duplicate files: ')
    find_duplicates(path_to_scan)
