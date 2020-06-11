from django.contrib import admin
from catalog.models import Varietal, Vino, InfoTec, Bodega

# Register your models here.
class VarietalAdmin (admin.ModelAdmin):
	list_display=("nombre",)

class VinoAdmin (admin.ModelAdmin):
	list_display=("nombre","varietal","bodega","cosecha","region","infoTec","viticultura","vinicultura")

class InfoTecAdmin (admin.ModelAdmin):
	list_display=("alcohol","ph","acidez_total","cierre")

class BodegaAdmin (admin.ModelAdmin):
	list_display=("nombre_bodega",)	

admin.site.register(Varietal, VarietalAdmin)
admin.site.register(Vino, VinoAdmin)
admin.site.register(InfoTec, InfoTecAdmin)
admin.site.register(Bodega, BodegaAdmin)