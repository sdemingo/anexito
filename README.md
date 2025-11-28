# Anexito

Autorellenador de campos de formularios en PDF


## Dependencias

Necesita la librería [fillpdf](https://github.com/t-houssian/fillpdf). Para instalarla usar `pip`:

```
pip install fillpdf
```

El script ha sido probado sobre Linux Debian 12.


## Uso

Edita el fichero `datos.py` con los parámetros apropiados a tus necesidades. En el caso de los módulos o asignaturas recuerda seguir el formato indicado. Escribiendo en líneas separadas tanto los códigos como los nombres de estos módulos separados por una coma.

Escribe los nombres completos de los alumnos en el fichero `nombres.txt` o en otro fichero a tu elección. Introduce uno por línea y usa la coma para separar el nombre del apellido como en el ejemplo:

```
Sergio,García
Jose María,Ruíz del Olmo
Francisco José,Pérez
Marta,García
Pablo Antonio,de Miguel
```

Una vez hecho esto solo necesitas ejecutar cambiando `fichero-nombres.txt` por el nombre del fichero donde hayas escrito los nombres:

* `./anexito -a1 fichero-nombres.txt`: Para obtener los Anexos I
* `./anexito -a2 fichero-nombres.txt`: Para obtener los Anexos II

Los anexos son creados en un directorio local llamado `anexos`. En caso de querer obtener una versión no editable de los ficheros PDF generados se puede usar el script `imprimir` que viene incluido en el directorio. 

