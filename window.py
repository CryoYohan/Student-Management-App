import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from dbhelper2 import DBHelper

class Window():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Student Management v1.0')
        self.root.resizable(False,False)
        self.WIDTH = 685
        self.HEIGHT = 500
        self.table = 'students'
        self.FIELDHEADERS:list = ['IDNO', 'LASTNAME', 'FIRSTNAME', 'COURSE', 'LEVEL']
        self.db = DBHelper()
        self.extractdata = []
        self.studentrecord = []
        self.k=0
        self.add_widget()
        self.position()
   
        
    def position(self):
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.WIDTH}x{self.HEIGHT}+{(self.screen_width-self.WIDTH)//2}+{(self.screen_height-self.HEIGHT)//2}")
        self.root.mainloop()
           
        
    def headerframe(self)->None:
        # HEADER FRAME
        self.frame1 = tk.Frame(self.root,highlightbackground="black", highlightthickness=2,width= self.WIDTH, height=10, bg='blue2')
        self.frame1.pack_propagate(0)
        self.frame1.pack(fill='both', side='top', expand='False')
        # HEADER    
        self.header = tk.Label(self.frame1,text = 'Student Management v1.0', font="Verdana,20",bg='blue2',fg='gold')
        self.header.grid(row=0,column=0,padx=10,pady=5,sticky="W")
    
    def entryfieldsframe(self)->None:
        # ENTRY FIELDS FRAME
        self.frame2 = tk.Frame(self.root, highlightbackground='black', highlightthickness=1)
        self.frame2.pack_propagate(0)
        self.frame2.pack(fill='both', side='left', expand='False', padx=0, pady=0)
        
        # ADD ENTRY FIELDS
        for i in range(0,len(self.FIELDHEADERS)-2):
            # Label
            self.lbl = tk.Label(self.frame2,text= self.FIELDHEADERS[i],font="Verdana,20")
            self.lbl.grid(row=i+self.k,column=0,padx=5,pady=5,sticky="W")

            # Entry
            self.txt= tk.Entry(self.frame2,width=27,font="Verdana,20",cursor='hand2', relief='sunken')
            self.txt.grid(row=i+self.k+1,column=0,padx=5,pady=5)
            
            self.extractdata.append(self.txt)
            self.k+=1
            
         
    def cboxfieldframe(self)->None:
        # ADD COMBOBOX FIELDS         
        self.combobox_items:list = [['BSIT', 'BSCS', 'BSCPE', 'BSBA', 'BSED', 'BSICS'], [1,2,3,4]] # Course and level List           
        for i in range(0, len(self.combobox_items)):
            for j in range(3+i,(len(self.FIELDHEADERS)-1)+i):
                # Label
                self.lbl = tk.Label(self.frame2,text= self.FIELDHEADERS[j],font="Verdana,20")
                self.lbl.grid(row=j+self.k,column=0,padx=10,pady=5,sticky="W")

                # Create Combobox widget
                self.combo_box = ttk.Combobox(self.frame2,state='readonly',width=25,font="Verdana,17",values=self.combobox_items[i],cursor='hand2')
                self.combo_box.grid(row=j+self.k+1,column=0,padx=10,pady=5,sticky="W")
                
                self.extractdata.append(self.combo_box)

                # Set default value
                self.combo_box.set(f"SELECT {self.FIELDHEADERS[j]}")
                self.k+=1
    
    
    def buttonsframe(self)->None:
        # BUTTONS FRAME
        self.frame3 = tk.Frame(self.frame2)
        self.frame3.pack_propagate(0)
        self.frame3.pack(fill='both', side='bottom',padx=0, pady=35)
        
        # ADD BUTTONS
            # SAVE
        self.btn = tk.Button(self.frame3, text='SAVE',width=15,height=2,bg='green',fg='WHITE', command = self.addstudent,cursor='hand2', relief='raised')
        self.btn.grid(row=0,column=0,padx=10,pady=5,sticky="W")
        self.btn.bind("btn", self.addstudent)
            # CANCEL
        self.btn2 = tk.Button(self.frame3, text='CANCEL',width=15,height=2,highlightbackground="red", highlightthickness=1,bd=1,fg='red', command = self.cancelcommand, cursor='hand2',relief='raised')
        self.btn2.grid(row=0,column=1,padx=10,pady=5,sticky="W")
        self.btn2.bind("btn2", self.cancelcommand)
        
        
    def displaytextframe(self):
        # TEXT BOX FRAME       
        self.frame4 = tk.Frame(self.root, bg='red',highlightbackground='red', highlightthickness=3)
        self.frame4.pack_propagate(0)
        self.frame4.pack(fill='both', side='right', expand='True')
        
        # Style Configuration
        style = ttk.Style()
        style.configure('Treeview.Heading', font=('Courier', 8), fg='yellow')
        
        # Add Tree View Widget called 'textbox'    
        self.textbox = ttk.Treeview(self.frame4, columns=(1,2,3,4,5), show='headings',height=22,selectmode='browse')
        v_scrollbar = ttk.Scrollbar(self.frame4, orient='vertical', command=self.textbox.yview)
        
        # Set Headers of Headings in Tree View
        for i,header in enumerate(self.FIELDHEADERS): # add headers
            self.textbox.heading(i+1,text=header)
            
        # Create columns in Tree View with a fixed width of 80
        for i in range(1,len(self.FIELDHEADERS)+1): # add columns with a fixed width of 80
            self.textbox.column(i,width=80)
        
        # IF TOTAL RECORDS EXCEEDS 20, A SCROLLBAR IS PLACED, ELSE NONE
        total_records = len(self.textbox.get_children())
        if total_records > 20:
            self.textbox.configure(yscrollcommand=v_scrollbar.set)
            self.textbox.grid(row=0, column=0, sticky='nsew')
            v_scrollbar.grid(row=0, column=1, sticky='ns')
        else:
            self.textbox.grid(row=0, column=0, sticky='nsew')
            
        self.displayrecords()
    def resetfields(self)->None:
        # Reset Entry fields to blanks
        for i in range(0,len(self.extractdata)-2):
            self.extractdata[i].delete(0, tk.END)  # Clears the content of each Entry widget
        # Reset the comboboxes to default values
        for  i in range(3,len(self.extractdata)):
            self.extractdata[i].set(f"SELECT {self.FIELDHEADERS[i]}")
        total_records = len(self.textbox.get_children())
        if total_records>0:
            for item in self.textbox.get_children():
                self.textbox.delete(item)
            self.displayrecords()
        else:
            self.displayrecords()
                        
    def add_widget(self):
        self.headerframe()
        self.entryfieldsframe()
        self.cboxfieldframe()
        self.buttonsframe()
        self.displaytextframe()
        
