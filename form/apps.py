from django.apps import AppConfig
# from .models import Hotel

class FormConfig(AppConfig):
    name = 'form'

    def ready(self):
    	import form.signals