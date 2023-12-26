# Proyecto Final Python - CoderHouse
#### Comisión: 56050 Alumno: Fons Augusto

## Nombre del Proyecto
Universidad Coder

## Descripción del Proyecto
Esta Web simula la lógica de una universidad donde se relacionan carreras, comisiones y alumnos. Un usuario común(estudiantes) podra al loguearse inscribirse
en una carrera, suscribirse a las novedades de la página y navegar por la misma. Un usuario administrador podra crear, editar y eliminar carreras y comisiones,
tambien podra eliminar alumnos inscriptos.

Aún tengo pendientes algunas cosas pensadas como agregar una paginación, mejorar estilos, fuentes, etc.

##### Front-End
- HTML / CSS / JS
- Bootstrap 5

##### Back-End
- Python / Django
- DBSqlite localmente
- PostgresQL en produccion

Para usar PostgresQL en producción use la libreria Supabase. En el archivo settings del proyecto esta el condicional para que en el caso de que la variable
de entorno DJANGO_ENV tenga el valor de 'production' se ejecute una base de datos de postgres. En ese caso se tendran que configurar las demás variables
de entorno que estan en .env.example con los valores de la libreria Supabase. De todos modos, para ejecutar localmente con DBSqlite hay que tener el archivo .env
con la variable DJANGO_ENV con un valor diferente a 'production'.
El deploy esta echo en Vercel.

## Video Explicación: https://drive.google.com/file/d/10rDlQZPyLIYMKcCiSDkhYAyEwvVta2YE/view?usp=drive_link

## Deploy: https://proyecto-python-coderhouse-fons-augusto.vercel.app/

