from operator import le
from tkinter import * #import tkinter GUI
from openpyxl import Workbook, load_workbook #automate excel
from openpyxl.styles.alignment import Alignment
from time import strftime
from tkinter import font
from turtle import back

#Toplevel windows boolean variables
#purpose sani na boolean variables para pag gin click mo an 'book' or an 'customers' button san bisan pira ka beses, ka-usad lang sya ma create san window
BOOK_WINDOW_CREATED = False 
CUSTOMERS_WINDOW_CREATED = False
#excel customers worksheet | workbook variable
wb = load_workbook('customer_database.xlsx')
#worksheet variable
ws = wb.active
#book window
def create_book_window():
    global BOOK_WINDOW_CREATED #para maging global variable sya
    if BOOK_WINDOW_CREATED is not True: #if false
        BOOK_WINDOW_CREATED = True #window created
        #create book window
        book_window = Toplevel()
        #book window closing function
        def close_book_window():
            global BOOK_WINDOW_CREATED #make it a global variable
            BOOK_WINDOW_CREATED = False #set to false so we can create it again
            book_window.destroy()
        book_window.protocol('WM_DELETE_WINDOW', close_book_window) #amo lang ina sya aram ko na protocol 'WM_DELETE_WINDOW' meaning pag gin close mo sya ica-call nya an 'close_book_window' function
        book_window.title("Book") #title san window
        book_window.resizable(False, False) #disable resizing
        width = 550 #window's width
        height = 500 #window's height
        #screen dimension
        screen_width = book_window.winfo_screenwidth() #screen max width pixels
        screen_height = book_window.winfo_screenheight() #screen max height pixels
        #kailangan ini sya para ma center an aton windows 
        center_x = int(screen_width/2 - width/2)
        center_y = int(screen_height/2 - height/2)
        #tas i-seset naton sya
        book_window.geometry(f'{width}x{height}+{center_x}+{center_y}') #set book window's height and width
        book_window.configure(bg='#FFFFFF') #main window background color
        
        #variables
        duration_price = 430 #per day price
        expected_date = StringVar()
        firstname = StringVar()
        lastname = StringVar()
        address = StringVar()
        contact = StringVar()
        email = StringVar()
        price = StringVar()
        duration = StringVar()
        #set values

        #header text
        Label(book_window, text='Customer Data', font=('sans-serif', 25, font.BOLD), bg='#FFFFFF',fg='#787A40').place(x=170, y=30)
        #first name
        Label(book_window, text='First name:', background='#FFFFFF', font=('sans-serif', 10)).grid(column=0, row=0, sticky=E, pady=(115, 5), padx=(100, 0))
        first_name_entry = Entry(book_window, width=15, highlightthickness=1, highlightbackground='#c0c4c1', textvariable=firstname).grid(column=1, row=0, pady=(115, 5), padx=(0, 20))
        #last name
        Label(book_window, text='Last name:', background='#FFFFFF', font=('sans-serif', 10)).grid(column=2, row=0, sticky=E, pady=(115, 5))
        last_name_entry = Entry(book_window, width=15, highlightthickness=1, highlightbackground='#c0c4c1', textvariable=lastname).grid(column=3, row=0, pady=(115, 5))
        #address 
        Label(book_window, text='Address:', background='#FFFFFF', font=('sans-serif', 10)).grid(column=0, row=1, sticky=E)
        address_entry = Entry(book_window, width=35, highlightthickness=1, highlightbackground='#c0c4c1', textvariable=address).grid(column=1, row=1, columnspan=3, sticky=W, pady=(5))
        #contact number
        Label(book_window, text='Contact #:', background='#FFFFFF', font=('sans-serif', 10)).grid(column=0, row=2, sticky=E)
        contact_number_entry = Entry(book_window, width=35, highlightthickness=1, highlightbackground='#c0c4c1', textvariable=contact).grid(column=1, row=2, columnspan=3, sticky=W, pady=(5))
        #email address
        Label(book_window, text='Email:', background='#FFFFFF', font=('sans-serif', 10)).grid(column=0, row=3, sticky=E)
        email_address_entry = Entry(book_window, width=35, highlightthickness=1, highlightbackground='#c0c4c1', textvariable=email).grid(column=1, row=3, columnspan=3, sticky=W, pady=(5))
        #payment and duration
        Label(book_window, text='Expected Date and Duration', font=('sans-serif', 20, font.BOLD), bg='#FFFFFF',fg='#787A40').place(x=110, y=255)
        #format label
        Label(book_window, text='Format: mm/dd/yy', background='#FFFFFF', font=('sans-serif', 9), fg='gray').place(x=170, y=305)
        #expected date
        Label(book_window, text='Expected date:', background='#FFFFFF', font=('sans-serif', 10)).grid(column=0, row=4, sticky=E, pady=(90, 5))
        date_entry = Entry(book_window, width=15, highlightthickness=1, highlightbackground='#c0c4c1', textvariable=expected_date)
        date_entry.grid(column=1, row=4, sticky=W, pady=(90, 5), columnspan=3)
        #duration
        Label(book_window, text='Duration:', background='#FFFFFF', font=('sans-serif', 10)).grid(column=0, row=5, sticky=E, pady=(5))
        duration_entry = Entry(book_window, width=4, highlightthickness=1, highlightbackground='#c0c4c1', textvariable=duration)
        duration_entry.grid(column=1, row=5, sticky=W, pady=(5))
        #set price
        def setPrice(event):
            _duration = duration.get()
            if (_duration.isnumeric()):
                price.set(duration_price * int(_duration))
            if (len(_duration) is 0):
                price.set("")
        duration_entry.bind('<KeyRelease>', setPrice)
        Label(book_window, text='day(s)', background='#FFFFFF', font=('sans-serif', 10)).grid(column=1, row=5, sticky=NS, pady=(5))
        #price
        Label(book_window, text='Price:', background='#FFFFFF', font=('sans-serif', 10)).grid(column=0, row=6, sticky=E, pady=(5))
        Label(book_window, textvariable=price, background='#FFFFFF', font=('sans-serif', 10)).grid(column=1, row=6, sticky=W, pady=(5))
        #submit customer's data
        def submit():
            #get variables value
            name = firstname.get() + " " + lastname.get()
            _address = address.get()
            _contact = contact.get()
            _email = email.get()
            _expected_date = expected_date.get()
            _duration = duration.get() + " day(s)"
            _amount_paid = price.get()
            #verify if any of the entries has 0 length value
            variables = [name, _address, _contact, _email, _expected_date, _duration, _amount_paid]
            hasZeroValue = False
            for x in variables:
                if (len(x) == 0):
                    hasZeroValue = True
            if (hasZeroValue is False):
                #slice or remove the first entered value if it starts with 0
                if (_duration[:1] == '0' or 0):
                    _duration = _duration[1:]
                #append data in the worksheet
                ws.append([name, _address, _contact, _email, _expected_date, _duration, _amount_paid])
                #get excel max occupied row
                max_row = ws.max_row
                #style occupied cells
                for x in range(1, (max_row + 1)):
                    for y in range(1, 8):
                        ws.cell(row=x, column=y).alignment = Alignment(horizontal='center', vertical='center') #horizontally and vertically center cells
                #save worksheet
                wb.save('customer_database.xlsx')
            else:
                print('Please fill out the entries')

        #submit button
        submit_reservation = Button(book_window, text='BOOK', font=('sans-serif', 11, font.BOLD), fg='#C8AB65', bg='#787A40', borderwidth=0, width=35, height=1, command=submit)
        submit_reservation.place(x=120, y=440)
        book_window.mainloop() #mainloop() need ini sya para ma display an window

#customers window
def create_customers_window():
    global CUSTOMERS_WINDOW_CREATED #para maging global variable sya
    if CUSTOMERS_WINDOW_CREATED is not True: #if false
        CUSTOMERS_WINDOW_CREATED = True #window created
        #create customers window
        customers_window = Toplevel()
        #book window closing function
        def close_customers_window():
            global CUSTOMERS_WINDOW_CREATED #make it a global variable
            CUSTOMERS_WINDOW_CREATED = False #set to false so we can create it again
            customers_window.destroy()
        customers_window.protocol('WM_DELETE_WINDOW', close_customers_window) #amo lang ina sya aram ko na protocol 'WM_DELETE_WINDOW' meaning pag gin close mo sya ica-call nya an 'close_customers_window' function
        customers_window.title("Customers") #title san window
        customers_window.resizable(False, False) #disable resizing
        width = 700 #window's width
        height = 450 #window's height
        #screen dimension
        screen_width = customers_window.winfo_screenwidth() #screen max width pixels
        screen_height = customers_window.winfo_screenheight() #screen max height pixels
        #kailangan ini sya para ma center an aton windows 
        center_x = int(screen_width/2 - width/2)
        center_y = int(screen_height/2 - height/2)
        #tas i-seset naton sya
        customers_window.geometry(f'{width}x{height}+{center_x}+{center_y}') #customers window's height and width
        customers_window.configure(bg='#FFFFFF') #main window background color
        customers_window.mainloop() #mainloop() need ini sya para ma display an window

#create main window
main = Tk() 
main.title("Reservation System") #title san window
main.resizable(False, False) #disable resizing
width = 600 #window's width
height = 450 #window's height
#screen dimension
screen_width = main.winfo_screenwidth() #screen max width pixels
screen_height = main.winfo_screenheight() #screen max height pixels

#kailangan ini sya para ma center an aton windows
center_x = int(screen_width/2 - width/2)
center_y = int(screen_height/2 - height/2)

#tas i-seset naton sya
main.geometry(f'{width}x{height}+{center_x}+{center_y}') #set main window's height and width
main.configure(bg='#FFFFFF') #main window background color

#display time
def start_timer(): #timer loop function
    current_time = strftime("%I:%M:%S") #current time, an strftime(), format ina sya san %HOUR %MINUTES %SECONDS https://www.w3schools.com/python/python_datetime.asp
    time.configure(text=current_time) #tas configure() meaning i-seset or i-change an text value san aton time label widget (inan sa baba)
    time.after(1000, start_timer) #after method an first argument milliseconds ina 1000 ms = 1 second, tas an panduwa an start_timer function ica-call sya para mag loop after san 1000 milliseconds

#time label widget
time = Label(main, font=('sans-serif', 15, font.BOLD), fg='#787A40', bg='#FFFFFF') #(container, font, text color, background-color)
time.grid(column=0, row=0, ipadx=20, ipady=20) #grid geometry manager, 3 ina sya (grid, pack, place) https://www.pythontutorial.net/tkinter/tkinter-pack/

#book button
book_button = Button(main, text='BOOK', font=('sans-serif', 11, font.BOLD), fg='#C8AB65', bg='#787A40', borderwidth=0, width=10, height=2, command=create_book_window) #(container, text value, font(font-family, size, weight), text color, background color, call create_book_window function)
book_button.place(x=190, y=220) #place geometry manager, (x, y) specific coordinates

#customers button
customers_button = Button(main, text='CUSTOMERS', font=('sans-serif', 11, font.BOLD), fg='#C8AB65', bg='#787A40', borderwidth=0, width=15, height=2, command=create_customers_window) #(container, text value, font(font-family, size, weight), text color, background color, call create_customers_window function)
customers_button.place(x=300, y=220) #place geometry manager, (x, y) specific coordinates
#call start timer
start_timer()
main.mainloop() #mainloop() need ini sya para ma display an window