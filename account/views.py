from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import permission_required

# Create your views here.

def user_login(request):
	if request.method == 'POST':
		#instantiate login form
		form = LoginForm(request.POST)
		#check if form is valid
		if form.is_valid():
			cd = form.cleaned_data
			user  = authenticate(username=cd['username'], password = cd['password'])
			if user is not None:
				if user.is_active:
					login(request,user)
					return HttpResponse('Authenticated successfully')
				else:
					return HttpResponse('Disabled account')
			else:
				HttpResponse('Invalid Login')
	else:
		form = LoginForm()
	return render(request, 'account/login.html', {'form': form}) 

@permission_required
def dashboard(request):
	return render(request,'account/dashboard.html',{'section':'dashboard'})