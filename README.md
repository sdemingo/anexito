# anexito

Autorellenador de campos de formularios en PDF


## Dependencias

Necesita la librería [fillpdf](https://github.com/t-houssian/fillpdf). Para instalarla usar `pip`:

```
pip install fillpdf
```

## Ejemplo de uso de la librería

Para sobreescribir varios campos usar un diccionario como muestra el ejemplo:

```
data_dict = {
'Campo1': 'valor del campo2',
'Campo2': 'valor del campo2',
}

fillpdfs.write_fillable_pdf('formulario.pdf', 'nuevo.pdf', data_dict)

```

Para conseguir los nombres de los campos incluidos en el documento se puede usar el comando `extractfillpdf` incluido con la librería. Este comando genera un archivo JSON con todos los nombres.

```
$ extractfillpdf formulario.pdf
```




