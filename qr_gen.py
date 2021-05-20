from tkinter import *
from resizeimage import resizeimage
import qrcode
from PIL import Image,ImageTk

class QGen:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+200+50")
        self.root.title("QR Code Generator")
        self.root.resizable(False,False)

        self.var_regno=StringVar()
        self.var_name=StringVar()
        self.var_phone=StringVar()
        self.var_dept=StringVar()

        title=Label(self.root,text="QR Code Generator",font=("times new roman",40),bg='#053246',fg='white').place(x=0,y=0,relwidth=1)

        entryFrame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        entryFrame.place(x=50,y=100,width=500,height=380)
        
        title1=Label(entryFrame,text="Details",font=("goudy old style",20),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)
        
        lbl_code=Label(entryFrame,text="Reg. Number",font=("times new roman",15,'bold'),bg='white').place(x=20,y=60)
        lbl_name=Label(entryFrame,text="Name",font=("times new roman",15,'bold'),bg='white').place(x=20,y=100)
        lbl_dept=Label(entryFrame,text="Department",font=("times new roman",15,'bold'),bg='white').place(x=20,y=140)
        lbl_phno=Label(entryFrame,text="Phone",font=("times new roman",15,'bold'),bg='white').place(x=20,y=180)

        
        txt_code=Entry(entryFrame,textvariable=self.var_regno,font=("times new roman",15),bg='white').place(x=200,y=60)
        txt_name=Entry(entryFrame,textvariable=self.var_name,font=("times new roman",15),bg='white').place(x=200,y=100)
        txt_dept=Entry(entryFrame,textvariable=self.var_dept,font=("times new roman",15),bg='white').place(x=200,y=140)
        txt_phno=Entry(entryFrame,textvariable=self.var_phone,font=("times new roman",15),bg='white').place(x=200,y=180)


        btn_gen=Button(entryFrame,text='Generate QR',command=self.gen,font=("times new roman",18,'bold'),bg='#2196f3',fg='white').place(x=70,y=240,width=180,height=30)
        btn_clr=Button(entryFrame,text='Clear',command=self.clr,font=("times new roman",18,'bold'),bg='#607d8b',fg='white').place(x=300,y=240,width=120,height=30)


        self.msg=''
        self.lbl_msg=Label(entryFrame,text=self.msg,font=("times new roman",20),bg='white',fg='green')
        self.lbl_msg.place(x=0,y=320,relwidth=1)



        qrFrame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        qrFrame.place(x=600,y=100,width=250,height=380)
        title2=Label(qrFrame,text="QR Code",font=("goudy old style",20),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)

        self.qrc=Label(qrFrame,text='No QR Code \nAvailable',font=('times new roman',15),bg='#60bbf0',fg='white',bd=1,relief=RIDGE)
        self.qrc.place(x=35,y=100,width=180,height=180)

    def clr(self):
        self.var_regno.set('') 
        self.var_name.set('') 
        self.var_dept.set('') 
        self.var_phone.set('')
        self.msg=''
        self.lbl_msg.config(text=self.msg)
        self.qrc.config(image='')

    def gen(self):
        if self.var_regno.get()=='' or self.var_name.get()=='' or self.var_dept.get()=='' or self.var_phone.get()=='':
            self.msg='All Fields are Required !!'
            self.lbl_msg.config(text=self.msg,fg='red')
        else:
            qr_data=(f"Reg No : {self.var_regno.get()}\nName : {self.var_name.get()}\nDepartment : {self.var_dept.get()}\nPhone No : {self.var_phone.get()}")
            qr_code=qrcode.make(qr_data)
            
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("QR/R_"+str(self.var_regno.get())+'.png')

            self.img=ImageTk.PhotoImage(qr_code)
            self.qrc.config(image=self.img)
            
            self.msg="QR Code Generated Successfully!!!"
            self.lbl_msg.config(text=self.msg,fg='green')


root=Tk()
o=QGen(root)
root.mainloop()