import os

imageMagickPath = r'D:ImageMagick-6.2.7-Q16\convert.exe'   #ImageMagick安装目录下convert.exe所在目录
sourcePath = r'./'                          #png图片所在目录

def doStrip(path):
  data = {};
  print(path)
  for root, dirs, files in os.walk(path):
    for file in files:
      name = file.lower();
      if name.find('.png') != -1:
        print(file)
        path = os.path.join(root, file)
        os.system('"{0}" {1} -strip {1}'.format(imageMagickPath, path, path));


doStrip(sourcePath)
