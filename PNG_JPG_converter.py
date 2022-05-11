#!/usr/bin/env python
# coding: utf-8

# In[52]:


# Python program to convert png files to jpg files, and remove original png file

# !pip install Pillow
from PIL import Image
import os

def png_jpg_converter(fpath):
    
    path, f = os.path.split(fpath)
    fname, fextension = os.path.splitext(fpath)  
    f_jpg = fname+'.jpg'
    print(path, f)
    if fextension =='.png':
        
        img_png = Image.open(fpath, mode='r')
        rgb_img = img_png.convert('RGB')

        f_jpg = os.path.join(path, f_jpg)
        rgb_img.save(f_jpg)
        
        print(f'{f_jpg} has converted')
        
        
        # 有轉換後才把原本.png 刪除
        os.remove(fpath)     
        print(f'{fpath} has removed')


def main():
    target_dir = 'img'
    directory = os.path.join(os.getcwd(), target_dir) #'path/to/dir'
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f) and filename.endswith('.png'):
            print(f)        
            png_jpg_converter(f) 
            print()        
            
            
if __name__ == '__main__':
    main()


# In[50]:





# In[ ]:





# In[ ]:





# In[ ]:




