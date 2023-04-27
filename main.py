"""
Project 2 Team 1
Matthew McNatt: 1001739201
Vladimir Caterov: 1002011907
Harrison Cawood: 1001729180
Date 4/11/2023
"""
#imports
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
ttk.Label(tab1, text ="IMPLEMENT HERE").grid(column = 0, row = 0, padx = 30, pady = 10)  
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

#buttons
def checkout_book_get_label():
    iq = sqlite3.connect("Library_Database.db")
    iq_cursor = iq.cursor()
    iq_cursor.execute("SELECT title, no_of_copies FROM Book_Copies JOIN Book ON Book_Copies.book_id = Book.book_id WHERE Book.book_id=:book_id;",
                      {
                        'book_id': task1_book_id.get(),
                      })

    records = iq_cursor.fetchall()
    print_records = ''
    for record in records: 
        print_records += str("BOOK: "+record[0]+"\nREMAINING COPIES "+str(record[1])+"\n")

    task1_result_label  = tk.Label(tab1, text=print_records)
    task1_result_label.grid(row=7, column=0, columnspan=2, pady=5, padx=10)

    iq.commit()
    iq.close()

def checkout_book_handler():
    checkout_book_conn= sqlite3.connect("Library_Database.db")
    checkout_book_cur=checkout_book_conn.cursor()
    checkout_book_cur.execute("INSERT INTO BOOK_LOANS (book_id, branch_id, card_no, date_out, due_date) VALUES (:book_id, :branch_id, :card_no, :date_out, :due_date)",
                              {
                                'book_id': task1_book_id.get(),
                                'branch_id': task1_branch_id.get(),
                                'card_no': task1_card_no.get(),
                                'date_out': task1_date_out.get(),
                                'due_date': task1_due_date.get()
                              })
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
ttk.Label(tab2, 
          text ="IMPLEMENT HERE").grid(column = 0, 
                               row = 0,
                               padx = 30,
                               pady = 30)  
"""TASK 3""" 
ttk.Label(tab3, 
          text ="IMPLEMENT HERE").grid(column = 0, 
                               row = 0,
                               padx = 30,
                               pady = 30)  
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
