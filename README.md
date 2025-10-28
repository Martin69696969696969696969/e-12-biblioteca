# 📚 Sistema de Biblioteca — Proyecto Refactorizado (Buenas Prácticas y Seguridad)

🚀 Proyecto desarrollado aplicando principios SOLID, seguridad en base de datos y cifrado de contraseñas con bcrypt.
Conexión a base de datos MySQL mediante consultas totalmente parametrizadas.

✅ Mejoras implementadas respecto al código original
Característica	Antes	Ahora
Estructura del proyecto	Todo en un solo archivo	Arquitectura modular
Principios SOLID	❌	✅ Aplicados
Seguridad SQL	Consultas vulnerables	Consultas parametrizadas
Manejo de contraseñas	Guardadas en texto plano ❌	Encriptación con bcrypt ✅
Logging	Parcial	Logging completo con gestión de errores
Mantenibilidad	Baja	Alta y escalable
📂 Estructura del proyecto
biblioteca/
│
├── conexion.py
├── main.py
│
└── modelos/
    ├── libro.py
    ├── usuario.py
    └── prestamo.py


✅ Separación de responsabilidades
✅ Código mantenible y escalable
✅ Fácil de extender (Autores, Categorías, Multas, etc.)

🛠️ Tecnologías utilizadas

✅ Python 3.10+

✅ MySQL Server / MySQL Workbench

✅ Bcrypt para encriptación

✅ PEP8 & logging

🔐 Seguridad aplicada

Hashing de contraseñas con bcrypt

Validaciones de entrada

Consultas SQL seguras → Prevención de Inyección SQL

Manejo de errores sin exponer información sensible del servidor

📌 Requerimientos

Instalar dependencias:

pip install bcrypt
pip install mysql-connector-python

🔧 Configuración de la Base de Datos

En MySQL crear la base y tablas con:

CREATE DATABASE biblioteca;
USE biblioteca;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    tipo ENUM('estudiante','profesor','admin') NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE libros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    autor VARCHAR(100),
    anio INT,
    disponible BOOLEAN DEFAULT TRUE
);

CREATE TABLE prestamos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    id_libro INT,
    fecha_prestamo DATE,
    fecha_devolucion DATE,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
    FOREIGN KEY (id_libro) REFERENCES libros(id)
);

▶️ Ejecución del programa

Desde la terminal:

python main.py


Menú principal:

1. Usuarios
2. Libros
3. Salir


✅ Alta de usuarios con contraseña segura
✅ Alta de libros
✅ Listo para agregar más funciones (préstamos, devoluciones, login)

📸 Capturas de ejemplo

(Coloca aquí tus capturas de ejecución en consola desde GitHub)

🌟 Trabajo Extra (opcional)

✅ Implementar deliberadamente una inyección SQL y demostrar el ataque
✅ Documentar el proceso
✅ Presentar evidencia en clase
➡️ Listo para implementarse si se solicita

👨‍💻 Autor

Nombre del estudiante: Tu nombre aquí

Materia: Seguridad Informática / Fundamentos de Programación

Universidad: CGUTyP

✅ Estado del proyecto: Finalizado con mejoras

📌 Puedes ampliar el sistema con autenticación, roles avanzados, gestión de multas, reportes y más.
