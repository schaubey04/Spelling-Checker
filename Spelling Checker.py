from tkinter import*
import tkinter
from textblob import TextBlob

root=Tk()
root.title("Spelling Checker")
root.geometry("700x400")
root.resizable(False,False)
root.config(bg="#dae6f6")

def spelling_check():
    word=enter_text.get()
    a=TextBlob(word)
    right=str(a.correct())

    cs=Label(root,text="Correct text is: ",font=("poppins",20),bg="#dae6f6",fg="#364971")
    cs.place(x=100,y=250)
    spell.config(text=right)

#icon
icon_image=PhotoImage(file="Spelling logo.png")
root.iconphoto(False,icon_image)

#Label

heading=Label(root,text="Spelling Checker",font=("Trebuchet MS",30,"bold"),bg="#dae6f6",fg="#364971")
heading.pack(pady=(50,0))

enter_text=Entry(root,justify="center",width=30,font=("poppins",25),bg="white",bd=2)
enter_text.pack(pady=10)
enter_text.focus()

#button
button=Button(root,text="Check",font=("arial",20,"bold"),fg="white",bg="red",command=spelling_check)
button.pack()

spell=Label(root,font=("poppins",20),bg="#dae6f6",fg="#364971")
spell.place(x=350,y=250)

root.mainloop()