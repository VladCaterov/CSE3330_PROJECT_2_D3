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
  
#root code
root = tk.Tk()
root.title("LIBRARY DBMS")
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
ttk.Label(tab1, 
          text ="IMPLEMENT HERE").grid(column = 0, 
                               row = 0,
                               padx = 30,
                               pady = 30)  
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