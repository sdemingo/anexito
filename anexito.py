from fillpdf import fillpdfs

fillpdfs.get_form_fields("formulario.pdf")

# returns a dictionary of fields
# Set the returned dictionary values a save to a variable
# For radio boxes ('Off' = not filled, 'Yes' = filled)

data_dict = {
'Texto2': 'hooooooola',
'Texto4': 'Adiooos',
'Texto1': 'vamoooooooS',
}

fillpdfs.write_fillable_pdf('formulario.pdf', 'new.pdf', data_dict)

# If you want it flattened:
fillpdfs.flatten_pdf('formulario.pdf', 'newflat.pdf')
