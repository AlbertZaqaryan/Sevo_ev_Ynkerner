from django.shortcuts import render, redirect
from .models import SliderActive, Category, SubCategory, Contact
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm, SubCategoryForm, ContactForm
# Create your views here.


def index(request):
    slider_active = SliderActive.objects.all()[0]
    slider = SliderActive.objects.all()[1:]
    category_list = Category.objects.all()
    sub_category_list = SubCategory.objects.all()
    return render(request, 'main/index.html', context={
        'slider_active':slider_active,
        'slider':slider,
        'category_list':category_list,
        'sub_category_list':sub_category_list
    })


def index_detail(request, id):
    slider_active = SliderActive.objects.all()[0]
    slider = SliderActive.objects.all()[1:]
    category_list = Category.objects.all()
    sub_category_list = SubCategory.objects.all()
    category_filter = Category.objects.filter(pk=id)
    return render(request, 'main/index_detail.html', context={
        'slider_active':slider_active,
        'slider':slider,
        'category_list':category_list,
        'sub_category_list':sub_category_list,
        'category_filter':category_filter
    })

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="main/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")

def prod(request, id):
	form = SubCategoryForm()
	cat = SubCategory.objects.get(pk=id)
	return render(request, 'main/prod.html', context={'form':form, 'cat':cat})


def contact(request):
	user_message = ''
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			Contact.objects.create(**form.cleaned_data)
			form = ContactForm()
			user_message = 'Good Job'
			return redirect('contact')
		else:
			user_message = 'Invalid form'
			
	else:
		form = ContactForm()
		user_message = ''
	return render(request, 'main/contact-us.html',context={
		'form':form,
		'user_message':user_message
    })