import db_connection as dbConn

class Read:
    def func_ReadData(self):   
        # Get the sql connection
        connection = dbConn.getConnection()
        cursor = connection.cursor()

        # Execute the sql query
        cursor.execute('Select * from Employee')

        # Print the data
        for row in cursor:
            print('row = %r' % (row,))
