from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings 
from gestionPedidos.forms import FormularioContacto

def contacto(request):
	if request.method == "POST":
		
		"""subject=request.POST["asunto"]#rescato lo que viene en el subject

		message=request.POST["mensaje"] + " " + request.POST["email"]#acá rescato lo que viene en el msj y el mail del usuario para poder contactarme

		email_from=settings.EMAIL_HOST_USER #especifica de DONDE viene el email, este es el email host user, el que yo puse

		recipient_list=["paki_93lot@hotmail.com"]#donde queremos que viaje esa información	

		send_mail(subject, message, email_from, recipient_list)

		return render(request, "gracias.html")

	return render(request, "contacto.html")"""

		miFormulario=FormularioContacto(request.POST)

		if miFormulario.is_valid ():

			#se guarda toda la información en esta nueva variable
			infForm=miFormulario.cleaned_data

			#acá pedimos la información del formulario, en los dos primero parámetros rescato el asunto y el msj
			#en el tercer parám enviar esa info, el 1° mail que introdujo el usuario y el 2° este mail es el del remitente, la del servidor
			#el 4° parám es el mail donde queremos que nos llegue la info
			send_mail(infForm['asunto'], infForm['mensaje'], infForm.get('email',''),[paki_93lot@hotmail.com])

			return render(request, "gracias.html")

	else:
		#cuando se salta el primer IF pq el usuario todavía no coloca ningun daot
		#pasa a este else, que creo un formulario vacío, que ahora se va a llenar
		miFormulario=FormularioContacto()

	#con esto vamos a hacer que construya un html con la información que hay dentro
	#el 1° parám es el request, el 2° es en html que voy a llenr, el 3° es el formulario que debe utilizar
	return render (request, "formuContacto.html")
