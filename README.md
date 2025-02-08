# Anexito

Autorellenador de campos de formularios en PDF


## Dependencias

Necesita la librería [fillpdf](https://github.com/t-houssian/fillpdf). Para instalarla usar `pip`:

```
pip install fillpdf
```

## Uso

Edita el fichero `datos.py` con los parámetros de curso, grupo, módulo, etc. apropiados a tus necesidades. Escribe los nombres completos de los alumnos en el fichero `nombres.txt`. Introduce uno por línea y usa la coma para separar el nombre del apellido como en el ejemplo:

```
Sergio,García
Jose María,Ruíz del Olmo
Francisco José,Pérez
Marta,García
Pablo Antonio,de Miguel
```

Una vez hecho esto solo necesitas ejecutar:

* `./anexito -a1`: Para obtener los Anexos I
* `./anexito -a2`: Para obtener los Anexos II

Los anexos son creados en un directorio local llamado `anexos`.



