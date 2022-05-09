import arttable
import conexion


def validacionURL(art, enlace):
    consulta = conexion.getconnection()
    vconsulta = consulta.cursor()
    query = "Select URL From NSFW as A where A.URL LIKE (?)"
    result = vconsulta.execute(query, enlace).fetchval()
    return bool(result)

def validacionArtist(art):
    consulta = conexion.getconnection()
    vconsulta = consulta.cursor()
    query = "Select Artist From NSFW as A where A.Artist LIKE (?)"
    result = vconsulta.execute(query, art).fetchval()
    return bool(result)

def discordattachment(url,artist):
    consult = conexion.getconnection()
    vconsult = consult.cursor()
    flag = validacionURL(artist,url)
    if(flag == False):
        query = "INSERT INTO  NSFW(Artist, URL) VALUES (?, ?)"
        result = vconsult.execute(query, artist, url)
        vconsult.commit()
    else:
        print('Data already in the database')

class prueba:
    def insert(art,enlace):
        lconsult = conexion.getconnection()
        consult = lconsult.cursor()
        flag = validacionURL(art,enlace)
        if(flag == False):
            query="INSERT INTO  NSFW(Artist, URL) VALUES (?, ?)"
            consult.execute(query,art,enlace)
            consult.commit()
        else:
            print("Dato repetido")


class listado:
    def nsfw():
        listconsult = conexion.getconnection()
        consult = listconsult.cursor()
        query="SELECT * FROM NSFW"
        lista = consult.execute(query).fetchall()
        return lista

class artistlist:
    def artlist(cantidad,artist):
        listconsult = conexion.getconnection()
        consult = listconsult.cursor()
        query="SELECT TOP (?) * FROM NSFW WHERE Artist like (?) "
        lista = consult.execute(query,cantidad,artist).fetchall()
        return lista

