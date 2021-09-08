import os


class LogLoader:
    def __init__(self):
        self.uses_folder = not (input('Is the input a folder name? (Y/n)\n> ').upper() == 'N')
        self.content = ""
        if self.uses_folder:
            self.folder_name = input('Name of directory \n> ')
            for filename in os.listdir(self.folder_name):
                if filename.endswith(".log"):
                    with open(self.folder_name + '/' + filename, 'r', errors='ignore') as f:
                        print(f'[*] Loading {filename}', end='\r')
                        self.content += f.read()
                else:
                    continue
        else:
            self.file_name = input('Log name \n> ')
            with open(self.file_name, 'r') as f:
                self.content += f.read()
        #print(self.content)
