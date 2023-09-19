from marshmallow import fields

from app.ext import ma
from app.db import db, BaseModelMixin
import datetime

class TerapeutaSchema(ma.Schema):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    especialidad = db.Column(db.String(100), nullable=False)
    experiencia = db.Column(db.Integer, nullable=False)
    direccion_consulta = db.Column(db.String(200))
    fecha_inicio_practica = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    estado = db.Column(db.String(20), default='Activo')
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

class GerenteSchema(ma.Schema):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    departamento = db.Column(db.String(100))
    numero_contacto = db.Column(db.String(15))
    correo = db.Column(db.String(100))
   

class RecepcionistaSchema(ma.Schema):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    edad = db.Column(db.Integer)
    turno = db.Column(db.String(50))
    fecha_contratacion = db.Column(db.Date)
    salario = db.Column(db.Float)

class EspecialistaEnMarketingSchema(ma.Schema):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    edad = db.Column(db.Integer)
    genero = db.Column(db.String(10))
    telefono = db.Column(db.String(15))
    fecha_contratacion = db.Column(db.Date)
    area_especializacion = db.Column(db.String(50))
    proyectos_realizados = db.Column(db.Integer)
    activo = db.Column(db.Boolean)
    
class IntendenteSchema(ma.Schema):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    edad = db.Column(db.Integer)
    genero = db.Column(db.String(15))
    cargo = db.Column(db.String(50))
    salario = db.Column(db.Float)
    fecha_contratacion = db.Column(db.Date)
    