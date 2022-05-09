import pyodbc
class tconx():
    def pruebaconexion():
        try:
            conn_str = pyodbc.connect("Driver={SQL Server};"
                              "Server=(local)\SQLExpress;"
                              "Database=HoloHell;"
                              "Trusted_Connection=yes;")
        except:
            print("Error de conexion")
        return conn_str

def getconnection():
    return tconx.pruebaconexion()