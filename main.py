import tkinter as tk
import tkinter.messagebox
from window2 import Window
from student import Student

class Main(Window):
    def __init__(self):
        super().__init__()
        self.studentrecord = []
        self.table = 'students'
        
    def displayrecords(self)->None:
        self.studentrecord= self.db.getall_records(self.table)
        for student in self.studentrecord:
            self.textbox.insert('', 'end', values=(f'{student[0]}', f'{student[1]}', f'{student[2]} ',f'{student[3]}', f'{student[4]}'))
        self.studentrecord.clear() # -> clear list so it will be used to store fresh record of database
    
    def no_empty_fields(self)->bool:
         # STORE EXTRACTED DATA FROM FIELDS IN STUDENT RECORD LIST
        for data in self.extractdata: # -> `extractdata` -> Data extracted from entry fields and combobox
            student_data = data.get()
            if student_data == '' or student_data =='SELECT COURSE' or student_data == 'SELECT LEVEL':
                tk.messagebox.showwarning('Student Management v1.0', f'Please Fill in all fields!')
                return False
            else:
                self.studentrecord.append(student_data)
        return True
    
    def addstudent(self)->None:
        if self.no_empty_fields():
            # Create Student Object
            self.student = Student(idno=self.studentrecord[0], lastname=self.studentrecord[1], firstname=self.studentrecord[2],course=self.studentrecord[3],level=self.studentrecord[4])
            
            # Add the student object to the database
            self.db.add_record(self.table,idno=self.student.getidno(),lastname=self.student.getlastname(), firstname=self.student.getfirstname(), course=self.student.getcourse(),level=self.student.getlevel())
            
            tk.messagebox.showinfo('Student Management v1.0',f'STUDENT SAVED !!!')
            
            self.resetfields() #  -> Reset Entry fields to blanks and Combobox to default values.
        
                       
    def cancelcommand(self)->None:
        self.root.quit() # -> quit the master/root window
            
     
if __name__ == ("__main__"):
    main = Main()