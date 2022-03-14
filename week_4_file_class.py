import tempfile
import os


class File:

    def __init__(self, path):
        self.path = path
        self._curr = 0
        if not os.path.exists(path):
            with open(path, 'x'):
                pass

    def get_file_name(self):
        return self.path.split('/')[-1]

    def __add__(self, obj):
        new_path = os.path.join(tempfile.gettempdir(
        ), self.get_file_name() + '.' + obj.get_file_name())
        with open(self.path, 'r') as f1, open(obj.path, 'r') as f2, open(new_path, 'w') as result_file:
            result_file.write(f1.read() + f2.read())
        return File(new_path)

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path, 'r') as f:
            f.seek(self._curr)
            line = f.readline()

            if line:
                self._curr = f.tell()
                return line
            else:
                self._curr = 0
                raise StopIteration

    def __str__(self):
        return self.path

    def read(self):
        with open(self.path, 'r') as f:
            return f.read()

    def write(self, text):
        with open(self.path, 'w') as f:
            return f.write(text)


if __name__ == '__main__':
    f = File('/home/clrsev_00/projects/abs')
    f2 = File('/home/clrsev_00/projects/a')
    print(f)
