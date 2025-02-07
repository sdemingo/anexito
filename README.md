# Anexito

Autorellenador de campos de formularios en PDF


## Dependencias

Necesita la librería [fillpdf](https://github.com/t-houssian/fillpdf). Para instalarla usar `pip`:

```
pip install fillpdf
```

## Uso

Escribir los nombres completos de los alumnos en el fichero `nombres.txt`. Uno por línea. 
Ejecutar:

* `./anexito -a1`: Para obtener los Anexos I
* `./anexito -a2`: Para obtener los Anexos II

Los anexos son creados en un directorio local llamado `anexos`.


