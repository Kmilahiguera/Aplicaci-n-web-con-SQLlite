from db import db


class Estudiante(db.Model):

    #Nombre de tabla
    
    __tablename__="estudiante"

    #Conjunto de atributos que van a ser los campos de la tabla

    #llave primaria

    id=db.Column(db.Integer, primary_key= True)

    nombre= db.Column(db.String(50)) #Permite crear una columna con el dato y definir que tipo de dato ademas del tamaño
    email= db.Column(db.String(70))
    codigo= db.Column(db.String(15))


    #Metodo cosntructor para mapaear datos en los campos definidos

    def __init__(self, nombre, email, codigo):

        self.nombre= nombre
        self.email= email
        self.codigo= codigo
