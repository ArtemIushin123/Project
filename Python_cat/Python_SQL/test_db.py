import pyodbc


def get_all_clients():
    connection_string = 'DRIVER={SQL Server};SERVER=.;DATABASE=DOCTOR;'
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute('select * from Client')
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result

