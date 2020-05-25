from django import forms
from personas.models import persona
class personaForm(forms.ModelForm):
	class Meta:
		model=persona
		fields=['nombre','relacion']
		labels={'Nombres':'Nombre de la relacion'}
		widget={'Nombres':forms.TextInput()}
		
	

		
	def __init__(self,*args,**kwargs):
		super().__init__ (*args,**kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class':'form-control'
			})
			
			