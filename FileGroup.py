import os


class FileGroup:
    def __init__(self, abs_path: str, size_limit: int):
        os.makedirs(abs_path, exist_ok=True)
        self.abs_path = abs_path
        self.size_limit = size_limit

    @property
    def size(self):
        size = 0
        for file_name in os.listdir(self.abs_path):
            file_path = os.path.join(self.abs_path, file_name)
            size += os.path.getsize(file_path)
        return size

    @property
    def smallest_file(self):
        smallest_file = None
        for file_name in os.listdir(self.abs_path):
            file_path = os.path.join(self.abs_path, file_name)
            if not smallest_file:
                smallest_file = file_path
            elif os.path.getsize(smallest_file) > os.path.getsize(file_path):
                smallest_file = file_path
        return smallest_file

    @property
    def largest_file(self):
        largest_file = None
        for file_name in os.listdir(self.abs_path):
            file_path = os.path.join(self.abs_path, file_name)
            if not largest_file:
                largest_file = file_path
            elif os.path.getsize(largest_file) < os.path.getsize(file_path):
                largest_file = file_path
        return largest_file

    @property
    def files(self):
        files = []
        for file_name in os.listdir(self.abs_path):
            files.append(os.path.join(self.abs_path, file_name))
        return files

    def append(self, file_abspath):
        size = self.size
        size_of_new_file = os.path.getsize(file_abspath)
        if size_of_new_file + size > self.size_limit:
            raise ValueError('Size Limit break!\n FileGroup Size Limit: {size_limit}\n'
                             'FileGroup Size: {size}, Added File Size: {size_of_new_file}'
                             .format(size_limit=self.size_limit, size=size, size_of_new_file=size_of_new_file))
        file_name = file_abspath.split(os.path.sep)[-1]
        os.rename(file_abspath, os.path.join(self.abs_path, file_name))
