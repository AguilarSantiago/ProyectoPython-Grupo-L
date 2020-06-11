from django import forms

class FormularioContacto (forms.Form):
	#campos
	asunto=forms.CharField()
	email=forms.EmailField()
	mensaje=forms.CharField()