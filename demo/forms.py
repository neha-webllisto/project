from django import forms

class Register_form(forms.Form):
	email = forms.EmailField()
	psw = forms.CharField(max_length=20)
	psw_repeat = forms.CharField(max_length=20)