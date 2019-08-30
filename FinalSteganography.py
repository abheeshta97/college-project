# Python program implementing Image Steganography

# PIL module is used to extract
# pixels of image and modify it
from tkinter import filedialog

from PIL import Image
import creationANDopening as note

# Convert encoding data into 8-bit binary
# form using ASCII value of characters
def genData(data):
    # list of binary codes
    # of given data
    newd = []

    for i in data:
        newd.append(format(ord(i), '08b'))
    return newd


# Pixels are modified according to the
# 8-bit binary data and finally returned
def modPix(pix, data):
    datalist = genData(data)  # holding the data in binary format
    lendata = len(datalist)  # length of the data
    imdata = iter(pix)

    for i in range(lendata):

        # Extracting 3 pixels at a time
        pix = [value for value in imdata.__next__()[:3] +
               imdata.__next__()[:3] +
               imdata.__next__()[:3]]
        #print(pix)
        # Pixel value should be made
        # odd for 1 and even for 0
        for j in range(0, 8):

            if (datalist[i][j] == '0') and (pix[j] % 2 != 0):

                if (pix[j] % 2 != 0):
                    if (pix[j] == 0):
                        pix[j] = 2
                    pix[j] -= 1

            elif (datalist[i][j] == '1') and (pix[j] % 2 == 0):
                if (pix[j] == 0):
                    pix[j] = 2
                pix[j] -= 1

        # Eigh^th pixel of every set tells
        # whether to stop ot read further.
        # 0 means keep reading; 1 means the
        # message is over.
        if (i == lendata - 1):
            if (pix[-1] % 2 == 0):
                pix[-1] -= 1
        else:
            if (pix[-1] % 2 != 0):
                pix[-1] -= 1

        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]


def encode_enc(newimg, data):
    w = newimg.size[0]
    (x, y) = (0, 0)

    for pixel in modPix(newimg.getdata(), data):

        # Putting modified pixels in the new image
        newimg.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1
    return newimg


# Encode data into image
def encode(fileName,root):
    from tkinter import messagebox
    messagebox.showinfo("Information", "SELECT IMAGE TO BE ENCODED")
    img=note.selectImageFile(root)
    image = Image.open(img, 'r')

    f = open(fileName, "r")
    data = f.read()
    print(data)
    if (len(data) == 0):
        raise ValueError('Data is empty')

    newimg = image.copy()
    newimg1 = encode_enc(newimg, data)
    messagebox.showinfo("Information", "ENTER IN NAME FOR ENCODED IMAGE ")
    new_img_name =filedialog.asksaveasfilename(parent=None, title='Save As',  defaultextension='.png',filetypes=(("png file", ".png"), ("All files", "*")))
    print(new_img_name)
    newimg1.save(new_img_name)

    f.close()
    messagebox.showinfo("Information", "INSERTION MECHANISM COMPLETED.......")


# Decode the data in the image
def decode(img):

    image = Image.open(img, 'r')

    data = ''
    imgdata = iter(image.getdata())

    while (True):
        pixels = [value for value in imgdata.__next__()[:3] +
                  imgdata.__next__()[:3] +
                  imgdata.__next__()[:3]]

        # string of binary data
        binstr = ''

        for i in pixels[:8]:
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'

        data += chr(int(binstr, 2))
        if (pixels[-1] % 2 != 0):
            data=data.replace("â\x82\x84", "`")
            return data

        # Main Function

