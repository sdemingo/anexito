#!/usr/bin/python3

from fillpdf import fillpdfs

import sys


#fillpdfs.get_form_fields("formulario.pdf")
# returns a dictionary of fields

# Set the returned dictionary values a save to a variable
# For radio boxes ('Off' = not filled, 'Yes' = filled)

data_dict = {
'Alumnoa': 'Sergio',
'Check Box1': 'Yes',
'Check Box2': 'Yes',
'Check Box8': 'Yes',
'Check Box4': 'Yes',
'Check Box7': 'Yes',
'Check Box48': 'Yes',
'Check Box12': 'Yes',
'Check Box16': 'Yes',
'Check Box45.1.0': 'Yes',
}


if __name__=='__main__':

    if (len(sys.argv)<2):
        print ("Faltan argumentos")
        sys.exit(0)

    if (sys.argv[1] == "-l"):
        fillpdfs.print_form_fields("formulario.pdf")
        sys.exit(0)

    if (sys.argv[1] == "-p"):
        fillpdfs.write_fillable_pdf('formulario.pdf', 'new.pdf', data_dict)
        # If you want it flattened:
        #fillpdfs.flatten_pdf('formulario.pdf', 'newflat.pdf')


    print ("Argumetos  erróneos")





