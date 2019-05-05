from django import forms

# class UploadDocForm(forms.Form):
#     doc = 

from docs_management.models import ExtractedDoc


class ExtractedDocUpdateForm(forms.ModelForm):
	class Meta:
		model = ExtractedDoc
		fields = ["invoice_number", "summary"]

	def update_instance(self, instance, commit=True):
		for f in instance._meta.fields:
		    if f.attname in self.fields:
		        setattr(instance,f.attname,self.cleaned_data[f.attname])
		if commit:
		    try: 
		        instance.save()
		    except: 
		        return False
		return instance