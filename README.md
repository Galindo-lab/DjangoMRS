# DjangoMRS

Proyecto para la asignatura de Tecnologías Emergentes en el semestre 2023-2 de la Universidad Autónoma de Baja California.

DMRS es un sistema desarrollado en Django que facilita la gestión de reportes médicos. Permite a los usuarios programar citas y a los médicos recibir información de los pacientes durante su turno, además de realizar funciones de supervisión.


## Hacer las migraciones 
```
python config/manage.py makemigrations core
python config/manage.py migrate
```

## Crear unidades medicas
```
python config/manage.py createmedicalunits
```
