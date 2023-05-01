"""
Project 2 Team 1
Matthew McNatt: 1001739201
Vladimir Caterov: 1002011907
Harrison Cawood: 1001729180
Date 4/11/2023
"""
#imports
import utility
import tkinter as tk                    
from tkinter import ttk
import sqlite3


#root code
root = tk.Tk()
root.title("LIBRARY DBMS")
root.geometry("800x400")
tabControl = ttk.Notebook(root)

#adds tab to the root
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)
tab6 = ttk.Frame(tabControl)
tab7 = ttk.Frame(tabControl)
  
tabControl.add(tab1, text ='Checkout Book')
tabControl.add(tab2, text ='Add Borrower')
tabControl.add(tab3, text ='Add Book')
tabControl.add(tab4, text ='Get Copies')
tabControl.add(tab5, text ='Track Lates')
tabControl.add(tab6, text ='Late Fees')
tabControl.add(tab7, text ='Book Info')

tabControl.pack(expand = 1, fill ="both")

"""TASK 1""" 
#THESE GUI ELEMENTS ARE SIMPLE. Only important note, is prefix names with task#, cause they 
#have to have global scope, and duplicates are hard to track.
#If you work in tab1, make sure your UI elements are set to tab1. 
ttk.Label(tab1, text ="CHECKOUT BOOK").grid(column = 0, row = 0, padx = 30, pady = 10)  
task1_book_id= tk.Entry(tab1, width=30)
task1_book_id.grid(row = 1, column=1, pady=5)
task1_book_id_label= tk.Label(tab1, text='Book id: ')
task1_book_id_label.grid(row=1, column=0,pady=5)

task1_branch_id= tk.Entry(tab1, width=30)
task1_branch_id.grid(row = 2, column=1,pady=5)
task1_branch_id_label= tk.Label(tab1, text='Branch ID: ')
task1_branch_id_label.grid(row=2, column=0,pady=5)

task1_card_no= tk.Entry(tab1, width=30)
task1_card_no.grid(row = 3, column=1,pady=5)
task1_card_no_label=tk.Label(tab1, text='CARD NO: ')
task1_card_no_label.grid(row=3, column=0,pady=5)

task1_date_out= tk.Entry(tab1, width=30)
task1_date_out.grid(row = 4, column=1,pady=5)
task1_date_out_label=tk.Label(tab1, text='Date Out: ')
task1_date_out_label.grid(row=4, column=0,pady=5)

task1_due_date= tk.Entry(tab1, width=30)
task1_due_date.grid(row = 5, column=1,pady=5)
task1_due_date_label=tk.Label(tab1, text='Date Out: ')
task1_due_date_label.grid(row=5, column=0,pady=5)

#buttons and handlers
#remember its python so definitions have to precede calls or they will be undefined
"""OUTPUT GENERATOR"""
def checkout_book_get_label():
    #basic sqlite interface
    iq = sqlite3.connect("Library_Database.db")
    iq_cursor = iq.cursor()
    iq_cursor.execute("SELECT title, no_of_copies FROM Book_Copies JOIN Book ON Book_Copies.book_id = Book.book_id WHERE Book.book_id=:book_id;",
                      {
                        'book_id': task1_book_id.get(),
                      })

    #The following is odd...but its just the established way to parse query output
    records = iq_cursor.fetchall()
    print_records = ''
    for record in records: 
        #IF AN ATTRIBUT IS NOT STRING, YOU GOTTA str() it.
        print_records += str("BOOK: "+record[0]+"\nREMAINING COPIES "+str(record[1])+"\n")
    #this is inside handler so wont render till pressed
    task1_result_label  = tk.Label(tab1, text=print_records)
    task1_result_label.grid(row=7, column=0, columnspan=2, pady=5, padx=10)
    #ALWAYS DO THIS AFTER SQL
    iq.commit()
    iq.close()

def checkout_book_handler():
    if(not utility.check_id(task1_book_id.get()) or
      not utility.check_id(task1_card_no.get()) or
      not utility.check_date(task1_date_out.get()) or
      not utility.check_date(task1_due_date.get())):
        task1_warning=tk.Label(tab1, text='INPUT ERROR ', fg="red")
        task1_warning.grid(row=9, column=0,pady=5)
        return
        
    checkout_book_conn= sqlite3.connect("Library_Database.db")
    checkout_book_cur=checkout_book_conn.cursor()
    #dictionary implementation
    checkout_book_cur.execute("INSERT INTO BOOK_LOANS (book_id, branch_id, card_no, date_out, due_date) VALUES (:book_id, :branch_id, :card_no, :date_out, :due_date)",
                              {
                                'book_id': task1_book_id.get(),
                                'branch_id': task1_branch_id.get(),
                                'card_no': task1_card_no.get(),
                                'date_out': task1_date_out.get(),
                                'due_date': task1_due_date.get()
                              })
    #decrements copies for that branch
    checkout_book_cur.execute("UPDATE BOOK_COPIES SET no_of_copies = no_of_copies-1 WHERE book_id = :book_id AND branch_id = :branch_id", 
                              {
                                'book_id': task1_book_id.get(),
                                'branch_id': task1_branch_id.get(),
                              })
    checkout_book_conn.commit()
    checkout_book_conn.close()
    checkout_book_get_label()

checkout_book_button = tk.Button(tab1, text = "Checkout Book", command=checkout_book_handler)
checkout_book_button.grid(row=6, column=0, columnspan=2, pady=5, padx=10)


"""TASK 2"""
# Add information about a new Borrower. Do not provide the CardNo in your query. Output the card
# number as if you are giving a new library card. Submit your editable SQL query that your code
# executes.
ttk.Label(tab2, 
          text ="ADD BORROWER").grid(column = 0, 
                               row = 0,
                               padx = 30,
                               pady = 10)  
task2_name= tk.Entry(tab2, width=30)
task2_name.grid(row = 1, column=1, pady=5)
task2_name_label= tk.Label(tab2, text='Name: ')
task2_name_label.grid(row=1, column=0,pady=5)

task2_address= tk.Entry(tab2, width=30)
task2_address.grid(row = 2, column=1,pady=5)
task2_address_label= tk.Label(tab2, text='Address: ')
task2_address_label.grid(row=2, column=0,pady=5)

task2_phone= tk.Entry(tab2, width=30)
task2_phone.grid(row = 3, column=1,pady=5)
task2_phone_label=tk.Label(tab2, text='Phone: ')
task2_phone_label.grid(row=3, column=0,pady=5)


#buttons and handlers
#remember its python so definitions have to precede calls or they will be undefined
"""OUTPUT GENERATOR"""
def add_borrower_get_label():
    #basic sqlite interface
    iq = sqlite3.connect("Library_Database.db")
    iq_cursor = iq.cursor()
    iq_cursor.execute("SELECT card_no FROM BORROWER WHERE phone=:phone_u;",
                      {
                        'phone_u': task2_phone.get(),
                      })

    #The following is odd...but its just the established way to parse query output
    records = iq_cursor.fetchall()
    print_records = ''
    for record in records: 
        #IF AN ATTRIBUT IS NOT STRING, YOU GOTTA str() it.
        print_records += str("CARD NO: "+str(record[0])+"\n")
    #this is inside handler so wont render till pressed
    task2_result_label  = tk.Label(tab2, text=print_records)
    task2_result_label.grid(row=7, column=0, columnspan=2, pady=5, padx=10)
    #ALWAYS DO THIS AFTER SQL
    iq.commit()
    iq.close()

def add_borrower_handler():
    if(not utility.check_string(task2_name.get()) or
      not utility.check_string(task2_address.get())):
        task1_warning=tk.Label(tab1, text='INPUT ERROR ', fg="red")
        task1_warning.grid(row=9, column=0,pady=5)
        return
        
    add_borrower_conn= sqlite3.connect("Library_Database.db")
    add_borrower_cur=add_borrower_conn.cursor()
    #dictionary implementation
    add_borrower_cur.execute("INSERT INTO BORROWER (name, address, phone) VALUES (:name_u, :address_u, :phone_u)",
                              {
                                'name_u': task2_name.get(),
                                'address_u': task2_address.get(),
                                'phone_u': task2_phone.get(),
                                
                              })
    
    add_borrower_conn.commit()
    add_borrower_conn.close()
    add_borrower_get_label()

add_borrower_button = tk.Button(tab2, text = "Add Borrower", command=add_borrower_handler)
add_borrower_button.grid(row=6, column=0, columnspan=2, pady=5, padx=10)

"""TASK 3""" 
ttk.Label(tab3, text ="ADD BOOK").grid(column = 0, row = 0, padx = 30, pady = 30)  
task2_book_name= tk.Entry(tab3, width=30)
task2_book_name.grid(row = 1, column=1, pady=5)
task2_book_name_label= tk.Label(tab3, text='Book title: ')
task2_book_name_label.grid(row=1, column=0,pady=5)

task2_book_author= tk.Entry(tab3, width=30)
task2_book_author.grid(row = 2, column=1, pady=5)
task2_book_author_label= tk.Label(tab3, text='Book author: ')
task2_book_author_label.grid(row=2, column=0,pady=5)

task2_book_publisher= tk.Entry(tab3, width=30)
task2_book_publisher.grid(row = 3, column=1, pady=5)
task2_book_publisher_label= tk.Label(tab3, text='Book publisher: ')
task2_book_publisher_label.grid(row=3, column=0,pady=5)

def add_books_handler():
  task2_warning=tk.Label(tab3, text='INPUT ERROR ', fg="red")
  if(not task2_book_name.get() or
     not task2_book_publisher.get() or
     not task2_book_author.get()
     ):
      task2_warning.grid(row=6, column=0,pady=5)
      return
  print("something")
  add_books_conn= sqlite3.connect("Library_Database.db")
  add_books_cur=add_books_conn.cursor()
  
  add_books_cur.execute("INSERT INTO BOOK (title, book_publisher) VALUES (:title, :publisher);",{
      'title':task2_book_name.get(),
      'publisher':task2_book_publisher.get()  
  })


  add_books_cur.execute("INSERT INTO BOOK_AUTHORS (book_id, author_name) VALUES ((SELECT book_id FROM BOOK WHERE title = :title), :author);",{
      'title':task2_book_name.get(),
      'author':task2_book_author.get()  
  })

  add_books_cur.execute("INSERT INTO BOOK_COPIES (book_id, branch_id, no_of_copies) SELECT Book.book_id, Library_Branch.branch_id, 5 FROM Book, Library_Branch WHERE title = :title;",{
      'title':task2_book_name.get(),
  })
      

  add_books_conn.commit()
  add_books_conn.close()
  task2_warning.destroy()
  task2_success=tk.Label(tab3, text='SUCCESS', fg="green")
  task2_success.grid(row=7, column=0,pady=5)



add_books_button = tk.Button(tab3, text = "Add Book Copies", command=add_books_handler)
add_books_button.grid(row=4, column=0, columnspan=2, pady=5, padx=10)



"""TASK 4""" 
ttk.Label(tab4, 
          text ="IMPLEMENT HERE").grid(column = 0, 
                               row = 0,
                               padx = 30,
                               pady = 30)  
"""TASK 5""" 
ttk.Label(tab5, 
          text ="IMPLEMENT HERE").grid(column = 0, 
                               row = 0,
                               padx = 30,
                               pady = 30)  
"""TASK 6""" 
ttk.Label(tab6, 
          text ="IMPLEMENT HERE").grid(column = 0, 
                               row = 0,
                               padx = 30,
                               pady = 30)  
"""TASK 1""" 
ttk.Label(tab7, 
          text ="IMPLEMENT HERE").grid(column = 0, 
                               row = 0,
                               padx = 30,
                               pady = 30)  
"""DRIVER CODE""" 

root.mainloop()
