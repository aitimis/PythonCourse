class MyFile:
    def __enter__(self):
        self.file = open("file1", "a")
        return self

    def read_python_code(self):
        indent = 0
        x = input('>>> ')
        self.file.write(x + "\n")
        if x[-1] == ':':
            indent += 1
        while x != '' or indent:
            if indent == 0:
                x = input('>>> ')
            else:
                x = input('...' + '    ' * indent)
            self.file.write("    " * indent + x + "\n")
            if x == '':
                if indent > 0:
                    indent -= 1
            elif x[-1] == ':':
                indent += 1

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.write(str(exc_tb.tb_frame))
        self.file.close()
        return True

if __name__ == '__main__':
    with MyFile() as my_file:
        my_file.read_python_code()
        my_file.read_python_code()