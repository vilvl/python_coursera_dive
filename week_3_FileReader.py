class FileReader:

    def __init__(self, file_path) -> None:
        self.file_path = file_path

    def read(self):
        try:
            with open(self.file_path, 'r') as f:
                return f.read()
        except IOError:
            return ''


