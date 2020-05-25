from django import forms
from misiones.models import mision
class misionForm(forms.ModelForm):
	class Meta:
		model=mision
		fields=['nombreClave','misiones','fecha','lugar']
		labels={'nombreClave':'Nombre de la mision'}
		labels={'misiones':'Tipo de mision'}
		widget={'nombreClave':forms.TextInput()}
		
	

		
	def __init__(self,*args,**kwargs):
		super().__init__ (*args,**kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class':'form-control'
			})
			
			