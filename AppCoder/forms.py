from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profesor


class CursoFormulario(forms.Form):
    
    #especificar los campos
    
    curso = forms.CharField(max_length=30)
    camada = forms.IntegerField()
    
    
class ProfesorFormulario(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'email', 'profesion']
    

class EstudianteFormulario(forms.Form):
    
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    
    
class EntregableFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    fecha_De_Entrega = forms.DateField()
    entregado = forms.BooleanField()
    
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields} 
        
        
class UserEditForm(UserCreationForm):

    #Acá se definen las opciones que queres modificar del usuario, 
    #Ponemos las básicas
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    
    last_name = forms.CharField()
    first_name = forms.CharField()


    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2',"last_name","first_name"] 
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}
        

class AvatarFormulario(forms.Form):

    #Especificar los campos
    
    imagen = forms.ImageField(required=True)
    
    
    
class MensajeForm(forms.Form):
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}))
