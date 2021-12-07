
import db_connection as dbConn;

class Delete:
    def func_DeleteData(self):
        # Get the sql connection
        connection = dbConn.getConnection()

        id = input('Enter Employee Id = ')
    
        try:
           # Get record which needs to be deleted
           sql = "Select * From Employee Where Id = ?" 
           cursor = connection.cursor()
           cursor.execute(sql, [id])
           item = cursor.fetchone()
           print('Data Fetched for Id = ', id)
           print('ID\t\t Name\t\t\t Age')
           print('-------------------------------------------')       
           print(' {}\t\t {} \t\t\t{} '.format(item[0], item[1], item[2]))
           print('-------------------------------------------')
           confirm = input('Are you sure to delete this record (Y/N)?')

           # Delete after confirmation
           if confirm == 'Y':
               deleteQuery = "Delete From Employee Where Id = ?"
               cursor.execute(deleteQuery,[id])
               connection.commit()
               print('Data deleted successfully!')
           else:
                print('Wrong Entry')
        except:
            print('Somethng worng, please check')
        finally:
            connection.close()