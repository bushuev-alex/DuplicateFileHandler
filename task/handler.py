import os
import sys
import re
import hashlib


class FileHandler:
    def __init__(self, data):
        self.root = data[1]
        self.my_gen = os.walk(self.root)
        self.format = input("Enter file format:\n")
        self.sorted = None
        self.file_sorted_by_size = {}
        self.file_sorted_by_hash = {}
        self.duplicates = {}

    def walk(self):
        for path, folder, files in self.my_gen:
            for file in files:
                if re.match(rf".*\.{self.format}$", file) or re.match(rf"{self.format}", file):
                    full_path = ''.join([path, f'{os.sep}' + file])
                    size = int(f"{os.path.getsize(full_path)}")
                    new_dict = {size: [full_path]}
                    try:
                        self.file_sorted_by_size[size].append(full_path)
                    except KeyError:
                        self.file_sorted_by_size.update(new_dict)

    def sorting_option(self):
        print("Size sorting options:\n1. Descending\n2. Ascending")
        while True:
            choice = input("Enter a sorting option:\n")
            if choice == '1':
                self.sorted = True
                break
            elif choice == '2':
                self.sorted = False
                break
            else:
                print("Wrong option\n")
                continue

    def check_duplicates(self):
        print("Check for duplicates?")
        while True:
            choice = input()
            if choice in ['yes', 'Yes', 'y', 'YES']:
                self.get_hash()
                break
            elif choice in ['no', 'n', 'No', 'NO']:
                break
            else:
                print("Wrong option")

    def delete_choice(self):
        print("Delete files?")
        while True:
            choice = input()
            if choice in ['yes', 'Yes', 'y', 'YES']:
                self.n_to_delete()
                break
            elif choice in ['no', 'n', 'No', 'NO']:
                break
            else:
                print("Wrong option")

    def get_md5_sum(self, fname):
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as file:
            for chunk in iter(lambda: file.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def get_hash(self):
        for size, file_list in self.file_sorted_by_size.items():
            if len(file_list) >= 2:
                for file in file_list:
                    hash_ = self.get_md5_sum(file)
                    hash_dict = {hash_: [size, file]}
                    try:
                        self.file_sorted_by_hash[hash_].append(file)
                    except KeyError:
                        self.file_sorted_by_hash.update(hash_dict)

    def n_to_delete(self):
        while True:
            print("Enter file numbers to delete:\n")
            try:
                numbers = [int(x) for x in input().split()]
                if numbers != [] and set(numbers).issubset(set(self.duplicates)):
                    self.delete_files(numbers)
                    break
                else:
                    print("Wrong format")
            except ValueError:
                print("Wrong format")

    def delete_files(self, x):
        size = 0
        for number in x:
            path = self.duplicates[number][0]
            size += self.duplicates[number][1]
            os.remove(path)
        print(f"Total freed up space: {size} bytes")

    def result_by_size(self):
        for size_, file_list_ in sorted(self.file_sorted_by_size.items(), reverse=self.sorted):
            print(size_, 'bytes')
            print(*file_list_, sep='\n')
            print()

    def result_by_hash(self):
        n = 1
        prev_file_size = None
        for hash_, file_list in sorted(self.file_sorted_by_hash.items(),
                                       reverse=self.sorted, key=lambda element: element[1][0]):
            cur_file_size = file_list[0]
            if len(file_list) >= 3:
                if cur_file_size != prev_file_size:
                    print()
                    print(cur_file_size, 'bytes')  # file_list[0] = size
                print("Hash: " + hash_)
                for file in file_list[1:]:
                    duplicated_file = {n: [file, cur_file_size]}
                    self.duplicates.update(duplicated_file)
                    print(n, file, sep='. ')
                    n += 1
            prev_file_size = cur_file_size


def main():
    params = sys.argv
    try:
        my_handler = FileHandler(params)
        my_handler.sorting_option()
        my_handler.walk()
        my_handler.result_by_size()
        my_handler.check_duplicates()
        my_handler.result_by_hash()
        my_handler.delete_choice()
        my_handler.n_to_delete()
    except IndexError:
        print("Directory is not specified")


if __name__ == '__main__':
    main()
