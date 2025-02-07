# Anexito

Autorellenador de campos de formularios en PDF


## Dependencias

Necesita la librería [fillpdf](https://github.com/t-houssian/fillpdf). Para instalarla usar `pip`:

```
pip install fillpdf
```

## Uso

Edita el fichero `datos.py` con los parámetros de curso, grupo, módulo, etc. apropiados a tus necesidades. Escribe los nombres completos de los alumnos en el fichero `nombres.txt`. Uno por línea. Tras todo esto solo queda ejecutar:

* `./anexito -a1`: Para obtener los Anexos I
* `./anexito -a2`: Para obtener los Anexos II

Los anexos son creados en un directorio local llamado `anexos`.



