import os
import zipfile
import requests


class FileFromWeb:

    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file

    def __enter__(self):
        # download
        response = requests.get(self.url)
        with open(self.tmp_file, 'wb') as f:
            f.write(response.content)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == FileNotFoundError:
            print(f'Error {exc_val}')
            return False # if false error will be shown
        elif exc_type == KeyError:
            print(f'Error {exc_val}')
            return False
        else:
            return True # rest of erros will be hidden


with FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', 'c:/temp/euroxref.zip') as f:
    with zipfile.ZipFile(f.tmp_file, 'r') as z:
        a_file = z.namelist()[0]
        print(a_file)
        os.chdir('c:/temp')
        z.extract(a_file, '.', None)