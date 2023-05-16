from tkinter import *
import time
import pyautogui
import keyboard

root = Tk()

class Funcs():
#                                      Class with the commands

#                                      method to clear all fields 
    def cleaning(self):
        self.entry_key.delete(0,END)
        self.entry_msg.delete(0,END)
        self.entry_keystop.delete(0,END)
#                                      method to verify empty fields and bind    
    def verify(self):
        key = self.entry_key.get()
        msg = self.entry_msg.get()
        keystop = self.entry_keystop.get()
        if key == '' or msg  == '' or keystop == '':
            self.button_status = Button(root,text="status", height = 1,width = 5,bg='red',fg='white')
            self.button_status.grid(column=2,row=5,padx=10,pady=10)
            self.label_error = Label(root,text="empty fields",bg='black',fg='white')
            self.label_error.grid(column=1,row=6,padx=10,pady=10)
            root.after(1000,self.label_error.destroy)
        else:
            self.button_status = Button(root,text="status", height = 1,width = 5,bg='green',fg='white')
            self.button_status.grid(column=2,row=5,padx=10,pady=10)
            self.label_error = Label(root,text="attached key",bg='black',fg='white')
            self.label_error.grid(column=1,row=6,padx=10,pady=10)    
            root.after(1000,self.label_error.destroy)
            while True:
                event = keyboard.read_event() 
                if event.event_type == keyboard.KEY_DOWN and event.name == key:
                    pyautogui.write(msg)
                if event.event_type == keyboard.KEY_DOWN and event.name == keystop:
                    break
            

class Application(Funcs):
#                                      Class with the interface     
    def __init__(self):
        self.root = root
        self.tela()
        self.widgets()
        root.mainloop()

    def tela(self):
        self.root.title('Binpy')
        self.root.configure(background='black')
        self.root.geometry('300x300')
        self.root.resizable(False,False)
        self.root.iconbitmap('')

    def widgets(self):
#                                      Buttons        
        self.button_refresh = Button(root,text="clear", height = 1,width = 5,bg='blue',fg='white',cursor='exchange',bd='4',command=self.cleaning)
        self.button_refresh.grid(column=0,row=5,padx=10,pady=10)

        self.button_run= Button(root,text="run", height = 1,width = 5,bg='green',fg='white',cursor="pirate",bd='4',command=self.verify)
        self.button_run.grid(column=1,row=5,padx=10,pady=10)

        self.button_status = Button(root,text="status", height = 1,width = 5,bg='grey',fg='white')
        self.button_status.grid(column=2,row=5,padx=10,pady=10)


#                                      Labels

        self.binpytitle = Label(root,text="Binpy",bg='black',fg='white')
        self.binpytitle.grid(column=1,row=1,padx=10,pady=10)
        self.binpytitle.config(font=('Comic Sans MS',35))

        self.label_key = Label(root,text="Bind key",bg='black',fg='white')
        self.label_key.grid(column=0,row=2,padx=10,pady=10)

        self.label_msg = Label(root,text="Message",bg='black',fg='white')
        self.label_msg.grid(column=0,row=3,padx=10,pady=10)

        self.label_keystop = Label(root,text="Stop key",bg='black',fg='white')
        self.label_keystop.grid(column=0,row=4,padx=10,pady=10)

    
        

#                                      Entrys
        self.entry_key = Entry(root,bd=2)
        self.entry_key.grid(column=1,row=2,padx=10,pady=10)

        self.entry_msg = Entry(root,bd=2)
        self.entry_msg.grid(column=1,row=3,padx=10,pady=10)

        self.entry_keystop = Entry(root,bd=2)
        self.entry_keystop.grid(column=1,row=4,padx=10,pady=10)

Application()