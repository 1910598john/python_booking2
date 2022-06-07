yawa

from tkinter import * #import tkinter GUI
from time import strftime
from tkinter import font
from turtle import back

#Toplevel windows boolean variables
#purpose sani na boolean variables para pag gin click mo an 'book' or an 'customers' button san bisan pira ka beses, ka-usad lang sya ma create san window
BOOK_WINDOW_CREATED = False 
CUSTOMERS_WINDOW_CREATED = False

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

        Label(book_window, text='Customer Data', font=('sans-serif', 25, font.BOLD), bg='#FFFFFF',fg='#787A40').place(x=170, y=30)
        #first name
        Label(book_window, text='First name:', background='#FFFFFF', font=('sans-serif', 10)).grid(column=0, row=0, sticky=E, pady=(120, 0), padx=(80, 0))
        first_name_entry = Entry(book_window, width=15, highlightthickness=1, highlightbackground='#c0c4c1').grid(column=1, row=0, pady=(120, 0), padx=(0, 20))
        #last name
        Label(book_window, text='Last name:', background='#FFFFFF', font=('sans-serif', 10)).grid(column=2, row=0, sticky=E, pady=(120, 0))
        last_name_entry = Entry(book_window, width=15, highlightthickness=1, highlightbackground='#c0c4c1').grid(column=3, row=0, pady=(120, 0))
        
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