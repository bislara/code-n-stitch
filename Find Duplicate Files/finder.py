import os
import hashlib
from typing import Dict, List

result_file_name = 'results.txt'
separation_line = '___________________'


def find_duplicates(root_dir) -> Dict[str, List[str]]:
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


def export_results(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    print(separation_line)
    if len(results) > 0:
        print(
            f'Found {len(results)} duplications\n'
            f'The following files are identical, the name could differ, but the content is identical'
        )
        print(separation_line)
        for result in results:
            for file in result:
                print(f'\t{file}')
            print(separation_line)
        print(f'Results are saved to: {result_file_name}')
    else:
        print('No duplications found')


if __name__ == '__main__':
    path_to_scan = input('Enter path to check for duplicate files: ')
    duplicates = find_duplicates(path_to_scan)
    export_results(duplicates)
