from re import template
from django.shortcuts import render
from django.views.generic.edit import FormView
from QueryForm.forms import Formulario
from QueryForm.models import Form
from google.cloud import bigquery
from google.cloud import storage

# Create your views here.
class QueryForm(FormView):
    template_name = 'QueryForm/form.html' # enlaza ek html a la clase
    form_class = Formulario # llama el formulario dentro de la clase vista template

    def post(self,request,*arg,**kwargs): # se crea un metodo POST generar la consulta al darle inseertar
        form = Formulario() # se inicializa el formulario
        # client = bigquery.Client(project='sod-co-bi-sandbox') # proyecto de GCP
        if request.method == 'POST': # ingresa el metodo a ejecutar al presionar el submit
            form = Formulario(data=request.POST) # inicializa los datos en el modleo db
            if form.is_valid(): # si hay datos
                form.save() # se guardan en la tabla de DB
                formu = dict(request.POST) # se convierte los datos a diccionario
                formu = [{'qname': formu['qname'][0],'select': formu['select'][0],'fecha': formu['fecha'][0]}]  # se organiza los campos 
                print(formu)
                # errors = client.insert_rows_json("Nombre de la tabla", formu)  # nombre de la tabla a insertar y formu( los campos a insertar)
                # if errors == []:# si esta vacia
                #     print("New rows have been added.")
                # else:
                #     print("Encountered errors while inserting rows: {}".format(errors))
        return render(request,self.template_name)
    
    def form_valid(self, form):
        return super().form_valid(form)