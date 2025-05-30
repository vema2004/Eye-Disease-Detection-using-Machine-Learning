from tkinter import *
import ctypes,os
from PIL import ImageTk, Image
import tkinter.messagebox as tkMessageBox
from tkinter.filedialog import askopenfilename
import tensorflow as tf
import tensorflow.keras.models as models
from tensorflow.keras.models import load_model
import cv2
import matplotlib.pyplot as plt
import  numpy as np

        
home = Tk()
home.title("Retinal disease detection")

img = Image.open("images/home.png")
img = ImageTk.PhotoImage(img)
panel = Label(home, image=img)
panel.pack(side="top", fill="both", expand="yes")
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
lt = [w, h]
a = str(lt[0]//2-620)
b= str(lt[1]//2-450)
home.geometry("1240x900+"+a+"+"+b)
home.resizable(0,0)
file = ''

def Exit():
    global home
    result = tkMessageBox.askquestion(
        "Retinal disease detection", 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        home.destroy()
        exit()
    else:
        tkMessageBox.showinfo(
            'Return', 'You will now return to the main screen')
        
def browse():
    
    global file,l1
    try:
        l1.destroy()
    except:
        pass
    
    file = askopenfilename(initialdir=os.getcwd(), title="Select Image", filetypes=( ("images", ".png"),("images", ".jpg"),("images", ".jpeg")))


def predictc():
    global file,l1
    if file!='' or file!= None:
        model = load_model('./model/resnet cataract.h5')
        image = cv2.imread(file)
        img = image
        image = cv2.resize(image,(224,224))
        image = image.reshape(-1,224,224,3)
        pred = model.predict(image)
        v = pred.argmax()
        
        pred = pred[0][pred.argmax()]*100
        
        if v==0:
            predt = "Contaract"
        elif v==1:
            predt = "other"
            
        acc = '('+str(round(pred,2))+'%)'
        l1 = Label(home,text="Predicted Output Is: "+predt+acc,font=('',14,'bold'),bg="#343434",fg="#dcb86f")
        l1.place(x=700,y=50)
        plt.imshow(img,cmap="gray")
        pValue = "Prediction For Cataract: {0}".format(predt+acc)
        plt.title(pValue)
        plt.show()

def predictg():
    global file,l1
    if file!='' or file!= None:
        model = load_model('./model/resnet glaucoma.h5')
        image = cv2.imread(file)
        img = image
        image = cv2.resize(image,(224,224))
        image = image.reshape(-1,224,224,3)
        pred = model.predict(image)
        v = pred.argmax()
        
        pred = pred[0][pred.argmax()]*100
        
        if v==0:
            predt = "Glaucoma"
        elif v==1:
            predt = "other"
            
        acc = '('+str(round(pred,2))+'%)'
        l1 = Label(home,text="Predicted Output Is: "+predt+acc,font=('',14,'bold'),bg="#343434",fg="#dcb86f")
        l1.place(x=700,y=50)
        plt.imshow(img,cmap="gray")
        pValue = "Prediction For Glaucoma: {0}".format(predt+acc)
        plt.title(pValue)
        plt.show()

def predicth():
    global file,l1
    if file!='' or file!= None:
        model = load_model('./model/resnet hypertension.h5')
        image = cv2.imread(file)
        img = image
        image = cv2.resize(image,(224,224))
        image = image.reshape(-1,224,224,3)
        pred = model.predict(image)
        v = pred.argmax()
        
        pred = pred[0][pred.argmax()]*100
        
        if v==0:
            predt = "hypertension"
        elif v==1:
            predt = "other"
            
        acc = '('+str(round(pred,2))+'%)'
        l1 = Label(home,text="Predicted Output Is: "+predt+acc,font=('',14,'bold'),bg="#343434",fg="#dcb86f")
        l1.place(x=700,y=50)
        plt.imshow(img,cmap="gray")
        pValue = "Prediction For hypertension: {0}".format(predt+acc)
        plt.title(pValue)
        plt.show()

def predictm():
    global file,l1
    if file!='' or file!= None:
        model = load_model('./model/resnet myopia.h5')
        image = cv2.imread(file)
        img = image
        image = cv2.resize(image,(224,224))
        image = image.reshape(-1,224,224,3)
        pred = model.predict(image)
        v = pred.argmax()
        
        pred = pred[0][pred.argmax()]*100
        
        if v==0:
            predt = "myopia"
        elif v==1:
            predt = "other"
            
        acc = '('+str(round(pred,2))+'%)'
        l1 = Label(home,text="Predicted Output Is: "+predt+acc,font=('',14,'bold'),bg="#343434",fg="#dcb86f")
        l1.place(x=700,y=50)
        plt.imshow(img,cmap="gray")
        pValue = "Prediction For myopia: {0}".format(predt+acc)
        plt.title(pValue)
        plt.show()

def predictd():
    global file,l1
    if file!='' or file!= None:
        model = load_model('./model/resnet diabetes.h5')
        image = cv2.imread(file)
        img = image
        image = cv2.resize(image,(224,224))
        image = image.reshape(-1,224,224,3)
        pred = model.predict(image)
        v = pred.argmax()
        
        pred = pred[0][pred.argmax()]*100
        
        if v==0:
            predt = "Diabetes"
        elif v==1:
            predt = "other"
            
        acc = '('+str(round(pred,2))+'%)'
        l1 = Label(home,text="Predicted Output Is: "+predt+acc,font=('',14,'bold'),bg="#343434",fg="#dcb86f")
        l1.place(x=700,y=50)
        plt.imshow(img,cmap="gray")
        pValue = "Prediction For Diabetes: {0}".format(predt+acc)
        plt.title(pValue)
        plt.show()
        
def about():
    about = Toplevel()
    about.title("Retinal disease detection")

    img = Image.open("images/about.png")
    img = ImageTk.PhotoImage(img)
    panel = Label(about, image=img)
    panel.pack(side="top", fill="both", expand="yes")
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
    lt = [w, h]
    a = str(lt[0]//2-620)
    b= str(lt[1]//2-450)
    about.geometry("1240x900+"+a+"+"+b)
    about.resizable(0,0)
    about.mainloop()
    
photo = Image.open("images/1.png")
img2 = ImageTk.PhotoImage(photo)
b1=Button(home, highlightthickness = 0, bd = 0,activebackground="#343434", image = img2,command=browse)
b1.place(x=0,y=230)

photo = Image.open("images/2.png")
img3 = ImageTk.PhotoImage(photo)
b2=Button(home, highlightthickness = 0, bd = 0,activebackground="#343434", image = img3,command=predictc)
b2.place(x=0,y=314)

photo = Image.open("images/5.png")
img6 = ImageTk.PhotoImage(photo)
b5=Button(home, highlightthickness = 0, bd = 0,activebackground="#343434", image = img6,command=predictm)
b5.place(x=0,y=569)

photo = Image.open("images/3.png")
img4 = ImageTk.PhotoImage(photo)
b3=Button(home, highlightthickness = 0, bd = 0,activebackground="#343434", image = img4,command=predictg)
b3.place(x=0,y=398)

photo = Image.open("images/4.png")
img5 = ImageTk.PhotoImage(photo)
b4=Button(home, highlightthickness = 0, bd = 0,activebackground="#343434", image = img5,command=predicth)
b4.place(x=0,y=484)

photo = Image.open("images/6.png")
img7 = ImageTk.PhotoImage(photo)
b6=Button(home, highlightthickness = 0, bd = 0,activebackground="#343434", image = img7,command=predictd)
b6.place(x=0,y=654)

photo = Image.open("images/7.png")
img8 = ImageTk.PhotoImage(photo)
b7=Button(home, highlightthickness = 0, bd = 0,activebackground="#343434", image = img8,command=about)
b7.place(x=76,y=818)

photo = Image.open("images/8.png")
img9 = ImageTk.PhotoImage(photo)
b8=Button(home, highlightthickness = 0, bd = 0,activebackground="#343434", image = img9,command=Exit)
b8.place(x=752,y=819)
home.mainloop()
