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
task1_due_date_label=tk.Label(tab1, text='Due date: ')
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
        print_records += str("BOOK: "+record[0]+"\nREMAINING COPIES: "+str(record[1])+"\n")
    #this is inside handler so wont render till pressed
    task1_result_label  = tk.Label(tab1, text=print_records)
    task1_result_label.grid(row=7, column=0, columnspan=2, pady=5, padx=10)
    #ALWAYS DO THIS AFTER SQL
    iq.commit()
    iq.close()

task1_warning=tk.Label(tab1, text='INPUT ERROR ', fg="red")

def checkout_book_handler():
    if(not utility.check_id(task1_book_id.get()) or
      not utility.check_id(task1_card_no.get()) or
      not utility.check_date(task1_date_out.get()) or
      not utility.check_date(task1_due_date.get())):
        task1_warning.grid(row=9, column=0,pady=5)
        return
    task1_warning.grid_forget()
    
    try:
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
    except:
       print("DB update failed")
    finally:
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
task2_warning=tk.Label(tab1, text='INPUT ERROR ', fg="red")


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

task2_warning=tk.Label(tab2, text='INPUT ERROR ', fg="red")

def add_borrower_handler():
    if(not utility.check_string(task2_name.get()) or
      not utility.check_string(task2_address.get())or
      not utility.check_phone(task2_phone.get())):
        task2_warning.grid(row=9, column=0,pady=5)
        return
    task2_warning.grid_forget()
    try:
      add_borrower_conn= sqlite3.connect("Library_Database.db")
      add_borrower_cur=add_borrower_conn.cursor()
      #dictionary implementation
      add_borrower_cur.execute("INSERT INTO BORROWER (name, address, phone) VALUES (:name_u, :address_u, :phone_u)",
                                {
                                  'name_u': task2_name.get(),
                                  'address_u': task2_address.get(),
                                  'phone_u': task2_phone.get(),
                                  
                                })
    
    
      add_borrower_conn= sqlite3.connect("Library_Database.db")
      add_borrower_cur=add_borrower_conn.cursor()
      #dictionary implementation
      add_borrower_cur.execute("INSERT INTO BORROWER (name, address, phone) VALUES (:name_u, :address_u, :phone_u)",
                                {
                                  'name_u': task2_name.get(),
                                  'address_u': task2_address.get(),
                                  'phone_u': task2_phone.get(),
                                  
                                })
    except:
      print("DB failed.")

    finally:
      add_borrower_conn.commit()
      add_borrower_conn.close()        
    add_borrower_get_label()

add_borrower_button = tk.Button(tab2, text = "Add Borrower", command=add_borrower_handler)
add_borrower_button.grid(row=6, column=0, columnspan=2, pady=5, padx=10)

"""TASK 3""" 
ttk.Label(tab3, text ="ADD BOOK").grid(column = 0, row = 0, padx = 30, pady = 30)  
task3_book_name= tk.Entry(tab3, width=30)
task3_book_name.grid(row = 1, column=1, pady=5)
task3_book_name_label= tk.Label(tab3, text='Book title: ')
task3_book_name_label.grid(row=1, column=0,pady=5)

task3_book_author= tk.Entry(tab3, width=30)
task3_book_author.grid(row = 2, column=1, pady=5)
task3_book_author_label= tk.Label(tab3, text='Book author: ')
task3_book_author_label.grid(row=2, column=0,pady=5)

task3_book_publisher= tk.Entry(tab3, width=30)
task3_book_publisher.grid(row = 3, column=1, pady=5)
task3_book_publisher_label= tk.Label(tab3, text='Book publisher: ')
task3_book_publisher_label.grid(row=3, column=0,pady=5)

task3_warning=tk.Label(tab3, text='INPUT ERROR ', fg="red")

def add_books_handler():
  if(not task3_book_name.get() or
     not task3_book_publisher.get() or
     not task3_book_author.get()
     ):
      task3_warning.grid(row=6, column=0,pady=5)
      return
  task3_warning.grid_forget()

  try:
    add_books_conn= sqlite3.connect("Library_Database.db")
    add_books_cur=add_books_conn.cursor()
    
    add_books_cur.execute("INSERT INTO BOOK (title, book_publisher) VALUES (:title, :publisher);",{
        'title':task3_book_name.get(),
        'publisher':task3_book_publisher.get()  
    })


    add_books_cur.execute("INSERT INTO BOOK_AUTHORS (book_id, author_name) VALUES ((SELECT book_id FROM BOOK WHERE title = :title), :author);",{
        'title':task3_book_name.get(),
        'author':task3_book_author.get()  
    })

    add_books_cur.execute("INSERT INTO BOOK_COPIES (book_id, branch_id, no_of_copies) SELECT Book.book_id, Library_Branch.branch_id, 5 FROM Book, Library_Branch WHERE title = :title;",{
        'title':task3_book_name.get(),
    })
  except:
     print("DB failed to insert")
  finally:
    add_books_conn.commit()
    add_books_conn.close()

  task2_success=tk.Label(tab3, text='SUCCESS', fg="green")
  task2_success.grid(row=7, column=0,pady=5)



add_books_button = tk.Button(tab3, text = "Add Book Copies", command=add_books_handler)
add_books_button.grid(row=4, column=0, columnspan=2, pady=5, padx=10)



"""TASK 4""" 
ttk.Label(tab4, text ="QUERY COPIES").grid(column = 0, row = 0, padx = 30, pady = 30)  
task4_book_name= tk.Entry(tab4, width=30)
task4_book_name.grid(row = 1, column=1, pady=5)
task4_book_name_label= tk.Label(tab4, text='Book title: ')
task4_book_name_label.grid(row=1, column=0,pady=5)

task4_warning=tk.Label(tab4, text='INPUT ERROR ', fg="red")

def search_copies_handler():
    if(not task4_book_name.get()):
      task4_warning.grid(row=6, column=0,pady=5)
      return
    task4_warning.grid_forget()
    query_copies_conn= sqlite3.connect("Library_Database.db")
    query_copies_cur=query_copies_conn.cursor()
    query_copies_cur.execute('''SELECT LB.branch_name, BC.no_of_copies
                                FROM Book as B JOIN Book_Copies as BC ON B.book_id=BC.book_id JOIN Library_Branch as LB on BC.Branch_id=LB.branch_id
                                WHERE B.title=:title;''',{
                                  'title':task4_book_name.get()
                                })
    records = query_copies_cur.fetchall()
    print_records = ''
    for record in records: 
          #IF AN ATTRIBUT IS NOT STRING, YOU GOTTA str() it.
          print_records += str("BRANCH: "+record[0]+" | # OF COPIES: "+str(record[1])+"\n")
    #this is inside handler so wont render till pressed
    task4_result_label  = tk.Label(tab4, text=print_records)
    task4_result_label.grid(row=7, column=0, columnspan=2, pady=5, padx=1)
    
    
search_copies_button = tk.Button(tab4, text = "Search Lates", command=search_copies_handler)
search_copies_button.grid(row=4, column=0, columnspan=2, pady=5, padx=10)


"""TASK 5""" 
ttk.Label(tab5, text ="LATE BOOKS").grid(column = 0, row = 0, padx = 30, pady = 30)  
task5_date_1= tk.Entry(tab5, width=30)
task5_date_1.grid(row = 1, column=1, pady=5)
task5_date_1_label= tk.Label(tab5, text='START DATE: ')
task5_date_1_label.grid(row=1, column=0,pady=5)

task5_date_2= tk.Entry(tab5, width=30)
task5_date_2.grid(row = 2, column=1, pady=5)
task5_date_2_label= tk.Label(tab5, text='END DATE: ')
task5_date_2_label.grid(row=2, column=0,pady=5)

task5_warning=tk.Label(tab3, text='INPUT ERROR ', fg="red")

def search_lates_handler():
  if(not utility.check_date(task5_date_1.get()) or
     not utility.check_date(task5_date_2.get())
     ):
      task5_warning.grid(row=6, column=0,pady=5)
      return
  task5_warning.grid_forget()
  search_lates_conn= sqlite3.connect("Library_Database.db")
  search_lates_cur=search_lates_conn.cursor()
  search_lates_cur.execute('''SELECT title, julianday(BL.returned_date)-julianday(BL.due_date) AS Days_Late
                              FROM Book_loans as BL JOIN Book as B on B.book_id = BL.book_id
                              WHERE julianday(BL.returned_date)-julianday(BL.due_date) > 0 AND
                              BL.due_date BETWEEN :date1 AND :date2;''', {      
                                'date1': task5_date_1.get(),
                                'date2': task5_date_2.get()
                            })
  records = search_lates_cur.fetchall()
  print_records = ''
  for record in records: 
        #IF AN ATTRIBUT IS NOT STRING, YOU GOTTA str() it.
        print_records += str("TITLE: "+record[0]+" | DAYS LATE: "+str(record[1])+"\n")
  #this is inside handler so wont render till pressed
  task5_result_label  = tk.Label(tab5, text=print_records)
  task5_result_label.grid(row=7, column=0, columnspan=2, pady=5, padx=1)
    

search_lates_button = tk.Button(tab5, text = "Search Lates", command=search_lates_handler)
search_lates_button.grid(row=4, column=0, columnspan=2, pady=5, padx=10)

"""TASK 6""" 
ttk.Label(tab6, text ="BORROWER FEES").grid(column = 0, row = 0, padx = 30, pady = 30)  
task6_borrower_name= tk.Entry(tab6, width=30)
task6_borrower_name.grid(row = 1, column=1, pady=5)
task6_borrower_name_label= tk.Label(tab6, text='Filter by Name: ')
task6_borrower_name_label.grid(row=1, column=0,pady=5)

task6_borrower_id= tk.Entry(tab6, width=30)
task6_borrower_id.grid(row = 2, column=1, pady=5)
task6_borrower_id_label= tk.Label(tab6, text='Filter by ID: ')
task6_borrower_id_label.grid(row=2, column=0,pady=5)

task6_warning=tk.Label(tab6, text='INPUT ERROR ', fg="red")
task6_result_label  = tk.Label(tab6, text="")

def search_borrower_fees_handler():
    #This one is different from the rest, its an and statement
    #because the user can use one or both filters.
    task6_result_label.grid_forget()
    search_borrowers_conn= sqlite3.connect("Library_Database.db")
    search_borrowers_cur=search_borrowers_conn.cursor()
    
    #CASE 1: name only
    if (task6_borrower_name.get() and not task6_borrower_id.get()):
       search_borrowers_cur.execute('''SELECT card_no, name, SUM(LateFeeBalance)
                                      FROM vBookLoanInfo
                                      WHERE name LIKE :name 
                                      GROUP BY card_no;''',{
                                         'name':'%'+task6_borrower_name.get()+'%'
                                      })
    #CASE 2: ID only
    elif (not task6_borrower_name.get() and task6_borrower_id.get()):
       search_borrowers_cur.execute('''SELECT card_no, name, SUM(LateFeeBalance)
                                      FROM vBookLoanInfo
                                      WHERE card_no = :card_no 
                                      GROUP BY card_no;''',{
                                         'card_no':task6_borrower_id.get()
                                      })
    #CASE 3: NAME AND ID
    elif (task6_borrower_name.get() and task6_borrower_id.get()):
      search_borrowers_cur.execute('''SELECT card_no, name, SUM(LateFeeBalance)
                                      FROM vBookLoanInfo
                                      WHERE name LIKE :name AND
                                      card_no = :card_no 
                                      GROUP BY card_no;''',{
                                         'name':'%'+task6_borrower_name.get()+'%',
                                         'card_no':task6_borrower_id.get()
                                      })
    #CASE 4: no filters
    else:
      search_borrowers_cur.execute('''SELECT card_no, name, SUM(LateFeeBalance)
                                      FROM vBookLoanInfo 
                                      GROUP BY card_no;''')
      
    records = search_borrowers_cur.fetchall()
    print_records = ''
    for record in records: 
          #IF AN ATTRIBUT IS NOT STRING, YOU GOTTA str() it.
          late_fee = "${:.2f}".format(record[2]) if record[2] != 0 else "$0.00"
          print_records += str("CARD NO: "+str(record[0])+" | NAME: "+record[1]+ " LATE FEE: ("+late_fee+")\n" )
    #this is inside handler so wont render till pressed
    task6_result_label.config(text=print_records)
    task6_result_label.grid(row=7, column=0, columnspan=2, pady=5, padx=1)


    

search_lates_button = tk.Button(tab6, text = "Filter", command=search_borrower_fees_handler)
search_lates_button.grid(row=4, column=0, columnspan=2, pady=5, padx=10)

"""TASK 7""" 
ttk.Label(tab7, text ="BOOK INFO").grid(column = 0, row = 0, padx = 30, pady = 30)  
task7_book_name= tk.Entry(tab7, width=30)
task7_book_name.grid(row = 1, column=1, pady=5)
task7_book_name_label= tk.Label(tab7, text='Filter by Name: ')
task7_book_name_label.grid(row=1, column=0,pady=5)

task7_book_id= tk.Entry(tab7, width=30)
task7_book_id.grid(row = 2, column=1, pady=5)
task7_book_id_label= tk.Label(tab7, text='Filter by ID: ')
task7_book_id_label.grid(row=2, column=0,pady=5)

task6_warning=tk.Label(tab7, text='INPUT ERROR ', fg="red")

def search_book_view_handler():
    if(not task7_book_name.get() and
     not utility.check_id(task7_book_id.get()) 
     ):
      task5_warning.grid(row=6, column=0,pady=5)
      return
    task6_warning.grid_forget()
    

search_lates_button = tk.Button(tab7, text = "Filter", command=search_book_view_handler)
search_lates_button.grid(row=4, column=0, columnspan=2, pady=5, padx=10)
"""DRIVER CODE""" 

root.mainloop()
