# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 10:29:44 2022

@author: ishar
"""
from tkinter import *
root=Tk()
root.geometry("900x900")
root.title("Element Generator")
root.configure(bg="lightblue")




elements = ["label","button","textarea","input","dropdown","radiobutton"]
dropdown = ttk.Combobox(root,state="readonly" ,values =elements)
dropdown.pack()
class CreateElements:
     def __init__(self):
        print("This is Create_Elements class")
        
     def createlabel(self):
         label=Label(root, text="A new label has been created using this class", fg="red", bg="lavender")
         label.pack()
     def createbutton(self):
         btn=Button(root, text="A new button has been created", command=self.message, fg="red",bg="lavender")
         btn.pack(padx=20, pady=10)
     def createtextarea(self):
         my_text= Text(root,height=10,width=80)
         my_text.pack(padx=10, pady=20)
     def createinput(self):
         input1=Entry(root)
         input1.pack(padx=10, pady=20)
     def createdropdown(self):
         elements = ["example 1", "example 2"]
         dropdown = ttk.Combobox(root, values = elements, state="readonly")
         dropdown.pack(padx=10, pady=20)
     def createradio(self):
         radiobtn=Radiobutton(root, text="radiobutton", value="yes", bg="lightblue")
         radiobtn.pack(padx=10, pady=20)
     def message(self):
         messagebox.showinfo("show info", "You clicked the button created using the class") 
     
                
     def choose(self):
        global dropdown
        element = dropdown.get()
        if element=="label":
            self.createlabel()
        elif element=="button":
            self.createbutton()
        elif element=="textarea":
            self.createtextarea()
        elif element=="input":
            self.createinput()
        elif element=="dropdown":
            self.createdropdown()
        elif element=="radiobutton":
            self.createradio()

           
            
            
               
obj_of_CreateElements = CreateElements()
btn = Button(root, text ="Click to create label and button element", command =obj_of_CreateElements.choose)

btn.pack(padx=20, pady=10)

root.mainloop()
