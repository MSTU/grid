from django import forms
from grid_frontend.models import Loadcase


class JobForm(forms.Form):
	name = forms.CharField(required=True)
	description = forms.CharField(widget=forms.Textarea())
	loadcases = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=[(lc.name, lc.id) for lc in Loadcase.objects.all()])
	input_params = forms.CharField(widget=forms.Textarea())

class MathModelForm(forms.Form):
	model_type = forms.CharField(required=True)
	model_name = forms.CharField(required=True)
	model_file = forms.FileField(required=False)

class LoadcaseForm(forms.Form):
	name = forms.CharField(required=True)
	description = forms.Textarea()
	model = forms.Select()