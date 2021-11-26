import requests
import os
import shutil # this module allows to copy from file to other file


def save_url_to_file(url, file_path):
    r = requests.get(url, stream=True)
    with open(file_path, "wb") as f:
        f.write(r.content)


url = 'http://www.mobilo24.eu/spis/'
dir = r'C:\Users\maxym\Desktop\Python\Basic\Obsluga_Bledow'
tmpfile = 'download.tmp'
file = 'spis.html'

tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)

print(tmpfile_path)

try:
    if os.path.isfile(tmpfile):
        print('File exsist, deleting file..')
        os.remove(tmpfile)

    print(f'Downloading URL {url}')
    save_url_to_file(url, tmpfile_path)

    print(f'Coping file {tmpfile_path}, {file_path}')
    shutil.copy(tmpfile_path,file_path)

except Exception as e :
    print(f'Error : \nDetails: \n {e} ')

else:
    print(f'URL succesfully downloaded {file}')
finally:
    if os.path.exists(tmpfile_path):
        print('Final removal of the file {}'.format(tmpfile_path))
        os.remove(tmpfile_path)
    print('DONE!')
