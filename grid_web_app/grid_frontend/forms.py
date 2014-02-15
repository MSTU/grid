from django import forms

class CreateModelForm(forms.Form):
	model_type = forms.CharField(max_length=100)
	model_name = forms.CharField()
	model_file = forms.FileField(required=False)

class CreateLoadcaseForm(forms.Form):
	name = forms.CharField()
	description = forms.CharField()
	model = forms.CharField()