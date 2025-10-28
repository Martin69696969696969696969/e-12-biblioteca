# 📚 Sistema de Biblioteca — Proyecto Refactorizado

Proyecto de un sistema de gestión de biblioteca en Python, refactorizado aplicando buenas prácticas (principios SOLID), seguridad en base de datos y cifrado de contraseñas con bcrypt. Conexión a MySQL mediante consultas parametrizadas.

## 📌 Contenido de este README

Descripción

Estructura del proyecto

Tabla de características

Requisitos e instalación

Configuración de base de datos (SQL)

Ejecución del sistema

Seguridad aplicada

Trabajo extra (inyección SQL)

Autor

## 📝 Descripción

Este proyecto es una mejora del sistema de biblioteca original del Ejercicio 11.
Se reestructura el código para hacerlo más seguro, modular y mantenible.

Aplicaciones principales del refactor:

✅ Principios SOLID

✅ Contraseñas cifradas con bcrypt

✅ Consultas SQL seguras

✅ Registro de logs

✅ Arquitectura escalable

## 📂 Estructura del proyecto
``` bash
biblioteca/
│
├── conexion.py
├── main.py
│
└── modelos/
    ├── libro.py
    ├── usuario.py
    └── prestamo.py
```

✅ Mejor organización del código

✅ Separación de responsabilidades (SRP)

## 🔍 Tabla de características
###Antes
Característica
Estructura del proyecto	❌ Un solo archivo	

Principios SOLID	❌	

Contraseñas seguras	❌ Texto plano	

Seguridad SQL	❌ Vulnerable	

Mantenibilidad	❌	Baja	

Logging	Parcial	❌	

Validaciones	❌	Básicas	

### Ahora
Estructura del proyecto ✅ Módulos separados

Principios SOLID ✅ Sí

Contraseñas seguras ✅ Hash bcrypt

Seguridad SQL ✅ Parametrizada

Mantenibilidad Alta ✅

Logging	Parcial ✅ Completo

Validaciones ✅ Robustas
## 🛠 Requisitos e instalación

Requisitos:

Python 3.8+

MySQL Server + Workbench opcional

Instalación de dependencias:

pip install bcrypt mysql-connector-python


Sugerencia: usar entorno virtual

python -m venv venv
.\venv\Scripts\Activate.ps1    # Windows PowerShell
pip install bcrypt mysql-connector-python

## 🗄️ Configuración de base de datos

Ejecuta en MySQL Workbench o consola:
``` bash
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
```
## ▶️ Ejecución

Ejecuta desde consola:

python main.py


Menú inicial:

1. Usuarios
2. Libros
3. Salir


✅ Registrar usuarios con contraseña segura

✅ Registrar libros en la base de datos

## 🔒 Seguridad aplicada

✅ Cifrado bcrypt → No se guardan contraseñas en claro

✅ Prevención de inyección SQL con consultas parametrizadas

✅ Manejo de errores sin filtrar información

✅ Recomendado principio de mínimo privilegio en usuario MySQL

## ➕ Trabajo Extra (Opcional)

Se puede incluir:

📌 Implementar una vulnerabilidad SQL en una rama separada

📌 Mostrar un ataque de inyección SQL exitoso

📌 Documentar el ataque para presentación en clase

(Disponible si tu docente solicita punto extra)

## 👤 Autor

Nombre: Martin
Materia: Seguridad Informática / Bases de Datos
Docente: profe Jorge
Institución: utc
Fecha: 28/10/2025
