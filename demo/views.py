from django.shortcuts import render
from .forms import Register_form
from .models import Register


# Create your views here.
def home(request):
	return render(request,'home.html')

def register(request):
	# import pdb;pdb.set_trace()
	return render(request,'register.html')

def login(request):
	return render(request,'login.html')

def demo(request):
	if request.method == 'POST':
		form = Register_form(request.POST)

		if form.is_valid():
			email = form.cleaned_data['email']
			password = form.cleaned_data['psw']
			repeat_password = form.cleaned_data['psw_repeat']

			e = Register(email=email,password=password,repeat_password=repeat_password)
			e.save()

	else:
		form = Register_form()
	return render(request,'register.html',{'form':form})