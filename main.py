''' ***ORIGINAL COPY***'''
import tkinter as tk
import tkinter.messagebox
from window import Window
from student import Student
import sqlite3

class Main(Window):
    def __init__(self):
        super().__init__()
        self.studentrecord = []
        self.table = 'students'
    
    def is_duplicate(self,idno)->bool:
        databaserecord = self.dbhelper.getall_records(self.table)
        for student in databaserecord:
            if student[1] == idno:
                tk.messagebox.showerror('Student Management v1.0', 'Student ID No Already Exists!')
                return True
        return False
            
    def displayrecords(self)->None:
        self.studentrecord= self.dbhelper.getall_records(self.table)
        for student in self.studentrecord:
            self.textbox.insert('', 'end', values=(f'{str(student[1]).title()}', f'{str(student[2]).title()}, {str(student[3]).title()} ',f'{student[4]}-{student[5]}'))
            print(f"{student[0]} {student[1]} {student[2]} {student[3]} {student[4]} {student[5]}")
        self.studentrecord.clear() # -> clear list so it will be used to store fresh record of database
        self.auto_scrollbar()
    
        
    def addstudent(self)->None:
        for data in self.widgets: # -> `extractdata` -> Data extracted from entry fields and combobox
            student_data = data.get()
            if student_data == '' or student_data =='SELECT COURSE' or student_data == 'SELECT LEVEL':
                tk.messagebox.showwarning('Student Management v1.0', f'Please Fill in all fields!')
                self.studentrecord.clear()
                return False
            else:
                self.studentrecord.append(student_data)
        if not self.is_duplicate(self.studentrecord[0]):
            self.student = Student(idno=self.studentrecord[0], lastname=self.studentrecord[1], firstname=self.studentrecord[2],course=self.studentrecord[3],level=self.studentrecord[4])
            # Add the student object to the database
            self.dbhelper.add_record(self.table,**self.student.__dict__)
            
            tk.messagebox.showinfo('Student Management v1.0',f'STUDENT SAVED !!!')
            
            self.resetfields() #  -> Reset Entry fields to blanks and Combobox to default values.
        else:
            self.studentrecord.clear()
            self.resetfields()
                       
    def cancelcommand(self)->None:
        #self.root.quit() # -> quit the master/root window
        self.resetfields() # -> mao daw ni dapat ana sila
            
     
if __name__ == ("__main__"):
    main = Main()