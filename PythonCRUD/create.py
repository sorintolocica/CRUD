import db_connection as dbConn

class Create:
    def func_CreateData(self):

        # Get the sql connection
        connection = dbConn.getConnection()
                
        name = input('Enter Name = ')
        age = input('Enter Age = ')

        try:
           query = "Insert Into Employee(Name, Age) Values(?,?)" 
           cursor = connection.cursor()

           # Execute the sql query
           cursor.execute(query, [name, age])

           # Commit the data
           connection.commit()
           print('Data Saved Successfully')

        except:
             print('Somethng worng, please check')

        finally:
           # Close the connection
           connection.close()
