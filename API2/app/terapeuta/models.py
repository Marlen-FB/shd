#from operator import length_hint
#from sqlalchemy.orm import backref
from app.db import db, BaseModelMixin
import datetime


class Terapeuta(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    especialidad = db.Column(db.String(100), nullable=False)
    experiencia = db.Column(db.Integer, nullable=False)
    direccion_consulta = db.Column(db.String(200))
    fecha_inicio_practica = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    estado = db.Column(db.String(20), default='Activo')
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

    def __init__(self, nombre, especialidad, experiencia, direccion_consulta, usuario_id):
        self.nombre = nombre
        self.especialidad = especialidad
        self.experiencia = experiencia
        self.direccion_consulta = direccion_consulta
        self.usuario_id = usuario_id

    def __repr__(self):
        return f'Terapeuta({self.nombre}, {self.especialidad})'

    def __str__(self):
        return f'{self.nombre}, {self.especialidad}'


class Gerente(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    departamento = db.Column(db.String(100))
    numero_contacto = db.Column(db.String(15))
    correo = db.Column(db.String(100))
   
    def __init__(self, nombre, departamento, numero_contacto, correo, hospital_id):
        self.nombre = nombre
        self.departamento = departamento
        self.numero_contacto = numero_contacto
        self.correo = correo
        self.hospital_id = hospital_id

    def __repr__(self):
        return f'Gerente({self.nombre}, {self.departamento})'

    def __str__(self):
        return f'{self.nombre}, {self.departamento}'


class Recepcionista(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    edad = db.Column(db.Integer)
    turno = db.Column(db.String(50))
    fecha_contratacion = db.Column(db.Date)
    salario = db.Column(db.Float)

    def __init__(self, nombre, edad, turno, fecha_contratacion, salario):
        self.nombre = nombre
        self.edad = edad
        self.turno = turno
        self.fecha_contratacion = fecha_contratacion
        self.salario = salario

    def __repr__(self):
        return f'Recepcionista({self.nombre})'

    def __str__(self):
        return f'{self.nombre}'


class EspecialistaEnMarketing(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    edad = db.Column(db.Integer)
    genero = db.Column(db.String(10))
    telefono = db.Column(db.String(15))
    fecha_contratacion = db.Column(db.Date)
    area_especializacion = db.Column(db.String(50))
    proyectos_realizados = db.Column(db.Integer)
    activo = db.Column(db.Boolean)

    def __init__(self, nombre, edad, genero, telefono, fecha_contratacion, area_especializacion,
                 proyectos_realizados, activo=True):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.telefono = telefono
        self.fecha_contratacion = fecha_contratacion
        self.area_especializacion = area_especializacion
        self.proyectos_realizados = proyectos_realizados
        self.activo = activo

    def __repr__(self):
        return f'EspecialistaEnMarketing({self.nombre})'
    
    def __str__(self):
        return f'{self.nombre}'


class Intendente(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    edad = db.Column(db.Integer)
    genero = db.Column(db.String(15))
    cargo = db.Column(db.String(50))
    salario = db.Column(db.Float)
    fecha_contratacion = db.Column(db.Date)
    
    def __init__(self, nombre, edad, genero, cargo, salario, fecha_contratacion):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.cargo = cargo
        self.salario = salario
        self.fecha_contratacion = fecha_contratacion
    
    def __repr__(self):
        return f'Intendente({self.nombre})'
    
    def __str__(self):
        return f'{self.nombre} - {self.cargo}'


class Usuario(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String)
    password = db.Column(db.String)
    token = db.Column(db.String)

    def __init__(self, usuario, password):
        self.usuario = usuario
        self.password = password
        self.token = ""

    def __repr__(self):
        return f'Usuario({self.usuario})'
    def __str__(self):
        return f'{self.usuario}'
