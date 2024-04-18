from tkinter import *
from tkinter import messagebox
from dat import *
win = Tk()
win.geometry('600x500+450+190')
win.config(bg='gold')
win.title('Contact Manager')
#----------FUNCTION-------
obj = Data_base('d:/contacts.db')

def clear():
    ent_name.delete(0,END)
    ent_fname.delete(0,END)
    ent_course.delete(0,END)
    ent_pass.delete(0,END)
def pop_list():
    lst_box.delete(0,END)
    for row in obj.fetch():
        lst_box.insert(END,row)
def insert():
    obj.insert(ent_name.get(),ent_fname.get(),ent_course.get(),ent_pass.get())
    if ent_name.get() == '' or ent_fname.get() == '' or ent_course.get() == '' or ent_pass == '':
        messagebox.showerror('ارور','لطفا همه فیلد ها را کامل کنید')
    pop_list()
    clear()
def exit():
    res = messagebox.askquestion('خروج','آیا میخواهید خارج شوید؟')
    if res == 'yes':
        win.destroy() 
#----------LABLE----------
lbl_name = Label(win,text=': نام',font='arial 16')
lbl_name.place(x=525,y=40)
lbl_name.config(bg='black',fg='yellow')

lbl_fname = Label(win,text=':نام خانوادگی',font='arial 16')
lbl_fname.place(x=160,y=48)
lbl_fname.config(bg='black',fg='yellow')

lbl_course = Label(win,text=':نام دوره',font='arial 16')
lbl_course.place(x=525,y=80)
lbl_course.config(bg='black',fg='yellow')

lbl_pass = Label(win,text=':رمز ورود',font='arial 16')
lbl_pass.place(x=160,y=85)
lbl_pass.config(bg='black',fg='yellow')

lbl_pass2 = Label(win,text=':رمز ورود',font='arial 16')
lbl_pass2.place(x=460,y=405)
lbl_pass2.config(bg='black',fg='yellow')
#------------ENTRY----------
ent_name = Entry(win,font='arial 8',width=18)
ent_name.place(x=390,y=50)
ent_name.config(relief='solid')

ent_fname = Entry(win,font='arial 8',width=18)
ent_fname.place(x=25,y=50)
ent_fname.config(relief='solid')

ent_course = Entry(win,font='arial 8',width=18)
ent_course.place(x=390,y=85)
ent_course.config(relief='solid')

ent_pass = Entry(win,font='arial 8',width=18)
ent_pass.place(x=25,y=85)
ent_pass.config(relief='solid')

ent_pass2 = Entry(win,font='arial 8',width=63)
ent_pass2.place(x=50,y=410)
ent_pass2.config(relief='solid')
#----------BUTTON------------
btn_view_all = Button(win,text='مشاهده همه',font='arial 13 bold',width=13)
btn_view_all.place(x=435,y=140)
btn_view_all.config(bg='black',fg='yellow')

btn_add = Button(win,text='اضافه کردن',font='arial 13 bold',width=13,command=insert)
btn_add.place(x=435,y=180)
btn_add.config(bg='black',fg='yellow')

btn_empt = Button(win,text='خالی کردن ورودی ها',font='arial 13 bold',width=13,command=clear)
btn_empt.place(x=435,y=220)
btn_empt.config(bg='black',fg='yellow')

btn_delete = Button(win,text='حذف کردن',font='arial 13 bold',width=13)
btn_delete.place(x=435,y=260)
btn_delete.config(bg='black',fg='yellow')

btn_exit = Button(win,text='خروج',font='arial 13 bold',width=13,command=exit)
btn_exit.place(x=435,y=300)
btn_exit.config(bg='black',fg='yellow')

btn_enter_net = Button(win,text='ورود به سامانه',font='arial 13 bold',width=13)
btn_enter_net.place(x=435,y=340)
btn_enter_net.config(bg='black',fg='yellow')
#----------list_box----------

lst_box = Listbox(win,font='arial 14',width=25,height=10)
lst_box.place(x=60,y=160)
lst_box.config(relief='solid')

win.mainloop()