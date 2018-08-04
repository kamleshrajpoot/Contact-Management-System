#!python
#log/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import User_info
from django.shortcuts import redirect

# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating
@login_required(login_url="login/")
def home(request):
	information=User_info.objects.all()
	return render(request,"home.html",{'information':information})

@login_required(login_url="login/")
def createcontact(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			name = request.POST['user_name']
			email = request.POST['email']
			contact = request.POST['contact_number']
			requestcommunitycreation = User_info.objects.create(
				name = name,
				email  = email,
				contact = contact
				)
			return redirect('home')
		else:
			return render(request, 'createcontact.html')
	else:
		return redirect('login')

@login_required(login_url="login/")
def update(request,pk):
	if request.user.is_authenticated:
		user = User_info.objects.get(pk=pk)
		if request.method == 'POST':
			user.name = request.POST['user_name']
			user.email = request.POST['email']
			user.contact = request.POST['contact_number']
			user.save(update_fields=["name","email","contact"])
			return redirect('home')
		else:
			return render(request, 'update.html', {'user':user})
	else:
		return redirect('login')

@login_required(login_url="login/")
def delete(request, pk):
	if request.user.is_authenticated:
		user = User_info.objects.get(pk=pk)
		user.delete()
		return redirect('home')
	else:
		return redirect('login')

