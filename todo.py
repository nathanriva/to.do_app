
from tkinter import *
from tkinter import messagebox

#____GRAFIC INTERFACE ROOT________________________________________________________________________________________________________#
root=Tk()
root.title("Lista de Tareas")
root.geometry("400x400")
root.resizable(False,False)

#____ APP CODE, FUNCTIONS ________________________________________________________________________________________________________#
todo_list= []

def openTaskFile():
    try:
        global todo_list
        with open("todo.txt","r") as todolist:
            tasks = todolist.readlines()
        
        for task in tasks: 
            if task !="\n":
                todo_list.append(task)
                listbox.insert(END, task )
    except:
        file=open("todo.txt", "w")
        file.close()

def addAction():
    task = task_entry.get()
    task_entry.delete(0, END)
    
    if task:
        with open("todo.txt", "a") as backup:
            backup.write(f"{task}\n")
            todo_list.append(task)
            listbox.insert(END, task)

def addTask():
    addAction()

def adpk(e):
    addAction()

def deleteAction():
    global todo_list
    task = str(listbox.get(ANCHOR))
    if task in todo_list:
        todo_list.remove(task)
        with open("todo.txt", "w") as todolist:
            for task in todo_list:
                todolist.write(task+"\n")

        listbox.delete(ANCHOR)

def deleteTask():
    try:
        deleteAction()
    except:
        messagebox.showerror("Error", "ningun item seleccionado")

def dlpk(e):
    deleteAction()

#____GRAFIC INTERFACE FRAMES_____________________________________________________________________________________________________#

#title
icon=PhotoImage(file="./logo/logo.png")
root.iconphoto(False, icon)
title=Label(root, text='TAREAS', font="ARIAL-BLACK 20")
title.place(x=130,y=10)

#imput
imputframe= Frame(root, width=400,height=38,bg="white")
imputframe.place(x=0,y=70)
task=StringVar()
task_entry=Entry(imputframe,width=25, font="arial 15", bd=0)
task_entry.place(x=90,y=7)
task_entry.focus()

#add button
add = Button(imputframe, text="ADD", font='arial 15 bold', width=6, bd=1, command=addTask, activebackground="gray")
add.place(x=0,y=0)

#list
listframe = Frame(root, bd=2,height=80,bg="white")
listframe.pack(pady=(120,0))
listbox= Listbox(listframe,width=50, font="arial 12 italic", bd=0)
listbox.pack(pady=(0,0))

#delete button
delete = Button(root, text="BORRAR", font='arial 15 bold', width=10, bd=1, command=deleteTask,  activebackground="gray")
delete.place(x=130,y=350)

#__________________________________________________________________________________________________________________________________
root.bind("<BackSpace>", dlpk)
root.bind("<Return>", adpk)

openTaskFile()
root.mainloop()
#closeTaskFile()