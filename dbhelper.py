'''
	database helper API
'''
from sqlite3 import connect, Row

class DBHelper():
    def __init__(self):
        self.database:str = 'student.db'


    def postprocess(self,sql:str)->bool:
        #connect to database
        db:object = connect(self.database)
        #create cursor
        cursor:object = db.cursor()
        # execute sql command
        cursor.execute(sql)
        #commit the command
        db.commit()
        # close database
        cursor.close()
        return True if cursor.rowcount > 0 else False


    def getprocess(self,sql:str)->list:
        #connect to database
        db:Object = connect(self.database)
        #create cursor
        cursor:Object = db.cursor()
        #convert the record into an object
        cursor.row_factory = Row
        #execute command
        cursor.execute(sql)
        #fetch all data
        data:list = cursor.fetchall()
        #close database connection
        cursor.close()
        #return collected data
        return data
        

    def getall_records(self,table:str)->list:
        sql:str = f"SELECT * FROM '{table}'"
        return self.getprocess(sql)
        
        
    def find_record(self,table:str, **kwargs)->list:
        keys:list = list(kwargs.keys())
        values:list = list(kwargs.values())
        sql:str = f"SELECT * FROM `{table}` WHERE `{keys[0]}` == '{values[0]}'"
        return self.getprocess(sql)
        
        
    def add_record(self,table:str, **kwargs)->list:
        keys:list = list(kwargs.keys())
        values:list = list(kwargs.values())
        #join all keys together as one string with "`,`" as field delimiter
        flds:str = "`,`".join(keys)
        #join all keys together as one string with "`,`" as field delimiter
        data:str = "','".join(values)
        #construct sql statement
        sql:str = f"INSERT INTO `{table}`(`{flds}`) VALUES('{data}')"
        return self.postprocess(sql)
          
    def update_record(self,table:str, **kwargs)->list:
        #UPDATE  `students` SET `lastname`= 'durano', `firstname` = 'dennis'....WHERE
        #`idno` = '1000'
        keys:list = list(kwargs.keys())
        values:list = list(kwargs.values())
        flds:list = []
        # join both keys and values as an element in a list
        for i in range(1, len(keys)):
            flds.append(f"`{keys[i]}` = '{values[i]}'")
        #transform the list of string with "," as delimiter
        fld:str = ",".join(flds)
        #print(fld)
        #create sql statement
        sql:str = f"UPDATE `{table}` SET {fld} WHERE `{keys[0]}`= '{values[0]}'"
        return self.postprocess(sql)
            
        
        
    def delete_record(self,table:str, **kwargs)->list:
        keys:list = list(kwargs.keys())
        values:list = list(kwargs.values())
        sql:str = f"DELETE FROM `{table}` WHERE `{keys[0]}` = '{values[0]}'"
        return self.postprocess(sql)
