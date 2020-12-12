from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

def c2():
    
    
    f = filedialog.askopenfilename(initialdir="C:\\User\\" , filetypes=(("PDF file","*.pdf"),))
    MyButton2['state']='disable'
    MyButton3['state']='disable'
    MyButton4['state']='disabled'
    MyButton5['state']='disabled'
    print(f)


    
    
def c3():
    
    
    f = filedialog.askopenfilename(initialdir="C:\\User\\" , filetypes=(("TXT file","*.txt"),))
    MyButton2['state']='disable'
    MyButton3['state']='disable'
    MyButton4['state']='disabled'
    MyButton5['state']='disabled'
    print(f)
    
   
    
def c5():
    from tkinter import simpledialog
    consumer_key=simpledialog.askstring(title="INPUT",prompt="Enter the Consumer key")
    consumer_seceret__key=simpledialog.askstring(title="INPUT",prompt="Enter the Consumer Seceret key")
    access_token_key=simpledialog.askstring(title="INPUT",prompt="Enter the Access Token key")
    access_token_secret_key=simpledialog.askstring(title="INPUT",prompt="Enter the Access Token Secret key")
    
    print(consumer_key)
    print(consumer_seceret__key)
    print(access_token_key)
    print(access_token_secret_key)
    MyButton2['state']='disable'
    MyButton3['state']='disable'
    MyButton4['state']='disabled'
    MyButton5['state']='disabled'
    

def c4():
    from tkinter import simpledialog
    
    f=simpledialog.askstring(title="INPUT",prompt="Enter the url")    
    
    MyButton2['state']='disable'
    MyButton3['state']='disable'
    MyButton4['state']='disabled'
    MyButton5['state']='disabled'
    print(f)
    

s1=s2=s3=s4='normal'

root=Tk()

root.title("Sentimental Analysis")

#root.geometry("640x340+0+0")

myLabel1=Label(root,text="Hello User!")
myLabel=Label(root,text=" ")

myLabel2=Label(root,text="To enter a text from pdf:")
myLabel3=Label(root,text="To enter a text from file:")
myLabel4=Label(root,text="To enter a text from Website:")
myLabel5=Label(root,text="To enter a text from Twitter:")


MyButton2=Button(root,text="click Here!",command=c2, state = s1,padx=80,pady=2)
MyButton3=Button(root,text="click Here!",command=c3, state = s2,padx=80,pady=2)
MyButton4=Button(root,text="click Here!",command=c4, state = s3,padx=80,pady=2)
MyButton5=Button(root,text="click Here!",command=c5, state = s4,padx=80,pady=2)

myLabel1.grid(row=1,column=3)
myLabel.grid(row=0,column=1)


myLabel2.grid(row=2,column=2)
MyButton2.grid(row=2,column=5)
myLabel3.grid(row=4,column=2)
MyButton3.grid(row=4,column=5)
myLabel4.grid(row=6,column=2)
MyButton4.grid(row=6,column=5)
myLabel5.grid(row=8,column=2)
MyButton5.grid(row=8,column=5)




root.mainloop()