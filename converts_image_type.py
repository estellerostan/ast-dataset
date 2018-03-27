from PIL import Image
import glob


for filename in glob.glob('/home/deeplearning/Pictures/*.gif'):
    img = Image.open(filename)
    img.save(filename.split('.')[0], 'png')

for filename in glob.glob('/home/deeplearning/Pictures/*.jpg'):
    img = Image.open(filename)
    img.save(filename, 'png')


# TODO: os.remove(path, *, dir_fd=None) après
# ou shutil.rmtree(path, ignore_errors=False, onerror=None)
