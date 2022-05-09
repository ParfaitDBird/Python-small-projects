import sys
import os
from PIL import Image,ImageFile
'''
rootdir = 'C:/Users/sid/Desktop/test'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        print(os.path.join(subdir, file))



def conversion(new_path):
    for subdir, dirs, files in os.walk(new_path):
        for file in files:
            if(subdir==new_path):
                print(file)
                print(f'new path: {new_path}')
                im = Image.open(os.path.join(subdir, file))
  '''
'''
def Lopeo(path,new_path):
    for subdir, dirs, files in os.walk(path):
        for file in files:
            if(subdir==path):
                print(file)
                clean_name = os.path.splitext(file)[0]
                img = Image.open(file)
                # added the / in case user doesn't enter it. You may want to check for this and add or remover it.
                img.save(f'{new_folder}/{clean_name}.png', 'png')
                #copy2(os.path.join(subdir, file),nuevo_path)
#grab the arguments from console (1st folder name\ 2nd new folder )
'''

og_folder = str(sys.argv[1])
new_folder = str(sys.argv[2])
# Parent Directory path
parent_dir = rf"D:\Users\Lietail\Code\Scripting\venv\{og_folder}"
# Create the directory
print(og_folder)
nuevo_path = os.path.join(parent_dir, new_folder)
try:
    os.makedirs(nuevo_path)
    print(f'folder: {new_folder} created!')
except OSError as error:
    print(nuevo_path)
    print('Directory already created lmao!')

    #Lopeo(og_folder,new_folder)

for filename in os.listdir(parent_dir):
    clean_name = os.path.splitext(filename)[0]
    print(clean_name)
    if(filename!=new_folder):
        img = Image.open(rf'{parent_dir}\{filename}')
        #added the / in case user doesn't enter it. You may want to check for this and add or remover it.
        img.save(rf'{nuevo_path}\{clean_name}.png', 'png')
        print('all done!')
    else:
        pass


#save them to new folder