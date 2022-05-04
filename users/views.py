from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import authenticate, login , logout
from consultancy_portal.views import index  
from users.forms import UserRegistrationForm , ConsultantForm

#  register() is for visitor to register into the site 
def register(request):
	if request.method =='POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('consultancy_portal:index')
	else:
		form = UserRegistrationForm()
	return render(request, 'users/register.html',  {'form': form})
    
#  login_view() is for visitor to log in  the site
def login_view(request):
	if request.method=='POST':
		form=AuthenticationForm(request,data=request.POST)
		username=request.POST.get('username')
		password = request.POST.get('password') 
		user=authenticate(request,username=username, password=password)
		if form.is_valid():
			login(request,user)
			return redirect('consultancy_portal:index')
	else:
		form=AuthenticationForm()
	return render(request, 'users/login.html', {'form':form})

#  consultant_Register() is for consultant to register into the site
def consultant_Register(request):
	if request.method=='POST':
		form=ConsultantForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('users:consultant_login')
	else:
		form=ConsultantForm()
	return render(request,'users/consultant_Register.html',{'form':form})

#  consultant_login() is for consultant to log in  the site
def consultant_login(request):
	if request.method=='POST':
		form=AuthenticationForm(request,data=request.POST)
		username=request.POST.get('username')
		password = request.POST.get('password')
		designation=request.POST.get('designation')
		user=authenticate(request,username=username, password=password)
		if form.is_valid():
			login(request,user)
			return redirect('users:consultancy_index')
	else:
		form=AuthenticationForm()
	return render(request, 'users/consultant_login.html', {'form':form})

#consultancy_index provides a different home page to the consultant 
def consultancy_index(request):
    return redirect('consultancy_portal:index')
	
def logout_view(request):
	logout(request)
	return render(request, 'consultancy_portal/index.html')
	