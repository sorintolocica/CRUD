
import db_connection as dbConn;

class Update:
    def func_UpdateData(self):
        # Ge the sql connection
        connection = dbConn.getConnection()

        id = input('Enter Employee Id = ')
    
        try:
           # Fethc the data which needs to be updated
           sql = "Select * From Employee Where Id = ?" 
           cursor = connection.cursor()
           cursor.execute(sql, [id])
           item = cursor.fetchone()
           print('Data Fetched for Id = ', id)
           print('ID\t\t Name\t\t\t Age')
           print('-------------------------------------------')       
           print(' {}\t\t {} \t\t\t{} '.format(item[0], item[1], item[2]))
           print('-------------------------------------------')
           print('Enter New Data To Update Employee Record ')

           name = input('Enter New Name = ')
           age = input('Enter New Age = ')
           query = "Update Employee Set Name = ?, Age =? Where Id =?" 
       
           # Execute the update query
           cursor.execute(query, [name, age, id])
           connection.commit()
           print('Data Updated Successfully')

        except:
             print('Somethng worng, please check')

        finally:
           # Close the connection
           connection.close()