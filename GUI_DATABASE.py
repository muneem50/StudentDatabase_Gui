from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("go")
root.geometry("1888x1999")

root.config(bg="Light Blue")

def open1():
    top= Toplevel()
    top.geometry("1888x1999")
    top.config(bg="Light Blue")

    top.title("Add Record")

    name = StringVar()
    roll = StringVar()

    marks1 = IntVar()
    marks2 = IntVar()
    marks3 = IntVar()
    marks4 = IntVar()
    marks5 = IntVar()

    total = IntVar()
    
    heading1 = Label(top, text="INPUT RECORD", font=("Times New Roman", 30, "bold", "underline"), bg="Light Blue",fg="Light Yellow").grid(row=0, column=2)
    
    head_name = Label(top, text="NAME",bg="Light Blue",font=("Times New Roman", 15, "underline")).grid(row=1, column=0, padx=200,pady=35)
    head_roll = Label(top, text="ROLL NUMBER",bg="Light Blue",font=("Times New Roman", 15, "underline")).grid(row=3, column=0, padx=42,pady=35)


    head_m1 = Label(top, text="MARKS OF MATHS",bg="Light Blue", font=("Times New Roman", 17, "underline")).grid(row=1, column=2, padx=0,pady=35)
    head_m2 = Label(top, text="MARKS OF PHYSICS",bg="Light Blue", font=("Times New Roman", 17, "underline")).grid(row=3, column=2, padx=20,pady=35)
    head_m3 = Label(top, text="MARKS OF CHEMISTRY",bg="Light Blue", font=("Times New Roman", 17, "underline")).grid(row=1, column=5, padx=0,pady=35)
    head_m4 = Label(top, text="MARKS OF BIOLOGY",bg="Light Blue", font=("Times New Roman", 17, "underline")).grid(row=5, column=3, padx=0,pady=35)
    head_m5 = Label(top, text="MARKS OF COMPUTER",bg="Light Blue", font=("Times New Roman", 17, "underline")).grid(row=3, column=5, padx=0,pady=35)

    head_total = Label(top, text="TOTAL MARKS",bg="Light Blue", font=("Times New Roman", 15, "underline")).grid(row=5, column=0, padx=0,pady=35)
    
    head_m0 = Label(top, text="",bg="Light Blue", font=("Times New Roman", 17, "underline")).grid(row=9, column=0, padx=0,pady=35)


    
    entry2 = Entry(top, bg="White", width=25, font=("Times New Roman", 15), textvariable = name)
    entry2.grid(row=2, column=0, ipady=3)

    entry3 = Entry(top, bg="White", width=25, font=("Times New Roman", 15), textvariable = roll)
    entry3.grid(row=4, column=0, ipady=3)

    entry4 = Entry(top, bg="White", width=25, font=("Times New Roman", 15), textvariable=marks1)
    entry4.grid(row=2, column=2, ipady=3)

    entry5 = Entry(top, bg="White", width=25, font=("Times New Roman", 15), textvariable=marks2)
    entry5.grid(row=4, column=2, ipady=3)

    entry6 = Entry(top, bg="White", width=25, font=("Times New Roman", 15), textvariable=marks3)
    entry6.grid(row=6, column=3, ipady=3)

    entry7 = Entry(top, bg="White", width=25, font=("Times New Roman", 15), textvariable=marks4)
    entry7.grid(row=2, column=5, ipady=3)

    entry8 = Entry(top, bg="White", width=25, font=("Times New Roman", 15), textvariable=marks5)
    entry8.grid(row=4, column=5, ipady=3)

    entry9 = Entry(top, bg="White", width=25, font=("Times New Roman", 15), textvariable = total)
    entry9.grid(row=6, column=0, ipady=3)




    def save():
        a = name.get()
        b = roll.get()

        c = marks1.get()
        d = marks2.get()
        e = marks3.get()
        o = marks4.get()
        g = marks5.get()

        h = total.get()

        t=round((c+d+e+o+g)*(100/h))

        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)
        entry6.delete(0, END)
        entry7.delete(0, END)
        entry8.delete(0, END)
        entry9.delete(0, END)


        f = open("polar.txt", "a")
        f.write( b+"\t\t")
        f.write(a+"\t\t")
        
        f.write(str(c)+'\t\t')
        f.write(str(d)+'\t\t')
        f.write(str(e)+'\t\t')
        f.write(str(o)+'\t\t')
        f.write(str(g)+'\t\t')
        f.write(str(h)+'\t\t')
        f.write(str(t)+'%')

        f.write("\n")
        f.close()
       
        
    btn=Button(top,text="ADD",command=save,width=10,pady=10,padx=10).grid(row=10, column=3)
        


    
def open2():
    
    top1=Toplevel()
    top1.geometry("1888x499")
    top1.title("Display")
    top1.config(bg="Light Blue")

    my_tree = ttk.Treeview(top1)
    my_tree['columns'] = ("Roll Number", "Name", "Marks Of 1","Marks Of 2","Marks Of 3","Marks Of 4","Marks Of 5","Total Marks","Percentage")
    
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("Roll Number", width=140, anchor=W)
    my_tree.column("Name", width=100,  anchor=CENTER)
    my_tree.column("Marks Of 1", width=120, anchor=W)
    my_tree.column("Marks Of 2", width=150, anchor=W)
    my_tree.column("Marks Of 3", width=150, anchor=W)
    my_tree.column("Marks Of 4", width=150, anchor=W)
    my_tree.column("Marks Of 5", width=150,anchor=W)
    my_tree.column("Percentage", width=150, anchor=W)
    my_tree.column("Total Marks", width=150,anchor=W)

    my_tree.heading("#0", text = "", anchor = W)
    my_tree.heading("Roll Number", text = "Roll Number", anchor = W)
    my_tree.heading("Name", text = "Name", anchor = CENTER)

    my_tree.heading("Marks Of 1", text = "Maths Marks",  anchor=W)
    my_tree.heading("Marks Of 2", text = "Physics Marks", anchor=W)
    my_tree.heading("Marks Of 3", text = "Biology Marks", anchor=W)
    my_tree.heading("Marks Of 4", text = "Chemistry Marks", anchor=W)
    my_tree.heading("Marks Of 5", text = "Computer Marks", anchor=W)
    my_tree.heading("Total Marks", text = "Total Marks", anchor=W)
    my_tree.heading("Percentage", text = "Percentage", anchor=W)

    count=0
    data=open("polar.txt","r")
    q=data.readlines()
    for record in q:
        my_tree.insert(parent='', index='end', iid=count, text="", values= (record))
        count+=1
    
    my_tree.grid(padx=45, pady=5)
    head_roll = Label(top1, text="",bg="Light Blue").grid(row=7, column=0)

    clse_butn =Button(top1, text="OK",command=top1.destroy, width=10).grid(row=10,column=0)   

def open6():
    top5=Toplevel()
    top5.geometry("1888x1999")
    top5.title("Search")
    top5.config(bg="Light Blue")

    roll = StringVar()
    lname = StringVar()

    newheading3 = Label(top5, text="ENTER NAME OF STUDENT", bg="Light Blue", font=("Times New Roman", 20, "underline")).grid(row=3, column=0, pady=30)
    newentry1 = Entry(top5, bg="White", width=30, font=("Times New Roman", 15), textvariable=lname)
    newentry1.grid(row=3, column=1, ipady=1, ipadx=15)


    newheading1 = Label(top5, text="SEARCH RECORD", font=("Arial Hebrew", 30, "bold", "underline"), bg="Light Blue",
                    fg="Green").grid(row=0, column=0, padx=100,pady=30)
    newheading2 = Label(top5, text="_"*40, font=("Times New Roman", 20),bg="Light Blue").grid(row=1, column=0, pady=40)
    newheading4 = Label(top5, text="ENTER ROLL NUMBER", bg="Light Blue", font=("Times New Roman",20, "underline")).grid(row=4, column=0,pady=30)
    newentry2 = Entry(top5, bg="White", width=30, font=("Times New Roman", 15), textvariable=roll)
    newentry2.grid(row=4, column=1, ipady=1, ipadx=15)

    def search():
        
        b = roll.get()
        a = lname.get()
    
        sb = str(b)
        sa = str(a)
        if (sb == "" or sa == ""):             
            messagebox.showerror("ERROR!","Entries are required")
        else:
            f = open("polar.txt", "r")
            for line in f:
                if sb in line and sa in line:
                    displayentry2.config(text=line)
             
    displayentry2 = Label(top5, bg="white", width=150, font=("Times New Roman", 11), highlightcolor="Black",
                      highlightthickness=1, height=8)
    displayentry2.place(x=95, y=535)

    displayentry3 = Label(top5, bg="white", width=150, font=("Times New Roman", 11), highlightcolor="Black",
                      highlightthickness=1,text='Roll Number\tName\t\t   Maths Marks\t   Physics Marks\t Biology Marks\t Chemistry Marks\tComputer Marks\tTotal Marks\tPercentage ', height=2)
    displayentry3.place(x=94, y=500)

            
    search_btn = Button(top5, text="SEARCH!", width=20, font=("Times New Roman", 12, "bold"), bg="Light Blue",
                 command=search).grid(row=6, column=1, pady=20)
  
    
add = Button(root, text="Add Record",command=open1, width=30,bg="Light Yellow",height=4,font=("Times New Roman", 15)).grid(row=2,column=2,pady=50)
display = Button(root, text="Display Record",command=open2,width=30,height=4,bg="Light Yellow",font=("Times New Roman", 15)).grid(row=4,column=2,pady=50)
search = Button(root, text="Search Record",command=open6,width=30,height=4,bg="Light Yellow",font=("Times New Roman", 15)).grid(row=6,column=2,pady=50)

heading1 = Label(root, text="Student Database", font=("Times New Roman", 30, "bold", "underline"), bg="Light Blue",fg="White").grid(row=0, column=0,padx=100)
close_win=Button(root, text="Exit", command=root.destroy,width=10,bg="Yellow").grid(row=6, column=8,padx=220)    
 

root.mainloop()


