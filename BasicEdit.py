#Tushar Tyagi
#10/11/2018

#!/usr/bin/env python3

import tkinter
import tkinter.messagebox as tkMessageBox
from tkinter.filedialog import *
from PIL import Image, ImageEnhance

imgpath=""
img=0;

def main():

    def openImg():
        #root = tkinter.Tk()
        filename = tkinter.filedialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("jpg files","*.jpg*"),("jpeg files","*.jpeg"),("png files","*.png*")))
        global imgpath
        global img
        imgpath = filename
        img = Image.open(imgpath)
        messagebox.showinfo("Information","Showing original image.\nClose image to proceed!")
        img.show()

    def editB():
        if imgpath=="":
            messagebox.showerror("Error","Open image first")
        else:
            top.destroy()



    top = tkinter.Tk()
    B2 = tkinter.Button(top, activebackground='blue' , padx=2, pady=2, text ="Choose Editing Options",command= editB)
    B = tkinter.Button(top, activebackground='blue' , padx=2, pady=2, text ="Open Image", command = openImg)

    B.pack()
    B2.pack()
    top.mainloop()

    top = tkinter.Tk()
    CheckVar1 = IntVar()
    CheckVar2 = IntVar()
    CheckVar3 = IntVar()
    CheckVar5 = IntVar()
    CheckVar6 = IntVar()
    C1 = Checkbutton(top, text = "Sharpen", variable = CheckVar1, \
                     onvalue = 1, offvalue = 0, height=5, \
                     width = 20)
    C2 = Checkbutton(top, text = "De-Sharpen", variable = CheckVar2, \
                     onvalue = 1, offvalue = 0, height=5, \
                     width = 20)
    C3 = Checkbutton(top, text = "Decrease Brightness", variable = CheckVar3, \
                     onvalue = 1, offvalue = 0, height=5, \
                     width = 20)
    C5 = Checkbutton(top, text = "Black and White", variable = CheckVar5, \
                     onvalue = 1, offvalue = 0, height=5, \
                     width = 20)
    C6 = Checkbutton(top, text = "Decrease Colours", variable = CheckVar6, \
                     onvalue = 1, offvalue = 0, height=5, \
                     width = 20)

    B3 = tkinter.Button(top, activebackground='green' , padx=2, pady=2, text ="OK",command = top.destroy)

    C1.pack()
    C2.pack()
    C3.pack()
    C5.pack()
    C6.pack()
    B3.pack()
    top.mainloop()

    global img
    image = img
    if (CheckVar1.get()==1):
        enhancer=ImageEnhance.Sharpness(image)
        enhanced = enhancer.enhance(2.0)
        enhanced.save("Modified_1.jpg")
        #del img
    if (CheckVar2.get()==1):
        enhancer=ImageEnhance.Sharpness(image)
        enhanced = enhancer.enhance(0.0)
        enhanced.save("Modified_2.jpg")
        #del img
    if (CheckVar3.get()==1):
        enhancer=ImageEnhance.Brightness(image)
        enhanced = enhancer.enhance(0.7)
        enhanced.save("Modified_3.jpg")
        #del img
    if (CheckVar5.get()==1):
        enhancer=ImageEnhance.Color(image)
        enhanced = enhancer.enhance(0.0)
        enhanced.save("Modified_5.jpg")
        #image.show()
        #del img
    if (CheckVar2.get()==1):
        enhancer=ImageEnhance.Color(image)
        enhanced = enhancer.enhance(0.7)
        enhanced.save("Modified_6.jpg")

    del image





if __name__ == '__main__':
    main()
