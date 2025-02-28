from tkinter import *  
from tkinter import messagebox  
import database  

win = Tk()  
win.geometry("1000x600")  # اندازه بزرگتر برای پنجره  
win.title("فروشگاه رفاه")  
win.resizable(0, 0)  
win.configure(background="#4B9CD3")  # رنگ آبی ایرانی  

db1 = database.Database("d:/data1.db")  

# ======Function  
def add_item():  
    try:  
        fname = name_entry.get()  
        lname = family_entry.get()  
        address = address_entry.get()  
        phone = phone_entry.get()  

        # اعتبارسنجی ورود  
        if not lname.replace('.', '', 1).isdigit() or not address.replace('.', '', 1).isdigit() or not phone.isdigit():  
            messagebox.showerror("خطا در ورودی", "لطفاً قیمت خرید، قیمت فروش و تعداد را وارد کنید.")  
            return  

        db1.insert(fname, lname, address, phone)  
        show_list()  
        clear()  
    except Exception as e:  
        messagebox.showerror("خطا", f"یک خطا رخ داده: {str(e)}")  

def show_list():  
    contact_list.delete(0, END)  
    records = db1.select()  
    for rec in records:  
        # نمایش اطلاعات با فرمت جدید  
        contact_list.insert(END, f"نام کالا: {rec[1]}, قیمت خرید: {rec[2]}, قیمت فروش: {rec[3]}, تعداد: {rec[4]}")  

def clear():  
    name_entry.delete(0, END)  
    family_entry.delete(0, END)  
    address_entry.delete(0, END)  
    phone_entry.delete(0, END)  
    name_entry.focus_set()  

def remove_item():  
    global data  
    result = messagebox.askquestion('حذف', f'آیا مطمئن هستید که {data[1]} {data[2]} را حذف می‌کنید؟')  
    if result == 'yes':  
        db1.delete(data[0])  
        show_list()  

def select_item(event):  
    global data  
    clear()  
    index = contact_list.curselection()  
    data = contact_list.get(index)  
    
    # جدا کردن اطلاعات برای پر کردن ورودی‌ها  
    item_details = data.split(", ")  
    name_entry.insert(0, item_details[0].split(": ")[1])  
    family_entry.insert(0, item_details[1].split(": ")[1])  
    address_entry.insert(0, item_details[2].split(": ")[1])  
    phone_entry.insert(0, item_details[3].split(": ")[1])  

def update_item():  
    global data  
    db1.update(data[0], name_entry.get(), family_entry.get(), address_entry.get(), phone_entry.get())  
    show_list()  
    clear()  

def search_item():  
    records = db1.search(search_entry.get())  
    contact_list.delete(0, END)  
    if not records:  
        contact_list.configure(fg='#ff0000', font='arial 18 bold')  
        contact_list.insert(0, 'سجله‌ای یافت نشد!!!')  
    else:  
        for rec in records:  
            contact_list.insert(END, f"نام کالا: {rec[1]}, قیمت خرید: {rec[2]}, قیمت فروش: {rec[3]}, تعداد: {rec[4]}")  

def cancel():  
    win.destroy()  

# نمایش لیست موجودی  
def display_inventory():  
    show_list()  

# buttons and entry  
name_label = Label(win, text="نام کالا:", bg="#4B9CD3", font=('Tahoma', 14))  
name_label.place(x=10, y=5)  
name_entry = Entry(win, bd=3, relief=GROOVE)  
name_entry.place(x=110, y=10, width=200)  

family_label = Label(win, text="قیمت خرید:", bg="#4B9CD3", font=('Tahoma', 14))  
family_label.place(x=10, y=45)  
family_entry = Entry(win, bd=3, relief=GROOVE)  
family_entry.place(x=110, y=50, width=200)  

address_label = Label(win, text="قیمت فروش:", bg="#4B9CD3", font=('Tahoma', 14))  
address_label.place(x=320, y=5)  
address_entry = Entry(win, bd=3, relief=GROOVE)  
address_entry.place(x=420, y=10, width=200)  

phone_label = Label(win, text="تعداد:", bg="#4B9CD3", font=('Tahoma', 14))  
phone_label.place(x=320, y=45)  
phone_entry = Entry(win, bd=3, relief=GROOVE)  
phone_entry.place(x=420, y=50, width=200)  

contact_list = Listbox(win, height=15, width=120, bd=3)  
contact_list.place(x=10, y=130, width=600)  

scrollbar = Scrollbar(win)  
scrollbar.place(x=620, y=130, height=240)  

contact_list.configure(yscrollcommand=scrollbar.set)  
scrollbar.configure(command=contact_list.yview)  

# دکمه‌ها با طرح جدید  
add_btn = Button(win, text="افزودن", bg="#28a745", width=18, command=add_item, fg="white", relief=RAISED)  
add_btn.place(x=650, y=130)  

remove_btn = Button(win, text="حذف", bg='#dc3545', width=18, command=remove_item, fg="white", relief=RAISED)  
remove_btn.place(x=650, y=170)  

update_btn = Button(win, text="به‌روزرسانی", bg='#ffc107', width=18, command=update_item, fg="black", relief=RAISED)  
update_btn.place(x=650, y=210)  

clear_btn = Button(win, text="پاک کردن ورودی‌ها", bg='#007bff', width=18, command=clear, fg="white", relief=RAISED)  
clear_btn.place(x=650, y=250)  

search_entry = Entry(win, bd=3, relief=GROOVE)  
search_entry.place(x=275, y=100, width=200)  

search_btn = Button(win, text="جستجو", bg='#17a2b8', width=18, command=search_item, fg="white", relief=RAISED)  
search_btn.place(x=500, y=100)  

# دکمه نمایش لیست موجودی  
inventory_btn = Button(win, text="نمایش لیست موجودی", bg='#007bff', width=18, command=display_inventory, fg="white", relief=RAISED)  
inventory_btn.place(x=650, y=300)  

exit_a = Button(win, text="حذف و خروج", bg='#343a40', width=18, command=cancel, fg="white", relief=RAISED)  
exit_a.place(x=650, y=340)  

contact_list.bind('<<ListboxSelect>>', select_item)  
win.mainloop()