#https://stackoverflow.com/questions/16790328/open-multiple-filenames-in-tkinter-and-add-the-filesnames-to-a-list
#https://note.nkmk.me/en/python-pillow-concat-images/
#https://www.delftstack.com/howto/python/python-split-list-into-chunks/
import tkinter
import tkinter.filedialog as filedialog

root = tkinter.Tk()
files = filedialog.askopenfilenames(parent=root, title='Choose a file')
files = root.tk.splitlist(files)

from PIL import Image
import math

def get_concat_auto(im_list):
    rownum = math.sqrt(len(im_list))
    rownum = int(math.ceil(rownum))
    colnum = int(math.ceil(len(im_list)/rownum))
    final_list = lambda test_list, x: [test_list[i:i+x] for i in range(0, len(test_list), x)]
    imfinal_list = final_list(im_list,rownum)
    print(str(len(imfinal_list)) + str(len(imfinal_list[0])))
    
    im1 = Image.open(imfinal_list[0][0])
    output = Image.new('RGBA', (im1.width * rownum, im1.height * colnum), (0, 0, 0, 0))
    for y in range(len(imfinal_list)):
        for x in range(len(imfinal_list[y])):
            img = Image.open(imfinal_list[y][x])
            output.paste(img, (im1.width * x, im1.height * y))
    return output
    
des = filedialog.asksaveasfilename(defaultextension='.png', filetypes=[("PNG", "*.png")])
get_concat_auto(files).save(des)