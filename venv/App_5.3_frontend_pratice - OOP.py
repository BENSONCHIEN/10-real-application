# 1 design Fronted Interface
# can grid methd, sketch first
from tkinter import*
from App_5_backend_pratice import Database #anothr pythonn file, can use the function in this .py file

database = Database("books.db") #call a class

def get_selected_row(event):
    global selected_tuple  #不用return 了
    index = list1.curselection()[0] # select from a tuple
    selected_tuple = list1.get(index) # go back to this row
    #让entry 变成我在list选的数据
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])
    print(index)

def view_command():
    list1.delete(0,END) #每次执行先删掉之前的
    for row in App_5_backend_pratice.view(): #执行view，记录每一行到row
        list1.insert(END,row) #插入到listbox

def search_command():
    list1.delete(0,END)
    for row in App_5_backend_pratice.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        #获取每个entry的值，as arguments of search
        list1.insert(END,row)

def add_command():
    App_5_backend_pratice.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()) #直接运行
    # 在listbox显示加了什么
    list1.delete(0, END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

 #bind in tkinter

def delete_command():
    App_5_backend_pratice.delete(selected_tuple[0]) #直接用全局变量

def update_command():
    print(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    App_5_backend_pratice.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())


window = Tk()

window.wm_title("Benson's Book List")

l1 = Label(window,text = "Title")
l1.grid(row = 0, column = 0)

l2 = Label(window,text = "Author")
l2.grid(row = 0, column = 2)

l3 = Label(window,text = "Year")
l3.grid(row = 1, column = 0)

l4 = Label(window,text = "ISBN")
l4.grid(row = 1, column = 2)

title_text = StringVar()
e1 = Entry(window, textvariable = title_text)
e1.grid(row = 0, column = 1)

author_text = StringVar()
e2 = Entry(window, textvariable = author_text)
e2.grid(row = 0, column = 3)

year_text = StringVar()
e3 = Entry(window,textvariable = year_text)
e3.grid(row = 1, column = 1)

isbn_text = StringVar()
e4 = Entry(window,textvariable = isbn_text)
e4.grid(row = 1, column = 3)

list1 = Listbox(window,height = 10,width = 35)
list1.grid(row = 2, column = 0,rowspan = 6, columnspan = 2)

sb1 = Scrollbar(window)
sb1.grid(row = 2, column = 2, rowspan = 6)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row) #define myself, 把list1和这个function捆绑在一起

b1 = Button(window, text = "View all", width = 12, command = view_command)
b1.grid(row = 2, column = 3)

b2 = Button(window, text = "Search entry", width = 12, command = search_command)
b2.grid(row = 3, column = 3)

b3 = Button(window, text = "Add entry", width = 12, command = add_command)
b3.grid(row = 4, column = 3)

b4 = Button(window, text = "Update Selected", width = 12, command = update_command)
b4.grid(row = 5, column = 3)

b5 = Button(window, text = "Delete", width = 12, command = delete_command)
b5.grid(row = 6, column = 3)

b6 = Button(window, text = "Close", width = 12, command=window.destroy)
b6.grid(row = 7, column = 3)

window.mainloop()