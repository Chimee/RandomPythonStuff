import pypyodbc 
cnxn = pypyodbc.connect("Driver={SQL Server Native Client 11.0};"
                        "Server=LAPTOP-XXX\XXX;"
                        "Database=AdventureWorks2014;"
                        "Trusted_Connection=yes;")


cursor = cnxn.cursor()
cursor.execute('SELECT AddressID, AddressLine1 FROM Person.Address WHERE AddressID < 10')

for row in cursor:
    print('row = %r' % (row,))

    
