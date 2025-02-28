# -This code creates a simple application for managing the inventory of a store using Tkinter, a Python library for creating graphical user interfaces. The main features of this application include adding, deleting, updating, and searching for items in an SQLite database. Here's a breakdown of the main components of the code:

Importing Libraries: Necessary libraries, including tkinter and SQLite for database interaction, are imported.

Defining the Main Window: A main window is created with a specific design and color scheme for the application.

Defining Functions: Various functions for managing CRUD operations (Create, Read, Update, Delete) are defined. These functions include:

add_item(): To add an item to the database.
show_list(): To display the list of items in a Listbox.
clear(): To clear input fields.
remove_item(): To delete an item.
select_item(): To select an item from the list and populate input fields with its information.
update_item(): To update an item's information.
search_item(): To search for items in the database based on the search input.
Creating User Interface: The user interface of the application is built using Tkinter widgets such as Label, Entry, Button, and Listbox.

Running the Application: At the end of the code, the application is run with the mainloop() command, putting it in a ready state for user interaction.

This application allows the user to easily manage their store's inventory and access information stored in the database.

این کد یک نرم‌افزار ساده برای مدیریت موجودی یک فروشگاه با استفاده از Tkinter، کتابخانه‌ای برای ساخت رابط کاربری در پایتون، ایجاد می‌کند. اصلی‌ترین قابلیت‌های این نرم‌افزار شامل افزودن، حذف، به‌روزرسانی و جستجوی کالاها در یک دیتابیس SQLite است. در ادامه به تشریح اجزای اصلی کد می‌پردازیم:

وارد کردن کتابخانه‌ها: کتابخانه‌های موردنیاز، شامل tkinter و SQLite برای ارتباط با بانک اطلاعاتی، بارگذاری می‌شوند.

تعریف پنجره اصلی: یک پنجره اصلی با طراحی و رنگ‌بندی مشخص برای نرم‌افزار ایجاد می‌شود.

تعریف توابع: توابع مختلف برای مدیریت عملیات‌های CRUD (ایجاد، خواندن، به‌روزرسانی و حذف) تعریف شده‌اند. این توابع شامل موارد زیر هستند:

add_item(): برای افزودن کالا به دیتابیس.
show_list(): برای نمایش لیست کالاها در لیست باکس.
clear(): برای پاک‌کردن فیلدهای ورودی.
remove_item(): برای حذف یک کالا.
select_item(): برای انتخاب یک کالا از لیست و پر کردن قسمت‌های ورودی با اطلاعات آن.
update_item(): برای به‌روزرسانی اطلاعات یک کالا.
search_item(): برای جستجوی کالاها در دیتابیس بر اساس ورودی جستجو.
ایجاد رابط کاربری: با استفاده از ویجت‌های Tkinter شامل Label، Entry، Button و Listbox، رابط کاربری نرم‌افزار ساخته می‌شود.

اجرای برنامه: در انتهای کد، با دستور mainloop()، نرم‌افزار به حالت اجرایی درآمده و آماده به‌کار می‌شود.

این نرم‌افزار به کاربر اجازه می‌دهد تا به‌راحتی موجودی فروشگاه خود را مدیریت کند و به اطلاعات موجود در دیتابیس دسترسی داشته باشد.

