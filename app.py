from flask import Flask, render_template, redirect, url_for, flash, g, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_cors import CORS
from dotenv import load_dotenv
import os
from datetime import datetime
import forms as f
from models import db, User, Producto, Pedido

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

# Configuración de CSRF
app.config['WTF_CSRF_ENABLED'] = True
app.config['WTF_CSRF_SECRET_KEY'] = 'clave_csrf_secreta_123'
app.config['SECRET_KEY'] = 'clave_secreta_123'

# Inicializar CSRF antes de otras extensiones
csrf = CSRFProtect(app)
db.init_app(app)
CORS(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.before_request
def before_request():
    g.user = current_user

def crear_admin_default():
    admin = User.query.filter_by(username='admin123').first()
    if not admin:
        admin = User(
            username='admin123',
            password='admin123',  # En producción, usar hashing
            role='ADMIN'
        )
        db.session.add(admin)
        db.session.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = f.LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:  # Usar hashing en producción
            login_user(user)
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('home'))
        flash('Credenciales inválidas', 'danger')
    return render_template('login.html', form=form)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = f.RegistroForm()
    if form.validate_on_submit():
        # Verificar si el usuario ya existe
        if User.query.filter_by(username=form.username.data).first():
            flash('El nombre de usuario ya está en uso. Por favor, elige otro.', 'danger')
            return render_template('registro.html', form=form)
        
        try:
            nuevo_usuario = User(
                username=form.username.data,
                password=form.password.data,  # Usar hashing en producción
                role='USER'
            )
            db.session.add(nuevo_usuario)
            db.session.commit()
            flash('Registro exitoso. Por favor, inicia sesión.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash('Error al registrar el usuario. Por favor, intenta de nuevo.', 'danger')
    
    return render_template('registro.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sesión cerrada', 'info')
    return redirect(url_for('index'))

@app.route('/home')
@login_required
def home():
    return render_template('home.html')

@app.route('/perfil')
@login_required
def perfil():
    return render_template('perfil.html')

@app.route('/pedidos')
@login_required
def pedidos():
    pedidos = Pedido.query.filter_by(user_id=g.user.id).all()
    return render_template('pedidos.html', pedidos=pedidos)

@app.route('/tienda')
def tienda():
    productos = Producto.query.all()
    return render_template('tienda.html', productos=productos)

@app.route('/realizar_pedido', methods=['POST'])
@login_required
def realizar_pedido():
    try:
        producto_id = request.form.get('producto_id')
        cantidad = int(request.form.get('cantidad', 1))
        
        if not producto_id:
            flash('No se especificó un producto', 'danger')
            return redirect(url_for('tienda'))
        
        producto = Producto.query.get_or_404(producto_id)
        
        if cantidad <= 0:
            flash('La cantidad debe ser mayor a 0', 'danger')
            return redirect(url_for('tienda'))
        
        if cantidad > producto.cantidad:
            flash('No hay suficiente stock disponible', 'danger')
            return redirect(url_for('tienda'))
        
        # Crear el pedido
        nuevo_pedido = Pedido(
            user_id=g.user.id,
            producto_id=producto.id,
            cantidad=cantidad,
            precio_total=producto.precio * cantidad,
            fecha=datetime.now(),
            estado='PENDIENTE'
        )
        
        # Actualizar el stock
        producto.cantidad -= cantidad
        
        db.session.add(nuevo_pedido)
        db.session.commit()
        
        flash('Pedido realizado con éxito', 'success')
        return redirect(url_for('pedidos'))
        
    except Exception as e:
        db.session.rollback()
        flash('Error al realizar el pedido', 'danger')
        return redirect(url_for('tienda'))

@app.route('/registro_producto', methods=['GET', 'POST'])
@login_required
def registro_producto():
    if g.user.role != 'ADMIN':
        flash('Acceso denegado. Solo los administradores pueden registrar productos.', 'danger')
        return redirect(url_for('home'))
    
    form = f.ProductoForm()
    if form.validate_on_submit():
        try:
            nuevo_producto = Producto(nombre=form.nombre.data, precio=form.precio.data, cantidad=form.cantidad.data)
            db.session.add(nuevo_producto)
            db.session.commit()
            flash('Producto registrado exitosamente', 'success')
            return redirect(url_for('home'))
        except ValueError as e:
            flash(str(e), 'danger')
        except Exception as e:
            flash('Error al registrar el producto', 'danger')

    return render_template('registro_producto.html', form=form)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        crear_admin_default()
    app.run(debug=True)