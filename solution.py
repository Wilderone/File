import os
import tempfile
import random


class File:

    def __init__(self, path):
        self.count = -1
        self.path = path
        try:
            with open(self.path, 'r+') as p:
                self.file = p
        except FileNotFoundError:
            with open(self.path, 'w+') as p:
                self.file = p

    def __add__(self, other):
        with open(self.path, 'r') as concat:
            first = concat.read()
        # first = self.file.read()
        with open(str(other), 'r') as merger:
            second = merger.read()
        temp_str = first + second
        temp_dir = tempfile.gettempdir()
        new_path = os.path.join(temp_dir, f'new_file{random.randint(1,10)}.txt')
        # print(f'file created in {new_path}')
        result = File(new_path)
        result.write(temp_str)
        return result

    def __str__(self):
        return str(self.path)

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path, 'r+') as p:
            p.seek(0)
            file_li = p.readlines()
            end = len(file_li)
            if self.count >= end-1:
                raise StopIteration
            else:
                self.count += 1
                return file_li[self.count].rstrip()

    def read(self):
        with open(self.path, 'r+') as p:
            return p.read()

    def write(self, text):
        with open(self.path, 'w') as for_write:
            for_write.write(text)


