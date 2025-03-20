# Sistema de Tienda con Flask-Login

Este es un sistema de tienda web desarrollado con Flask que implementa autenticación de usuarios, roles de administrador y cliente, y gestión de pedidos.

## 🚀 Características

- Autenticación de usuarios con Flask-Login
- Roles de usuario (Administrador y Cliente)
- Gestión de productos
- Sistema de pedidos
- Interfaz moderna con Tailwind CSS
- Protección CSRF
- Base de datos MySQL

## 📋 Requisitos Previos

- Python 3.10 o superior
- MySQL Server

## 🔧 Instalación

1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd Flask-Login
```

2. Crear y activar un entorno virtual:
```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar la base de datos:
- Crear una base de datos MySQL llamada `bdidgs805`
- Asegurarse de que las credenciales en el archivo `.env` sean correctas

## ⚙️ Configuración

1. Crear un archivo `.env` en la raíz del proyecto con el siguiente contenido:
```env
# Configuración de la base de datos
DATABASE_URL=mysql+pymysql://root:password@localhost/bdidgs805?charset=utf8mb4

# Claves secretas para seguridad
SECRET_KEY=clave_secreta_muy_segura_123456789
WTF_CSRF_SECRET_KEY=clave_csrf_muy_segura_123456789

# Configuración de la aplicación
FLASK_APP=app.py
FLASK_ENV=development
FLASK_DEBUG=1
```

## 🚀 Ejecución

1. Activar el entorno virtual si no está activado:
```bash
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate
```

2. Iniciar la aplicación:
```bash
python app.py
```

3. Acceder a la aplicación:
- Abrir el navegador y visitar `http://localhost:5000`

## 👥 Usuarios por Defecto

### Administrador
- Usuario: `admin123`
- Contraseña: `admin123`

### Cliente
- Registrarse como nuevo usuario en la página de registro

## 📁 Estructura del Proyecto

```
Flask-Login/
├── app.py              # Aplicación principal
├── config.py           # Configuraciones
├── forms.py            # Formularios
├── models.py           # Modelos de base de datos
├── requirements.txt    # Dependencias
├── .env               # Variables de entorno
└── templates/         # Plantillas HTML
    ├── layout.html    # Plantilla base
    ├── login.html     # Página de inicio de sesión
    ├── registro.html  # Página de registro
    ├── home.html      # Página principal
    ├── tienda.html    # Página de productos
    └── pedidos.html   # Página de pedidos
```

## 🔒 Seguridad

- Protección CSRF implementada
- Autenticación de usuarios
- Roles y permisos
- Validación de formularios
- Manejo seguro de sesiones

## 🛠️ Tecnologías Utilizadas

- Flask
- Flask-Login
- Flask-SQLAlchemy
- Flask-WTF
- MySQL
- Tailwind CSS
- Python-dotenv

## 📝 Notas Importantes

- En producción, asegúrate de:
  - Cambiar las claves secretas
  - Implementar hashing de contraseñas
  - Configurar HTTPS
  - Deshabilitar el modo debug
  - Usar variables de entorno seguras

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, asegúrate de:
1. Hacer fork del repositorio
2. Crear una rama para tu feature
3. Hacer commit de tus cambios
4. Hacer push a la rama
5. Abrir un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles. 
