from django import forms
from .models import *

class generalImageForm(forms.ModelForm):
	class Meta:
		model = ImageForm
		fields = ['name','image']