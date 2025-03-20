from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)  # Hash en producción
    role = db.Column(db.String(10), nullable=False)  # ADMIN o USER

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)
    precio = db.Column(db.Float, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)

    def __init__(self, nombre, precio, cantidad):
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a 0")
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precio_total = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False, default=datetime.now)
    estado = db.Column(db.String(20), nullable=False, default='PENDIENTE')

    user = db.relationship('User', backref='pedidos')
    producto = db.relationship('Producto', backref='pedidos')